---
name: company-valuation
description: >
  Estimate the intrinsic value of a public company using DCF, relative (peer multiple),
  sum-of-parts (SOTP), and — for banks and financial institutions — Gordon Growth Model
  Justified P/BV with Adjusted P/BV scoring. Triangulate to an implied share price with
  upside/downside versus the current market price. Use this skill whenever the user asks:
  "what is AAPL worth", "valuation of NVDA", "fair value of TSLA", "intrinsic value",
  "DCF for MSFT", "build a DCF", "discounted cash flow", "WACC", "terminal value",
  "implied share price", "upside to fair value", "is X overvalued/undervalued",
  "relative valuation", "peer comparison valuation", "EV/EBITDA target", "SOTP",
  "sum of the parts", "how much is [company] worth", "price target from fundamentals",
  "value this company", "justified P/BV", "gordon growth model bank", "bank valuation",
  "NIM", "PPOP", "net interest margin", "ROE valuation", "P/BV bank", "price to book",
  "bank fair value", or any ticker in the context of computing intrinsic or relative
  valuation. Default to running ALL applicable methods and presenting a blended implied
  price with a sensitivity table. Do not answer valuation questions from memory — always
  run the workflow.
---

# Company Valuation

Triangulates intrinsic value via the applicable method set, then blends to an implied share price.

**Standard companies (non-bank):**
1. **DCF** — 5-year FCFF projection, discount at WACC, terminal value.
2. **Relative** — apply peer median P/E, EV/Revenue, EV/EBITDA.
3. **SOTP** — when 2+ distinct reporting segments exist, value each at pure-play peer multiples.

**Banks & financial institutions (sector = Financial Services / Banking / Insurance):**
1. **GGM Justified P/BV** — Gordon Growth Model: `(ROE − g) / (ke − g)` × Book Value Per Share.
2. **Adjusted Justified P/BV** — Base P/BV scored for governance, asset quality, franchise, liquidity, cycle.
3. **DDM** — Dividend Discount Model as supplementary check: `DPS / (ke − g)`.
4. **Relative P/BV & P/TBV** — peer-median price-to-book and price-to-tangible-book.

Always present a sensitivity table and Bull/Base/Bear scenarios.

**Data sourcing priority (all company types):**
- **Tier 1 — Primary ground truth:** S&P Capital IQ via MCP (if available), then company financial statements / exchange filings. State the filing period next to every figure. Flag any figure more than one quarter stale as `[STALE]`.
- **Tier 2 — yfinance:** Use for market data, peer multiples, and any figure not available in Tier 1.
- **Tier 3 — Regulatory filings by region:** HKEX/SSE/SZSE (China), BSE/NSE/RBI (India), SET/BOT (Thailand), IDX/OJK (Indonesia), HoSE/HNX/SBV (Vietnam).
- All figures in the company's local reporting currency. Never convert without disclosing the exchange rate and date.
- If S&P Capital IQ conflicts with a regulatory filing, report both and state the definition mismatch.

**Disclaimer**: Research/educational output. Not financial advice.

---

## Step 1: Detection Flow

Detect data source, runtime deps, and company type.

**Environment status:**

```
!`python3 -c "import yfinance, numpy, pandas; print('YFIN_OK')" 2>/dev/null || echo "YFIN_MISSING"`
```

```
!`(command -v funda && funda --version) 2>/dev/null || echo "FUNDA_CLI_MISSING"`
```

```
!`python3 -c "import yfinance as yf; t=yf.Ticker('^TNX'); p=t.fast_info.last_price; print(f'RF_10Y={p/100:.4f}')" 2>/dev/null || echo "RF_FETCH_FAIL"`
```

**Decision tree:**

| Condition | Method path |
|---|---|
| `YFIN_OK` | **Path A** (primary): yfinance for financials + peer multiples |
| `YFIN_MISSING` but funda available | **Path B**: delegate to `funda-data` skill for fundamentals |
| Both missing | **Path C**: `python3 -m pip install -q yfinance numpy pandas`, then Path A |
| `RF_FETCH_FAIL` | Use default `rf = 0.045` and note stale risk-free rate in output |

If `RF_10Y=` printed, use that value as `rf` in Step 4 instead of the hardcoded 4.5%.

**Bank detection:** After pulling `info`, check `sector` and `industry`. Route to **Step 4-Bank** if any of:
- `sector` contains "Financial Services", "Banking", "Insurance", "Financial"
- `industry` contains "Bank", "Insurance", "Diversified Financial", "Capital Markets", "Thrift"
- Ticker is known to be a bank/insurer (user states it, or S&P CIQ classification confirms)

---

## Step 2: Choose Methods & Set Defaults

### Method applicability

| Company type | Methods | Step |
|---|---|---|
| Mature cash-flow (CPG, telecom, utilities) | DCF primary + Relative | Step 4 → 5 |
| High-growth SaaS / software | DCF with care + Relative primary (EV/Rev + Rule of 40) | Step 4 → 5 |
| Multi-segment conglomerate | DCF + Relative + SOTP primary | Step 4 → 5 → 6 |
| **Banks / insurance / financial institutions** | **GGM Justified P/BV + Adjusted P/BV + DDM + Relative P/BV** | **Step 4-Bank** |
| Pre-revenue | EV/Revenue only | Step 5 only |
| REITs | P/FFO, P/AFFO, NAV-based | Step 5 only |
| Cyclicals (energy, semis, industrials) | DCF on mid-cycle + Relative | Step 4 → 5 |

### Defaults table (standard companies)

| Parameter | Default | Rationale |
|---|---|---|
| Projection horizon | 5 years | Standard explicit forecast window |
| Terminal growth `g` | 2.5% | ~long-run US GDP |
| Risk-free rate `rf` | Live 10Y UST from Step 1, else 4.5% | Current cost of capital anchor |
| Equity risk premium `erp` | **4.6%** (Damodaran implied, US) | Forward-looking implied ERP, NOT historical 5.5% average |
| Beta | Blume-adjusted: `0.33 + 0.67 × info['beta']` | Mean-reversion adjustment; raw yfinance beta is 5-yr monthly which overstates for high-beta names |
| Cost of debt `kd` | `interest_expense / total_debt`, else 5.5% | Effective rate; fallback to IG spread |
| Tax rate | 3-yr median effective rate, floored 15%, capped 30% | Strips out one-offs |
| Margin assumptions | 3-yr median of each ratio | Smooths cyclical noise |
| Peer count | 4-6 | Balances signal vs noise |
| Peer multiple | Median (not mean) | Robust to outliers |
| Method weights (no SOTP) | DCF 50% / Relative 50% | Equal triangulation |
| Method weights (with SOTP) | DCF 40% / Relative 30% / SOTP 30% | SOTP gets weight when applicable |
| Sensitivity grid | WACC ±1% in 0.5% steps × g from 1.5–3.5% in 0.5% | 5×5 matrix |

### Defaults table (banks)

| Parameter | Default | Rationale |
|---|---|---|
| ROE | 3-yr average net income / avg book equity | Smooths credit-cycle volatility |
| Sustainable growth `g` | ROE × (1 − dividend payout ratio) | Plowback method; cap at 6% |
| Cost of equity `ke` | `rf + beta × erp` (no WACC — debt is raw material for banks) | Standard bank ke |
| Payout ratio | DPS / EPS trailing, else 40% | Conservative default |
| Book value per share | Total equity / shares out | From balance sheet |
| Tangible book | Book equity − goodwill − intangibles | Flag if intangibles > 20% of book |
| Adjusted P/BV scoring | 5 factors × (−10% to +10%) each | See Step 4-Bank §4B-iv |
| Method weights (banks) | GGM 40% / Adjusted P/BV 30% / DDM 20% / Relative P/BV 10% | GGM anchors; DDM and relative as crosschecks |
| Sensitivity grid (banks) | ROE ±200bps × ke ±100bps | 5×5 matrix |

See `references/wacc_erp_rates.md` for sector ke benchmarks and regional risk-free rates.

---

## Step 3: Pull Data

### Standard companies

```python
import yfinance as yf
import numpy as np
import pandas as pd

TICKER = "AAPL"  # replace
t = yf.Ticker(TICKER)

info       = t.info
income_a   = t.income_stmt
cashflow_a = t.cashflow
balance_a  = t.balance_sheet
income_q   = t.quarterly_income_stmt
cashflow_q = t.quarterly_cashflow

earnings_est = t.earnings_estimate
revenue_est  = t.revenue_estimate

price      = info.get("currentPrice") or info.get("regularMarketPrice")
market_cap = info.get("marketCap")
shares_out = info.get("sharesOutstanding")
total_debt = info.get("totalDebt") or 0
cash       = info.get("totalCash") or 0
beta       = info.get("beta") or 1.0
sector     = info.get("sector")
industry   = info.get("industry")
```

Key financial statement rows (yfinance labels):

| Need | Row |
|---|---|
| Revenue | `Total Revenue` |
| EBIT | `Operating Income` |
| Net income | `Net Income` |
| D&A | `Depreciation And Amortization` (cashflow) |
| CapEx | `Capital Expenditure` (negative in cashflow) |
| ΔNWC | `Change In Working Capital` (cashflow) |
| SBC | `Stock Based Compensation` (cashflow) |

### Banks — additional data pull

```python
# Bank-specific balance sheet items
book_equity     = float(balance_a.loc["Stockholders Equity"].iloc[0])
goodwill        = float(balance_a.loc["Goodwill"].iloc[0]) if "Goodwill" in balance_a.index else 0
intangibles     = float(balance_a.loc["Other Intangible Assets"].iloc[0]) if "Other Intangible Assets" in balance_a.index else 0
tangible_equity = book_equity - goodwill - intangibles
bvps            = book_equity / shares_out
tbvps           = tangible_equity / shares_out

# Income items
net_income_series = [float(income_a.loc["Net Income"].iloc[i]) for i in range(min(3, income_a.shape[1]))]
book_eq_series    = [float(balance_a.loc["Stockholders Equity"].iloc[i]) for i in range(min(3, balance_a.shape[1]))]
avg_equity_series = [(book_eq_series[i] + book_eq_series[min(i+1, len(book_eq_series)-1)]) / 2 for i in range(len(net_income_series))]
roe_series        = [ni / ae for ni, ae in zip(net_income_series, avg_equity_series)]
roe               = np.mean(roe_series)   # 3-yr average

# Payout ratio and sustainable growth
dps          = info.get("dividendRate") or 0
eps_trailing = info.get("trailingEps") or (net_income_series[0] / shares_out)
payout_ratio = min(dps / eps_trailing, 0.95) if eps_trailing > 0 else 0.40
g_sustainable = min(roe * (1 - payout_ratio), 0.06)  # cap at 6%

# Cost of equity (ke) — use CAPM, no WACC for banks
rf        = 0.045   # override with live RF from Step 1
erp       = 0.046   # Damodaran implied ERP (US, 2026)
beta_raw  = info.get("beta") or 1.0
beta_bank = 0.33 + 0.67 * beta_raw   # Blume adjusted
ke        = rf + beta_bank * erp
```

**Bank data from S&P Capital IQ (if MCP available — preferred over yfinance for banks):**
Pull: NIM, CIR (cost-to-income ratio), NPL/GNPA ratio, PCR (provision coverage ratio),
CASA ratio, Tier 1/CET1 capital ratio, net interest income, non-interest income,
pre-provision operating profit (PPOP), credit costs, loan growth. State period for each.

---

## Step 4: DCF Build (Standard Companies — skip for banks, go to Step 4-Bank)

```python
# 4a. Revenue growth path — fade from Y1 (consensus or hist CAGR) to terminal g
hist_cagr = (rev[-1] / rev[0]) ** (1 / (len(rev)-1)) - 1
y1 = float(revenue_est.loc["+1y", "growth"]) if "+1y" in revenue_est.index else hist_cagr
g_terminal = 0.025
growth_path = np.linspace(y1, g_terminal + 0.01, 5)

# 4b. Margins — 3y median
ebit_margin = float((income_a.loc["Operating Income"] / income_a.loc["Total Revenue"]).iloc[:3].median())
da_pct      = float((cashflow_a.loc["Depreciation And Amortization"] / income_a.loc["Total Revenue"]).iloc[:3].median())
capex_pct   = float((cashflow_a.loc["Capital Expenditure"].abs() / income_a.loc["Total Revenue"]).iloc[:3].median())
nwc_pct     = float((cashflow_a.loc["Change In Working Capital"].abs() / income_a.loc["Total Revenue"]).iloc[:3].median())
tax_rate    = max(0.15, min(0.30, 0.21))  # use effective if available

# 4c. FCFF per year
rev_t = [float(income_a.loc["Total Revenue"].iloc[0])]
fcff  = []
for g in growth_path:
    rev_t.append(rev_t[-1] * (1 + g))
    ebit = rev_t[-1] * ebit_margin
    nopat = ebit * (1 - tax_rate)
    fcff.append(nopat + rev_t[-1]*da_pct - rev_t[-1]*capex_pct - rev_t[-1]*nwc_pct)

# 4d. WACC — four-step: formula → sector sanity → peer-implied WACC → adjudicate
rf  = 0.045   # override with live 10Y UST from Step 1
erp = 0.046   # Damodaran implied ERP (US, 2026) — NOT historical 5.5%
kd  = 0.055   # override with effective rate = interest_expense / total_debt

# Blume mean-reversion beta adjustment (standard industry practice)
# Raw yfinance beta is 5-yr monthly — high-beta names revert toward 1 over time
beta_raw    = beta  # from yfinance info["beta"]
beta_adj    = 0.33 + 0.67 * beta_raw   # Blume (1975) adjusted beta
ke = rf + beta_adj * erp
e_v = market_cap / (market_cap + total_debt)
d_v = 1 - e_v
wacc_formula = e_v*ke + d_v*kd*(1 - tax_rate)
# Always disclose: beta_raw, beta_adj, erp used, and resulting ke

# Step 4d-ii. Sector sanity band (from references/wacc_erp_rates.md)
# wacc_lo, wacc_hi = sector_band_low, sector_band_high

# Step 4d-iii. Peer-implied WACC — compute FULL WACC for EACH peer (not just ke)
# For each peer p in the §10 peer set:
#   beta_p    = yf.Ticker(p).info.get("beta") or sector_default_beta
#   mc_p      = yf.Ticker(p).info.get("marketCap")
#   debt_p    = yf.Ticker(p).info.get("totalDebt") or 0
#   int_exp_p = abs(yf.Ticker(p).cashflow.loc["Interest Expense"].iloc[0]) if available else 0
#   kd_p      = int_exp_p / debt_p if debt_p > 0 else 0.055
#   ke_p      = rf + beta_p * erp
#   ev_p      = mc_p / (mc_p + debt_p)
#   wacc_p    = ev_p*ke_p + (1-ev_p)*kd_p*(1 - tax_rate)
# peer_wacc_median = np.nanmedian([wacc_p for all peers with valid data])
#
# market_implied_ke = (1 / fwd_pe) + g_terminal   # use terminal g, not short-term consensus
#
# Step 4d-iv. Adjudication rule — MANDATORY, produces ONE adopted_wacc:
#   GAP = wacc_formula - peer_wacc_median
#   if GAP <= 0.015:                          # within 150bps of peer median
#       adopted_wacc = wacc_formula           # formula is close to peers; use it
#   else:                                     # formula WACC is >150bps above peer median
#       adopted_wacc = peer_wacc_median       # switch to peer-implied WACC as base
#       note: "Formula WACC {wacc_formula:.2%} exceeds peer median {peer_wacc_median:.2%}
#              by {GAP*100:.0f}bps (>150bps threshold). Using peer-implied WACC for
#              base case. Formula WACC retained for bear-case scenario only."
#
#   Bear scenario always uses max(wacc_formula, adopted_wacc + 0.01)
#   Bull scenario always uses adopted_wacc - 0.01
#
#   If market_implied_ke diverges from adopted_wacc by >300bps: disclose in output
#   (common for high-growth names; the gap represents market's growth optionality premium)

wacc = wacc_formula   # replace with adopted_wacc per Step 4d-iv above
# REQUIRED output box (6 columns):
# | formula_wacc | sector_band | peer_median_wacc | market_implied_ke | GAP(bps) | adopted_wacc | reason |

# 4e. Terminal value — compute both, use midpoint
tv_gordon = fcff[-1] * (1 + g_terminal) / (wacc - g_terminal)
tv_exit   = (rev_t[-1] * ebit_margin + rev_t[-1] * da_pct) * 15  # peer median EV/EBITDA
tv_base   = 0.5 * (tv_gordon + tv_exit)

# 4f. Bridge to equity
pv_fcff = sum(f / (1+wacc)**(i+1) for i, f in enumerate(fcff))
pv_tv   = tv_base / (1+wacc)**5
ev      = pv_fcff + pv_tv
equity  = ev + cash - total_debt
implied_price_dcf = equity / shares_out
```

**Gates:** (a) `wacc <= g_terminal` → stop; (b) `pv_tv/ev > 0.85` or `< 0.45` → flag, show both TV methods; (c) `wacc_formula` outside sector band → run Step 4d adjudication.

---

## Step 4-Bank: GGM / Justified P/BV Valuation (Banks & Financial Institutions)

> **Route here when bank detected in Step 1. Do not run Steps 4–6. Jump to Step 7 after this step.**

### 4B-i. GGM Justified P/BV

```python
# Core Gordon Growth Model for banks
# Justified P/BV = (ROE - g) / (ke - g)

justified_pb  = (roe - g_sustainable) / (ke - g_sustainable)
implied_price_ggm = justified_pb * bvps

# Gate: if ke <= g_sustainable, cap g at ke - 0.5% and flag
if ke <= g_sustainable:
    g_sustainable = ke - 0.005
    print("WARNING: g >= ke — capped g to ke - 0.5%")

print(f"ROE (3yr avg):       {roe:.2%}")
print(f"Sustainable g:       {g_sustainable:.2%}  (ROE × retention {1-payout_ratio:.0%})")
print(f"ke (CAPM):           {ke:.2%}")
print(f"Justified P/BV:      {justified_pb:.2f}x")
print(f"Book value/share:    {bvps:.2f}")
print(f"GGM implied price:   {implied_price_ggm:.2f}")
print(f"Current P/BV:        {price/bvps:.2f}x  (mkt price / BVPS)")
```

**Interpretation rule:** If current P/BV > Justified P/BV → stock is overvalued on ROE basis. If ROE < ke → bank is destroying equity value; justified P/BV < 1.0×.

### 4B-ii. Adjusted Justified P/BV

Score each factor on a continuous scale from −10% to +10% relative to neutral (0%).
Use explicit evidence from filings, transcripts, or financial ratios — not judgment alone.

```python
adjustments = {
    # Governance (+10% = strong independent board, low RPTs, clean audit, aligned mgmt incentives;
    #             -10% = material RPTs, SEC/regulator action, opaque related-party dealings)
    "governance": 0.0,

    # Asset Quality Trajectory (+10% = NPL declining, PCR >80%, slippage rate <1%;
    #                           -10% = NPL rising, PCR <50%, stress pools >5% of loan book)
    "asset_quality_trajectory": 0.0,

    # Franchise Quality (+10% = CASA >50%, pricing power, dominant market position;
    #                   -10% = CASA <25%, margin compression vs peers, deposit flight risk)
    "franchise_quality": 0.0,

    # Liquidity Risk (+10% = LDR <80%, excess liquidity, strong LCR;
    #                -10% = LDR >95%, reliance on wholesale funding, concentration in top 20 depositors)
    "liquidity_risk": 0.0,

    # Cycle Positioning (+10% = upcycle, NIM expanding, loan growth accelerating;
    #                   -10% = late cycle, NIM under pressure, credit cost guidance rising)
    "cycle_positioning": 0.0,
}

# State score and evidence for each factor explicitly in output
total_adj_pct = sum(adjustments.values())           # e.g. +15% total
adj_factor    = 1 + (total_adj_pct / 100)
adjusted_pb   = justified_pb * adj_factor
implied_price_adj = adjusted_pb * bvps

print(f"Adjustment factors:  {adjustments}")
print(f"Total adjustment:    {total_adj_pct:+.0f}%")
print(f"Adjusted P/BV:       {adjusted_pb:.2f}x")
print(f"Adjusted implied px: {implied_price_adj:.2f}")
```

### 4B-iii. DDM (Dividend Discount Model — supplementary)

```python
# Only run if bank pays a dividend; skip if payout < 10% or DPS = 0
if dps > 0 and payout_ratio >= 0.10:
    implied_price_ddm = dps * (1 + g_sustainable) / (ke - g_sustainable)
    print(f"DDM: DPS {dps:.2f} / (ke {ke:.2%} - g {g_sustainable:.2%}) = {implied_price_ddm:.2f}")
else:
    implied_price_ddm = None
    print("DDM: skipped — dividend yield below threshold")
```

### 4B-iv. Relative P/BV & P/TBV (peer comparison)

```python
# Select 4-6 listed bank peers in same geography and tier
BANK_PEERS = ["JPM", "BAC", "WFC", "C", "USB"]   # replace with relevant regional peers

bank_mults = {}
for p in BANK_PEERS:
    pi = yf.Ticker(p).info
    bi = yf.Ticker(p).balance_sheet
    ni = yf.Ticker(p).income_stmt
    bv = float(bi.loc["Stockholders Equity"].iloc[0]) if "Stockholders Equity" in bi.index else None
    shares_p = pi.get("sharesOutstanding")
    bvps_p = bv / shares_p if (bv and shares_p) else None
    price_p = pi.get("currentPrice")
    roe_p   = pi.get("returnOnEquity")
    bank_mults[p] = {
        "pb":  price_p / bvps_p if (price_p and bvps_p) else None,
        "pe":  pi.get("forwardPE"),
        "roe": roe_p,
        "div_yield": pi.get("dividendYield"),
    }

# Print peer table
print(f"{'Peer':8} {'P/BV':>8} {'Fwd P/E':>9} {'ROE':>8} {'Div Yld':>9}")
for p, v in bank_mults.items():
    pb_s   = f"{v['pb']:.2f}x"   if v['pb']   else "n/a"
    pe_s   = f"{v['pe']:.1f}x"   if v['pe']   else "n/a"
    roe_s  = f"{v['roe']:.1%}"   if v['roe']  else "n/a"
    div_s  = f"{v['div_yield']:.1%}" if v['div_yield'] else "n/a"
    print(f"{p:8} {pb_s:>8} {pe_s:>9} {roe_s:>8} {div_s:>9}")

peer_pb_median = np.nanmedian([v["pb"] for v in bank_mults.values() if v["pb"]])
implied_price_rel_bank = peer_pb_median * bvps
print(f"Peer median P/BV: {peer_pb_median:.2f}x → implied price: {implied_price_rel_bank:.2f}")

# ROE vs P/BV Gordon scatter check:
# A bank with ROE < ke should trade below 1x BV.
# Plot or table: each peer's ROE vs P/BV vs GGM implied P/BV to see who is cheap/expensive
for p, v in bank_mults.items():
    if v["roe"] and v["pb"]:
        ggm_p = (v["roe"] - g_sustainable) / (ke - g_sustainable)
        gap = v["pb"] - ggm_p
        print(f"{p}: actual P/BV {v['pb']:.2f}x vs GGM P/BV {ggm_p:.2f}x  gap {gap:+.2f}x")
```

### 4B-v. Banking Financial Model (3yr historical + 3yr forward)

Build this table in the output using hardcoded historicals from Tier-1 sources and forward assumptions consistent with the bull/base/bear scenarios. Forecasts must reflect credit cycle risks — do not extrapolate peak-cycle NIM or suppressed credit costs.

| Line Item ([CCY] [unit]) | FY−2A | FY−1A | FY0A | FY1F | FY2F | FY3F |
|---|---|---|---|---|---|---|
| **ASSUMPTIONS** | | | | | | |
| Loan growth (YoY %) | | | | | | |
| NIM (%) | | | | | | |
| NOII growth (YoY %) | | | | | | |
| CIR (%) | | | | | | |
| Credit cost (% of avg loans) | | | | | | |
| **BALANCE SHEET** | | | | | | |
| Gross loans | | | | | | |
| Avg interest-earning assets | | | | | | |
| Book equity | | | | | | |
| Tangible book equity | | | | | | |
| **INCOME STATEMENT** | | | | | | |
| Net interest income (NII) | | | | | | |
| Non-interest income (NOII) | | | | | | |
| Total operating income (TOI) | | | | | | |
| Operating expenses (OPEX) | | | | | | |
| Pre-provision operating profit (PPOP) | | | | | | |
| Provisions / credit costs | | | | | | |
| Pre-tax profit (PBT) | | | | | | |
| Net profit (PAT) | | | | | | |
| **KEY RATIOS** | | | | | | |
| ROE (%) | | | | | | |
| ROA (%) | | | | | | |
| Tier 1 / CET1 (%) | | | | | | |
| NPL / GNPA ratio (%) | | | | | | |
| Provision coverage ratio (PCR %) | | | | | | |
| LDR / LTD ratio (%) | | | | | | |
| Justified P/BV — GGM (×) | | | | | | |
| Adjusted Justified P/BV (×) | | | | | | |

### 4B-vi. Blend and Sensitivity (Banks)

```python
# Method weights for banks
w_ggm, w_adj, w_ddm, w_rel = 0.40, 0.30, 0.20, 0.10
ddm_w = implied_price_ddm if implied_price_ddm else implied_price_ggm  # fallback

implied_price_bank = (w_ggm * implied_price_ggm
                    + w_adj * implied_price_adj
                    + w_ddm * ddm_w
                    + w_rel * implied_price_rel_bank)

# 5x5 sensitivity: ROE (y-axis) × ke (x-axis)
roe_grid = [roe + dx for dx in (-0.02, -0.01, 0.0, 0.01, 0.02)]
ke_grid  = [ke  + dx for dx in (-0.01, -0.005, 0.0, 0.005, 0.01)]
print("P/BV sensitivity (GGM): ROE vs ke")
ke_hdr = "ROE \\ ke  " + "  ".join("ke={:.1%}".format(k) for k in ke_grid)
print(ke_hdr)
for r in roe_grid:
    row = "ROE={:.1%} ".format(r)
    for k in ke_grid:
        if k <= g_sustainable:
            row += "   n/a"
        else:
            pb = (r - g_sustainable) / (k - g_sustainable)
            px = pb * bvps
            marker = "*" if (abs(r-roe)<0.001 and abs(k-ke)<0.001) else " "
            row += "  {}${:.0f}".format(marker, px)
    print(row)

print(f"\nBlended bank implied price: {implied_price_bank:.2f}")
print(f"Current price:              {price:.2f}")
print(f"Upside/(downside):          {(implied_price_bank-price)/price*100:+.1f}%")
```

**Bull/Base/Bear scenarios (banks):**
- Shift ROE ±200bps, NIM ±25bps, credit cost ±30bps, ke ∓50bps, g ±50bps
- Bear must include one specific quantitative trigger: NIM collapse, NPL spike, or capital ratio breach
- State the target P/BV and implied price for each scenario

---

## Step 5: Relative Valuation (Standard Companies)

> **Skip for banks — relative P/BV is embedded in Step 4-Bank.**

Select 4-6 peers from `references/relative_valuation.md`.

```python
PEERS = ["MSFT", "ORCL", "CRM", "NOW", "SAP", "WDAY"]  # replace by industry
multiples = {}
for p in PEERS:
    pi = yf.Ticker(p).info
    multiples[p] = {
        "pe_fwd":   pi.get("forwardPE"),
        "ev_rev":   pi.get("enterpriseToRevenue"),
        "ev_ebitda":pi.get("enterpriseToEbitda"),
    }
med_pe   = np.nanmedian([v["pe_fwd"]    for v in multiples.values() if v["pe_fwd"]])
med_evr  = np.nanmedian([v["ev_rev"]    for v in multiples.values() if v["ev_rev"]])
med_eveb = np.nanmedian([v["ev_ebitda"] for v in multiples.values() if v["ev_ebitda"]])

eps_ttm    = info.get("trailingEps") or 0
rev_ttm    = info.get("totalRevenue") or 0
ebitda_ttm = info.get("ebitda") or 0
net_debt   = total_debt - cash

implied_pe      = med_pe   * eps_ttm
implied_ev_rev  = (med_evr  * rev_ttm    - net_debt) / shares_out
implied_ev_ebit = (med_eveb * ebitda_ttm - net_debt) / shares_out
implied_price_rel = np.nanmedian([x for x in [implied_pe, implied_ev_rev, implied_ev_ebit] if x])
```

Adjust peer median ±10–30% if target's growth or margin profile diverges materially. Always state the adjustment and reason.

---

## Step 6: SOTP (Standard Companies — multi-segment only)

> **Skip for banks.**

Skip unless the 10-K reports 2+ operating segments with distinct economics. yfinance does NOT expose segment data — user must supply or parse from filings.
- Identify segments + pure-play peer for each
- Apply peer median EV/EBITDA (or EV/Rev for growth segments)
- Subtract unallocated corporate costs (cap 2-5% of revenue if unknown)
- Subtract net debt, minority interest; divide by shares

SOTP discount = (SOTP price − market price) / SOTP price. Flag if >20%.

---

## Step 7: Triangulate, Sensitivity, Scenarios

### Standard companies

```python
if sotp_price is None:
    blended = 0.5*implied_price_dcf + 0.5*implied_price_rel
else:
    blended = 0.4*implied_price_dcf + 0.3*implied_price_rel + 0.3*sotp_price

wacc_grid = [wacc + dx for dx in (-0.01, -0.005, 0, 0.005, 0.01)]
g_grid    = [0.015, 0.020, 0.025, 0.030, 0.035]
# (grid computation as before)
```

Bull/Base/Bear: shift revenue growth ±300bps, EBIT margin ±200bps, WACC ∓100bps, g 3.0%/2.5%/1.5%.

### Banks

Blending and sensitivity are in **Step 4-Bank §4B-vi**. After running that step, proceed directly to Step 8.

---

## Step 8: Respond to the User

### Standard companies — output order

1. **Headline verdict** — blended fair value vs current, % upside/downside, most bullish/bearish method.
2. **Snapshot** — sector, industry, market cap, current price, 1Y return, LTM revenue growth.
3. **Method summary table** — method | implied price | weight | rationale.
4. **WACC Adjudication box** — formula_wacc | sector_band | peer_median | market_implied_ke | final_wacc | reason.
5. **DCF build** — growth path, margins, WACC, 5yr FCFF table, EV bridge.
6. **Peer comparison table** — P/E fwd, EV/Rev, EV/EBITDA, gross margin, rev growth; median row.
7. **SOTP** (if applicable).
8. **Sensitivity matrix** — WACC × g grid.
9. **Bull/Base/Bear scenarios**.
10. **Key risks** — 3-5 bullets on which assumptions move the answer most.

### Banks — output order

1. **Headline verdict** — blended implied price vs current, % upside/downside.
2. **Bank snapshot** — country, currency, market cap, current price, current P/BV, current P/TBV, LTM ROE, LTM NIM, NPL ratio, Tier 1 ratio.
3. **Method summary table** — GGM | Adjusted P/BV | DDM | Relative P/BV | weight | implied price.
4. **GGM workings** — ROE, g, ke inputs; justified P/BV; GGM implied price; current P/BV vs justified P/BV with interpretation.
5. **Adjusted P/BV scoring table** — one row per factor: factor | score | evidence | impact.
6. **DDM workings** (if applicable) — DPS, ke, g, implied price.
7. **Peer P/BV table** — peer | P/BV actual | GGM P/BV | ROE | gap; Gordon scatter interpretation.
8. **Banking financial model table** — §4B-v format, 6 columns (FY−2A through FY3F).
9. **ROE × ke sensitivity grid** — §4B-vi format.
10. **Bull/Base/Bear scenario table** — key assumption | ROE | P/BV target | implied price | upside%.
11. **Value trap assessment** — is current P/BV sustainable given ROE vs ke? Flag if ROE < ke.
12. **Key risks** — NPL trajectory, NIM pressure, capital adequacy, regulatory, concentration.

---

## Error handling

| Missing / edge case | Action |
|---|---|
| Bank: `ke <= g` in GGM | Cap `g = ke − 0.5%`, flag in output, note implied P/BV is very sensitive |
| Bank: ROE < 0 (loss-making) | GGM produces negative P/BV — skip GGM, use DDM + Relative only; flag as distressed |
| Bank: no dividend | DDM weight = 0%; redistribute 20% DDM weight to GGM (60%) and Adjusted P/BV (40%) |
| Bank: intangibles > 20% of book | Use P/TBV as primary relative multiple; note goodwill inflation |
| Bank: NPL > 10% | Flag as "elevated stress" in output; bear case P/BV must reflect provisioning haircut |
| Standard: yfinance beta = None | Use sector-default beta from `references/wacc_erp_rates.md` |
| Standard: negative LTM EBITDA | Skip EV/EBITDA; use EV/Revenue + DCF only |
| Standard: negative LTM EPS | Skip trailing P/E; use forward P/E if positive, else skip |
| Standard: `wacc <= g_terminal` | Stop; report cannot compute with these inputs |
| Standard: `pv_tv/ev > 0.85` | Flag; show both Gordon and exit-multiple TV |
| Standard: `wacc_formula` outside sector band | Run Step 4d adjudication; do not silently use out-of-range value |
| Peer data fetch fails | Drop that peer from median; note in output |
| S&P CIQ conflicts with filing | Report both figures; state definition mismatch explicitly |
| Figure more than 1 quarter stale | Label `[STALE]` in output |

### Caveats to include
- GGM is highly sensitive to the ROE−ke spread; a 100bps change in ke can move implied P/BV by 30–50%
- Adjusted P/BV scoring is analyst judgment — state evidence for every score, not opinion
- DCF is garbage-in/garbage-out; sensitivity matters more than a point estimate
- yfinance data is unofficial for banks — cross-check all ratios against primary filings
- Not financial advice

---

## Reference Files

- `references/dcf.md` — DCF methodology + industry-specific guidance
- `references/relative_valuation.md` — Peer selection, multiple adjustment rules, Rule of 40
- `references/sotp.md` — Sum-of-parts methodology, conglomerate discount detection
- `references/wacc_erp_rates.md` — Risk-free rates, ERP tables, sector WACC/ke benchmarks
