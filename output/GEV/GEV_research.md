# GE Vernova Inc. (NYSE: GEV) — Institutional Research Report

**Engine:** Alpha Global Equity Research
**Report date:** 2026-06-10
**Price reference:** $920.15 (yfinance `info.currentPrice`, 2026-06-09 snapshot; last clean daily close $933.85 on 2026-06-08)
**Sector / Industry:** Industrials / Specialty Industrial Machinery (yfinance `info.sector` / `info.industry`)

> Data sources: yfinance-data, earnings-recap, earnings-preview, estimate-analysis, company-valuation, stock-liquidity. Optional skills finance-sentiment (no `ADANOS_API_KEY`) and twitter-reader (opencli unavailable) could not run — see §15 and §17.

---

## Section 1 — Market Statistics Table

| Metric | Value | Source |
|---|---|---|
| Current price | $920.15 | yfinance `info.currentPrice` |
| Last clean close | $933.85 (2026-06-08) | yfinance history (1y, auto_adjust) |
| Market cap | $247.3B | yfinance `info.marketCap` |
| Enterprise value | $242.4B | yfinance `info.enterpriseValue` |
| Shares outstanding | 268.7M | yfinance `info.sharesOutstanding` |
| Float shares | 268.2M | yfinance `info.floatShares` |
| 52-week high | $1,181.95 | yfinance `info.fiftyTwoWeekHigh` |
| 52-week low | $464.00 | yfinance `info.fiftyTwoWeekLow` |
| **Drawdown from 52-W high** | **-22.1%** | computed (920.15 / 1181.95 − 1) |
| **YTD return** | **+37.6%** | computed (vs 678.64 close 2026-01-02) |
| **1-year return** | **+101.1%** | computed (vs 464.29 close 2025-06-10) |
| **ADTV (30-day, $)** | **~$2.55B** | computed (3mo ADV $2.45B) |
| **30-day realized vol (annualized)** | **~40%** | computed from daily log returns |
| **Short % of float** | **3.42%** | yfinance `info.shortPercentOfFloat` |
| **Short ratio (days-to-cover)** | **3.77** | yfinance `info.shortRatio` |
| **Insider ownership** | **0.10%** | yfinance `info.heldPercentInsiders` |
| Institutional ownership | 79.6% | yfinance `info.heldPercentInstitutions` |
| Trailing P/E (GAAP) | 26.9x | yfinance `info.trailingPE` |
| Forward P/E (non-GAAP) | 37.5x | yfinance `info.forwardPE` |
| EV/Revenue (TTM) | 6.16x | yfinance `info.enterpriseToRevenue` |
| EV/EBITDA (TTM) | 71.0x [see note] | yfinance `info.enterpriseToEbitda` |
| Beta | 1.045 | yfinance `info.beta` |
| Dividend yield | 0.22% | yfinance `info.dividendYield` (rate $2.00) |
| Analyst mean rating | 1.59 (Buy) | yfinance `info.recommendationMean` (33 analysts) |
| Mean analyst target | $1,216.13 | yfinance `info.targetMeanPrice` |
| Median analyst target | $1,250.00 | yfinance `info.targetMedianPrice` |

> **Note on EV/EBITDA 71x:** This uses yfinance's TTM EBITDA of $3.42B against a still-thin-margin base. GAAP trailing P/E of 26.9x is *understated in quality* because trailing GAAP net income ($4.88B FY2025) is inflated by large non-operating / tax items (see §8 and §14). On clean, forward earnings power the stock trades ~37.5x forward EPS.

---

## Section 2 — Company Overview & Business Model

GE Vernova is the power, grid, and electrification company spun off from General Electric on 2024-04-02 (the third and final GE spin, alongside GE Aerospace and GE HealthCare). It is one of the largest pure-play electrification franchises in the world, built around the thesis that the global electricity system must simultaneously decarbonize and expand to meet surging load growth from data centers/AI, electrification of transport and industry, and grid modernization. The company describes its purpose as helping "electrify and decarbonize the world."

GEV makes money across the full electricity value chain. The **Power** segment sells gas turbines, steam/nuclear equipment and services, and long-term service agreements (high-margin, recurring aftermarket). **Electrification** sells grid equipment — transformers, switchgear, high-voltage products, grid software and storage — into a capacity-constrained market with multi-year backlogs and rising pricing. **Wind** sells onshore and offshore turbines and services, a segment that has been loss-making and is being restructured. Roughly half of revenue is equipment (more cyclical, lumpy) and half is higher-margin services/aftermarket tied to a massive installed base (~25-30% of the world's electricity is generated on GEV technology, per company materials [ESTIMATED from disclosure]).

**Business model flywheel:**

```
   Record orders & backlog (grid + power)
              │
              ▼
   Pricing power on scarce equipment ──► Gross margin expansion (20.3% FY25 vs ~10% pre-spin)
              │                                      │
              ▼                                      ▼
   Higher-margin installed base ──────► Growing recurring service revenue
              │                                      │
              ▼                                      ▼
   Free cash flow generation ($3.7B FY25) ──► Buybacks + dividend + reinvestment
              │
              ▼
   Capacity expansion (new fab/capacity) ──► Capture more orders (back to top)
```

**Operating model:** Fab-heavy industrial OEM with a large, asset-light service annuity layered on top. Cyclical equipment cycle + counter-cyclical aftermarket. Long-cycle backlog business — revenue visibility is multi-year, but project execution risk (especially in Wind and large fixed-price contracts) is the structural offset.

---

## Section 3 — Business Segments

FY2025 (fiscal year ended 2025-12-31). Total revenue $38.07B (yfinance income_stmt). Segment splits are [ESTIMATED] from company segment disclosure and earnings commentary; yfinance does not expose segment detail.

| Segment | Revenue (FY25) | % of Total | YoY Growth | Est. Operating/EBITDA Margin |
|---|---|---|---|---|
| Power (gas, nuclear, steam, hydro) | ~$18.5B [ESTIMATED] | ~49% | ~mid-single-digit | ~12-14% EBITDA [ESTIMATED] |
| Electrification (grid, software, storage) | ~$9.4B [ESTIMATED] | ~25% | ~high-teens / +20% | ~14% EBITDA [ESTIMATED] |
| Wind (onshore + offshore) | ~$9.1B [ESTIMATED] | ~24% | ~flat/declining | ~0-2% EBITDA (near breakeven) [ESTIMATED] |
| Corporate / other / eliminations | ~$1.0B [ESTIMATED] | ~2% | n/a | negative (unallocated cost) |
| **Total** | **$38.07B** | **100%** | **+9.0%** (vs $34.94B FY24) | **GP margin 20.3%** (yfinance) |

> Group revenue growth FY25 vs FY24: $38.07B / $34.94B − 1 = **+9.0%** (yfinance income_stmt). The growth engine is Electrification; Wind is the drag.

---

## Section 4 — Geographic Revenue

[ESTIMATED] from company 10-K geographic disclosure; yfinance does not expose geography. Directionally, GEV is majority US/Americas with material EMEA and Asia exposure.

| Geography | Revenue (FY25) | % of Total |
|---|---|---|
| United States / Americas | ~$18-19B [ESTIMATED] | ~48-50% |
| Europe (EMEA) | ~$10-11B [ESTIMATED] | ~28% |
| Asia / Pacific | ~$7-8B [ESTIMATED] | ~19% |
| Other | ~$1-2B [ESTIMATED] | ~4% |

> Not available with precision — data gap (see §17). US exposure is rising fastest given domestic data-center / grid capex.

---

## Section 5 — Top Customers & Concentration

No single customer exceeds the 10% SEC disclosure threshold based on available disclosure — GEV's revenue is diversified across utilities, independent power producers, hyperscalers (indirectly), and governments. The table below is [ESTIMATED] from earnings commentary and industry channel knowledge.

| Customer type | Est. Revenue exposure | Products | Disclosure basis |
|---|---|---|---|
| Regulated/IOU utilities | Largest block (~40%+) [ESTIMATED] | Grid equipment, gas turbines, service | Earnings commentary |
| Independent power producers / IPPs | Material [ESTIMATED] | Gas turbines, LTSAs | Earnings commentary |
| Hyperscalers / data center developers | Growing fast (indirect + direct) [ESTIMATED] | Gas turbines, grid, on-site power | Mgmt commentary on AI demand |
| Governments / national grids | Material [ESTIMATED] | Grid, nuclear, offshore wind | Earnings commentary |

**Concentration risk:** Low single-customer concentration (no >10% disclosed). The real concentration is *thematic* — exposure to the data-center/AI power buildout is now a large embedded bet (see §13). Customer base is investment-grade and backlog-protected.

---

## Section 6 — Management & Acquisition Track Record

| Name | Role | Tenure | Background |
|---|---|---|---|
| Scott Strazik | CEO | Since spin (2024); led GE Vernova predecessor businesses | Long-time GE Power/energy executive |
| Ken Parks | CFO | Since spin (2024) | Veteran industrial CFO |
| Steve Angel | Chairman | Since spin | Former Linde CEO; on board (insider buy 2026-05-14, 1,350 sh) |

> Officer Victor Abate (yfinance insider_transactions) acquired 4,819 shares on 2026-06-01 (~$4.57M); Matthew Potvin 2,333 shares 2026-05-14 (~$2.47M); multiple directors received 495-share grants 2026-05-14. See §15.

**Acquisitions:** As a 2024 spin-off, GEV's M&A history is short. Capital allocation to date has emphasized organic capacity expansion, debt-light balance sheet, buybacks ($3.32B repurchased FY25 per yfinance cashflow), and an initiated/growing dividend ($275M paid FY25). No transformative acquisition has been completed post-spin.

**Capital allocation philosophy (one sentence):** Self-fund organic capacity growth in grid/power, return excess cash via buyback + growing dividend, and preserve a net-cash balance sheet to absorb long-cycle project risk.

---

## Section 7 — Historical Financials

Source: yfinance income_stmt (annual), cashflow (annual), balance_sheet (annual). FY2021 is pre-spin / not populated in yfinance (NaN). FY2025 ended 2025-12-31. FY+1E/FY+2E from estimate consensus (yfinance earnings_estimate / revenue_estimate).

| ($M unless noted) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026E | FY2027E |
|---|---|---|---|---|---|---|
| Revenue | 29,654 | 33,239 | 34,935 | 38,068 | 45,484 | 51,891 |
| YoY growth | n/a | +12.1% | +5.1% | +9.0% | +19.5% | +14.1% |
| Gross margin | 11.7% | 14.5% | 17.4% | 19.8% | — | — |
| Operating income | (2,881) | (923) | 471 | 1,389 | — | — |
| Operating margin | (9.7%) | (2.8%) | 1.3% | 3.6% | — | — |
| EBITDA (reported) | (526) | 932 | 1,643 | 2,242 | — | — |
| GAAP Net Income | (2,736) | (438) | 1,552 | 4,884 ⚠ | — | — |
| Free Cash Flow | (627) | 442 | 1,700 | 3,710 | ~4.0-4.5B [EST] | — |
| FCF margin | (2.1%) | 1.3% | 4.9% | 9.7% | ~9-10% [EST] | — |
| GAAP Diluted EPS | (10) | (2) | 6 | 18 ⚠ | ~31.0 ⚠ | ~24.3 |
| non-GAAP EPS (est.) | n/a | n/a | n/a | n/a | ~$13-15 [EST clean] | ~$24.3 |
| Capex | (513) | (744) | (883) | (1,277) | — | — |
| Total Debt | 1,144 | 1,157 | 1,043 | 1,172 | — | — |
| Cash & equivalents | 2,067 | 1,551 | 8,205 | 8,848 | — | — |
| Net cash (cash − debt) | +923 | +394 | +7,162 | +7,676 | — | — |
| Net Debt/EBITDA | n/m | n/m | net cash | net cash | net cash | net cash |

> ⚠ **Critical flag:** FY2025 GAAP net income of $4.88B and EPS ~$18 are *inflated by large non-operating/tax items* (operating income was only $1.39B). The FY2026E consensus EPS of ~$31 (yfinance `0y` estimate) carries the same distortion — it was revised up from ~$14.8 about 60 days ago (see §8/§14). FY2027E (~$24.3, the `+1y` estimate) is the cleanest proxy for underlying earnings power. Use clean EPS, not GAAP, for valuation.

---

## Section 8 — Recent Results

Last two reported quarters (yfinance quarterly_income_stmt + earnings_history):

| Metric | Q4 2025 (2025-12-31) | Q1 2026 (2026-03-31) |
|---|---|---|
| Revenue | $10,956M | $9,338M |
| Gross profit / margin | $2,322M / 21.2% | $1,781M / 19.1% |
| Operating income / margin | $602M / 5.5% | $179M / 1.9% |
| GAAP Net income | $3,664M ⚠ | $4,745M ⚠ |
| GAAP Diluted EPS | $13.39 ⚠ | $17.44 ⚠ |
| EPS estimate (consensus) | ~$3 | ~$2 |

> ⚠ Both quarters' GAAP net income vastly exceeds operating income ($602M and $179M respectively) — driven by large non-operating gains / tax items (deferred tax valuation allowance release and/or non-operating items). The "beats" below reflect GAAP EPS clearing a low consensus bar, **not** clean operating outperformance. This must be disclosed; do not read the EPS surprise as operating quality.

**Beat history (yfinance earnings_history, EPS surprise):**

| Quarter | EPS Est | EPS Actual | Surprise |
|---|---|---|---|
| 2025-06-30 | ~$2 | ~$2 | ~0% (in line) |
| 2025-09-30 | ~$2 | ~$2 | ~0% (in line) |
| 2025-12-31 | ~$3 | ~$13 | very large (one-time-driven) ⚠ |
| 2026-03-31 | ~$2 | ~$17 | very large (one-time-driven) ⚠ |

**Guidance cadence:** Management provides annual revenue, adjusted EBITDA margin, and FCF guidance, updated quarterly, plus multi-year (2028) framework targets. Next print: **2026-07-22** (yfinance calendar).

---

## Section 9 — Competitive Landscape

| Market (TAM) | TAM estimate | GEV position | Time horizon |
|---|---|---|---|
| Global grid/electrification equipment | $200B+ annual, growing [ESTIMATED] | Top-3 global (vs Siemens Energy, Hitachi, ABB) | 2025-2035 |
| Gas turbine power generation + service | $50-70B [ESTIMATED] | #1/#2 globally (vs Siemens Energy, Mitsubishi) | 2025-2035 |
| Onshore/offshore wind | $80-100B [ESTIMATED], cyclical | Top-3 but sub-scale economics | 2025-2030 |
| Data-center / AI on-site power | Emerging, fast-growing [ESTIMATED] | Strong (gas turbine lead times = moat) | 2025-2030 |

| Peer | Market cap | LTM revenue | EV/Revenue | Key overlap |
|---|---|---|---|---|
| Siemens Energy (ENR.DE) | large-cap | ~€38B | 2.99x | Gas turbines, grid, wind (full overlap) |
| Schneider Electric (SU.PA) | mega-cap | ~€38B | 4.08x | Electrification / grid |
| Eaton (ETN) | mega-cap | ~$26B | 6.21x | Electrical / data-center power |
| Vertiv (VRT) | large-cap | ~$9B | 10.33x | Data-center power & thermal |
| Hitachi (grid via Hitachi Energy) | mega-cap | large | n/m | Grid/HVDC (direct overlap) |
| ABB (ABBNY) | mega-cap | ~$33B | 21.35x [data anomaly] | Electrification |
| Mitsubishi Heavy (MHVYF) | large-cap | large | n/m [data anomaly] | Gas turbines, power |

> Source: yfinance `info.enterpriseToRevenue` per peer. ABB / MHVYF EV/Rev figures look anomalous in yfinance and were excluded from medians.

---

## Section 10 — Peer Valuation Comparison

Source: yfinance `info` per ticker (forwardPE, enterpriseToRevenue, enterpriseToEbitda). GEV row uses forward (clean) basis.

| Company | Fwd P/E | EV/EBITDA | EV/Rev | Rev Growth (NTM) | FCF Margin | Rating |
|---|---|---|---|---|---|---|
| **GEV (subject)** | **37.5x** | **71x (TTM, low-margin base)** | **6.2x** | **~+19%** | **~9.7%** | Buy (1.59) |
| Siemens Energy (ENR.DE) | 24.6x | 32.7x | 3.0x | ~mid-teens | low | — |
| Schneider (SU.PA) | 22.8x | 20.6x | 4.1x | ~mid-single | mid-teens | — |
| Eaton (ETN) | 25.6x | 27.9x | 6.2x | ~+8% | high | — |
| Vertiv (VRT) | 32.8x | 47.0x | 10.3x | ~+15-20% | mid | — |
| Honeywell (HON) | 18.8x | 19.1x | 4.3x | ~low-single | high | — |
| ABB (ABBNY) | 29.3x | (anomaly) | (anomaly) | ~mid-single | mid | — |
| **Peer median** | **25.6x** | **24.3x** | **4.2x** | — | — | — |

**What the spread implies:** GEV trades at a **premium to the peer median on every multiple** — ~47% premium on forward P/E (37.5x vs 25.6x) and ~48% premium on EV/Revenue (6.2x vs 4.2x). The premium is *partially* justified by faster NTM revenue growth (~+19% vs peers ~mid-single-to-mid-teens) and best-in-class thematic exposure (grid + AI power). But it is a rich premium that prices the GEV margin-expansion story as near-certain. Even the closest growth comps (VRT 32.8x, ETN 25.6x) sit below GEV's forward multiple.

---

## Section 11 — Valuation

> **Headline:** Every cash-flow-based method (DCF, SOTP) lands materially below the current $920 price; only forward-earnings multiple methods approach it, and only by assuming GEV sustains/extends a margin-expansion supercycle. The stock is priced for ~2029-2030 earnings power *today*. Blended fair value ~**$470**, range **$333-$622**, implying material downside vs the $920 quote on fundamentals. This is the central, uncomfortable finding of the report.

### Method 1: DCF — Three Scenarios

**WACC adjudication box:**

| Item | Value |
|---|---|
| Formula WACC (CAPM, all-equity) | rf 4.4% + β 1.045 × ERP 5.0% = **9.62%** |
| Capital structure | Net-cash (~$7.7B); debt negligible → WACC ≈ ke |
| Sector industrial sanity band | 8.5% – 10.5% |
| Adjudicated base WACC | **9.0%** (inside band; bull 8.4%, bear 9.8%) |
| Reason | Net-cash co, β ~1.0; formula sits inside band, use formula-anchored 9.0% base |

7-year explicit horizon to capture the margin ramp (EBIT margin ramping from ~5% toward 12.5% base / 15.5% bull), then terminal growth.

| Scenario | WACC | Terminal g | Path (rev growth / EBIT margin) | Implied price |
|---|---|---|---|---|
| Bear | 9.8% | 2.5% | growth fades 12%→3%, margin stalls ~8% | **~$174** |
| Base | 9.0% | 3.5% | growth fades 17%→6%, margin ramps to 12.5% | **~$417** (TV/EV 77%) |
| Bull | 8.4% | 4.0% | growth 20%→7%, margin ramps to 15.5% | **~$717** |

**Probability-weighted DCF** (30% bear / 45% base / 25% bull) = **~$419**.

### Method 2: Relative (Peer Multiples)

Applied to clean forward earnings (not GAAP). FY2027E clean EPS ~$24.31 (yfinance `+1y`).

| Approach | Multiple | Base | Implied price |
|---|---|---|---|
| Peer-median fwd P/E | 25.6x | FY27 EPS $24.31 | ~$622 |
| Growth-premium fwd P/E | 31.0x | FY27 EPS $24.31 | ~$754 |
| EV/EBITDA | 24.3x | FY27 underlying EBITDA ~$5.2B | ~$498 |
| **Relative blended (median)** | — | — | **~$622** |

> Relative is the *most generous* method because it leans on the premium multiple already in the market and a forward earnings base. Even so, the peer-median P/E approach (~$622) and the EV/EBITDA approach (~$498) sit below the $920 price; only a 31x growth-premium multiple on FY27 earnings ($754) gets close.

### Method 3: SOTP

2027E segment EBITDA at pure-play multiples (Electrification gets a grid/data-center premium; Wind a distressed multiple).

| Segment | 2027E Rev | EBITDA margin | EBITDA | Multiple | EV |
|---|---|---|---|---|---|
| Power | $20.5B | 14% | $2.87B | 15x | $43.1B |
| Electrification | $11.5B | 16% | $1.84B | 20x | $36.8B |
| Wind | $8.5B | 5% | $0.42B | 9x | $3.8B |
| Corporate / unallocated | — | — | — | — | ($2.0B) |
| **Total EV** | — | — | — | — | **$81.7B** |
| + Net cash | — | — | — | — | +$7.7B |
| **Equity value** | — | — | — | — | **$89.4B** |
| **Implied price** | — | — | — | — | **~$333** |

> Conglomerate/narrative gap: SOTP at forward 2027 economics = ~$333 vs market $920 → the market values GEV at roughly **2.8x its forward sum-of-parts**. This is the cleanest statement of how much future the stock already discounts.

### Probability-Weighted Synthesis

| Method | Weight | Implied price | Weighted contribution |
|---|---|---|---|
| DCF (prob-weighted) | 40% | $419 | $168 |
| Relative (blended) | 35% | $622 | $218 |
| SOTP (2027E) | 25% | $333 | $83 |
| **Blended fair value** | **100%** | — | **~$469** |

**Blended fair value ~$470 vs current $920 → ~-49% (downside on fundamentals).**
**Fair value range: $333 (SOTP) – $622 (relative); bull-case ceiling ~$717-$754.**

> Honest caveat: GEV has repeatedly traded *above* intrinsic estimates because the market is discounting a multi-year electrification/AI-power supercycle and continuous upward estimate revisions. Fundamentals say expensive; momentum and Street targets (mean $1,216) say otherwise. The gap between this model (~$470) and the Street mean ($1,216) is itself the key debate (see §14, §16).

---

## Section 12 — Bull Case (10 Catalysts)

**Thesis:** GEV is the highest-quality pure-play on a structural, decade-long electricity supercycle (AI/data-center load + grid replacement + electrification), with pricing power, a net-cash balance sheet, and a margin-expansion runway that consensus keeps under-modeling.

1. **Data-center / AI power demand** — US electricity load is inflecting up for the first time in two decades; gas-turbine lead times now stretch multiple years, giving GEV scarcity-driven pricing power. (Mgmt commentary; revenue accel to +19% NTM, yfinance revenue_estimate.)
2. **Grid capex supercycle** — Electrification is the fastest-growing segment (~+20% [ESTIMATED]) with multi-year backlog and rising transformer/switchgear pricing amid global shortages.
3. **Margin expansion runway** — Gross margin rose from 11.7% (FY22) to 19.8% (FY25); operating margin turned positive (3.6%) and management guides toward low-teens adjusted EBITDA margin by 2028. (yfinance income_stmt.)
4. **FCF inflection** — FCF went from −$627M (FY22) to +$3.71B (FY25), a 9.7% FCF margin, funding buybacks and dividend. (yfinance cashflow.)
5. **Net-cash balance sheet** — ~$7.7B net cash (cash $8.85B vs debt $1.17B) gives optionality for capacity, buybacks, and downturn resilience. (yfinance balance_sheet.)
6. **Capital return ramp** — $3.32B repurchased FY25 + $275M dividends initiated; room to grow both given FCF trajectory. (yfinance cashflow.)
7. **Positive estimate revision momentum** — FY27 (`+1y`) EPS revised up from $22.49 (90d ago) to $24.31, with 20 up-revisions vs 3 down in 30 days. (yfinance eps_trend / eps_revisions.)
8. **Backlog visibility** — Long-cycle orders provide multi-year revenue visibility, de-risking the top line vs typical industrial cyclicals.
9. **Nuclear / SMR optionality** — GEV's nuclear (BWRX-300 SMR) and existing nuclear services give it leverage to the clean-baseload narrative that pairs naturally with data-center demand. (Mgmt commentary.)
10. **Multiple re-rating + Street support** — 29 of 37 ratings Buy/Strong Buy, 0 sells (yfinance recommendations); mean target $1,216 (~+32% from spot) anchors the bull and reflects continued re-rating willingness.

---

## Section 13 — Bear Case (10 Thesis-Breakers)

**Thesis (independent of the bull):** GEV is priced at ~2.8x forward SOTP and ~37.5x forward EPS for a margin-expansion-and-supercycle outcome that is largely consensus; any of demand normalization, project charges, Wind losses, or multiple compression takes the stock back toward intrinsic value ($333-$622).

1. **Valuation breaks first.** On DCF (~$419) and SOTP (~$333), fair value is roughly half the $920 price. The stock discounts ~2029-2030 earnings power today; even a flawless operational outcome leaves limited margin of safety. *Falsifier: clean forward EPS sustainably exceeds ~$30 with high-teens margins by 2027.*
2. **GAAP earnings quality is poor.** FY25 GAAP net income ($4.88B) and FY26E consensus EPS (~$31) are inflated by non-operating/tax items; operating income is a fraction of net income (Q1'26: $179M op income vs $4.75B net income). *Falsifier: operating income converges toward GAAP net income.*
3. **AI-power demand is partly a narrative.** A large share of the bull case rests on data-center load that could disappoint if hyperscaler capex normalizes, efficiency improves, or projects slip. *Falsifier: signed multi-year gas-turbine/grid orders from data centers keep accelerating.*
4. **Wind is a structural value-destroyer.** Onshore/offshore wind remains near breakeven with project-charge history; offshore in particular has destroyed industry capital. *Falsifier: Wind reaches sustained mid-single-digit EBITDA margin.*
5. **Long-cycle fixed-price project risk.** Large equipment contracts carry execution and warranty risk; a single large charge can erase a quarter's operating income (op income is only $179M-$602M/qtr). *Falsifier: multiple clean quarters with no project charges.*
6. **Margin ramp may stall.** The base case needs EBIT margin to roughly triple from ~5% to ~12.5%; supply-chain inflation, mix, or competition could cap it. *Falsifier: adjusted EBITDA margin hits ~10%+ on schedule.*
7. **Premium multiple compression.** GEV trades ~47% above peer-median forward P/E; any growth wobble re-rates it toward peers (25.6x → ~$622 or lower). *Falsifier: NTM growth stays >15% and beats.*
8. **Drawdown already underway.** Down 22.1% from the 52-week high ($1,182 → $920) — the market is already questioning the price; 40% realized vol signals fragility. *Falsifier: stock reclaims prior high on fundamentals.*
9. **Estimate distortion masks deceleration.** The FY26 EPS jump to ~$31 is one-time-driven; the *underlying* FY27 number (~$24.3) is actually *lower* than the headline FY26 figure, i.e., clean EPS is not compounding the way the headline implies. *Falsifier: clean EPS grows >15% per year through 2027.*
10. **Crowding / momentum unwind.** 79.6% institutional ownership and a beloved thematic story mean positioning is crowded; a macro/AI-capex scare could force concentrated selling into ~$2.5B/day liquidity. *Falsifier: ownership broadens and the stock absorbs macro shocks.*

**Structural risk register:**

| Risk category | Specific risk | Probability | Impact |
|---|---|---|---|
| Valuation | Multiple compression to peer median | High | High |
| Demand | AI/data-center power demand normalizes | Medium | High |
| Operational | Large fixed-price project charge | Medium | Medium |
| Segment | Wind losses persist/widen | Medium-High | Medium |
| Earnings quality | GAAP/non-GAAP divergence persists | High (already true) | Medium |
| Positioning | Crowded thematic unwind | Medium | High |

---

## Section 14 — Delta Audit

| Claim | Raw source value | Computation | Status |
|---|---|---|---|
| Market cap $247.3B | yfinance `info.marketCap` 247,262,707,712 | direct | ✓ Verified |
| Price $920.15 | yfinance `info.currentPrice` | direct (note: last clean close $933.85) | ⚠ Snapshot vs close mismatch |
| 1Y return +101.1% | history 464.29 → ~933.85 | (933.85/464.29−1) | ✓ Verified |
| YTD return +37.6% | history 678.64 → ~933.85 | computed | ✓ Verified |
| Drawdown −22.1% | 1181.95 high vs 920.15 | (920.15/1181.95−1) | ✓ Verified |
| FY25 revenue $38.07B | yfinance income_stmt | direct | ✓ Verified |
| FY25 gross margin 19.8% | 7,535 / 38,068 | computed | ✓ Verified (info shows 20.3% TTM — period mismatch) |
| FY25 operating income $1.39B | yfinance income_stmt | direct | ✓ Verified |
| FY25 GAAP net income $4.88B | yfinance income_stmt | direct — **but >3.5x operating income** | ⚠ Inflated by non-operating/tax items |
| FY25 FCF $3.71B | yfinance cashflow Free Cash Flow | direct | ✓ Verified |
| Net cash $7.68B | cash 8,848 − debt 1,172 | computed | ✓ Verified |
| FY26E EPS ~$31 | yfinance earnings_estimate `0y` 30.996 | direct — **was ~$14.8 90d ago** | ⚠ One-time-driven; not clean run-rate |
| FY27E EPS ~$24.3 | yfinance earnings_estimate `+1y` 24.31 | direct | ✓ Verified (cleanest proxy) |
| Forward P/E 37.5x | yfinance `info.forwardPE` | direct | ✓ Verified |
| Short % float 3.42% | yfinance `info.shortPercentOfFloat` | direct | ✓ Verified |
| Mean target $1,216 | yfinance `info.targetMeanPrice` | direct | ✓ Verified |
| Blended fair value ~$470 | model | 0.40×419 + 0.35×622 + 0.25×333 | ✓ Reproduces |
| Buyback $3.32B FY25 | yfinance cashflow Repurchase Of Capital Stock | direct | ✓ Verified |

**Required flags:**
- **GAAP/non-GAAP discrepancy (material):** FY25 and FY26E GAAP EPS are inflated by large non-operating/tax items. Operating income ($1.39B FY25; $179M Q1'26) is far below GAAP net income. Valuation uses clean FY27 EPS (~$24.3) to avoid this distortion. **This is the single most important reconciliation note in the report.**
- **Estimate spread width:** FY27 (`+1y`) EPS range $16.39–$29.74 on $24.31 mean = ±27% — very wide, signaling high uncertainty on the margin ramp. Revenue spread is tighter (±8% FY26).
- **Price snapshot:** `info.currentPrice` (920.15) is below the last clean daily close (933.85); intraday/snapshot timing. Returns computed off clean closes.
- **Segment/geography data:** [ESTIMATED] — yfinance does not expose segment or geographic detail; figures derived from disclosure/commentary (data gap §17).
- **Model vs Street gap:** Blended fair value ~$470 vs Street mean $1,216 — a very large divergence. This model weights cash-flow/SOTP methods that the market is currently overriding with a supercycle narrative.

**VERDICT: PASS WITH NOTES.** Core market and financial figures reproduce cleanly from yfinance primary fields. The two material caveats — (1) GAAP earnings inflated by one-time items, and (2) a large model-vs-market fair-value gap driven by methodology weighting — are disclosed and do not invalidate the audit, but the user must read the valuation as "expensive on fundamentals, supported by narrative/momentum."

---

## Section 15 — Sentiment & Flow

**Short interest narrative:** Short % of float 3.42% with a short ratio (days-to-cover) of 3.77 (yfinance). This is **low** — not a crowded short, no squeeze setup. The market is positioned long, not short; bears are expressing the view via options/underweights, not heavy borrow. Low short interest also means limited short-covering support on the way up.

**Insider transactions (yfinance insider_transactions, last significant):**

| Name | Role | Date | Type | Shares | Value |
|---|---|---|---|---|---|
| Abate Victor | Officer | 2026-06-01 | Acquire | 4,819 | ~$4.57M |
| Potvin Matthew Joseph | Officer | 2026-05-14 | Acquire | 2,333 | ~$2.47M |
| Angel Stephen F | Director (Chair) | 2026-05-14 | Acquire (grant) | 1,350 | — |
| Malave/Harris/Reynolds/Donald/Hund-Mejean | Directors | 2026-05-14 | Acquire (grant) | 495 each | — |

> Recent insider activity is net acquisition (officer open-market-style buys + director grants). No large insider selling in the available window — mildly constructive signal. Insider ownership is only 0.10% (yfinance), typical for a spin-off with no founder block.

**Top institutional holders (yfinance institutional_holders, as of 2026-03-31):**

| Holder | % Held | Shares | Value |
|---|---|---|---|
| BlackRock | 7.71% | 20.7M | ~$19.1B |
| FMR (Fidelity) | 6.82% | 18.3M | ~$16.9B |
| Vanguard Capital Mgmt | 6.52% | 17.5M | ~$16.1B |
| State Street | 4.24% | 11.4M | ~$10.5B |
| JPMorgan | 2.51% | 6.8M | ~$6.2B |

> Institutional ownership 79.6% — heavily owned by index/large managers (BlackRock, Vanguard, State Street ≈ passive). Crowded but stable base.

**Social / cross-source sentiment:** **DATA GAP** — finance-sentiment (Adanos) requires `ADANOS_API_KEY` (not set) and twitter-reader requires opencli (unavailable). Qualitative assessment from public discourse: GEV is a consensus-long, widely-loved thematic name (AI power + grid); sentiment skews strongly bullish, which is itself a contrarian caution flag given the valuation. No primary sentiment data could be retrieved.

---

## Section 16 — Synthesis & Recommendation

**Where bull and bear agree:**
1. GEV is a genuinely high-quality, structurally-advantaged electrification franchise with real pricing power and a net-cash balance sheet.
2. Revenue is accelerating (~+19% NTM) and margins/FCF have inflected sharply since the 2024 spin.
3. Reported GAAP earnings are *not* clean — both sides use forward/underlying numbers.
4. The stock prices in a multi-year supercycle; the debate is entirely about *how much* future is already in the price.
5. Execution/project risk and Wind remain the operational soft spots.

**Probability-weighted 12-month outcome:**

| Scenario | Probability | 12-month target | Weighted contribution |
|---|---|---|---|
| Bear (multiple compresses toward peers / demand wobble) | 30% | $560 | $168 |
| Base (narrative holds, fundamentals slowly catch up) | 45% | $850 | $383 |
| Bull (supercycle re-accelerates, beats + raises) | 25% | $1,200 | $300 |
| **Expected value** | **100%** | — | **~$851** |

> Note the tension: intrinsic blended fair value (~$470) is well below the *market-anchored* 12-month EV (~$851). The 12-month targets above are deliberately market-/momentum-anchored (they incorporate the Street's willingness to keep paying a premium and the mean target of $1,216), whereas the §11 fair value is the cash-flow/SOTP intrinsic estimate. The honest read: **fundamentally expensive, but a powerful narrative and revision cycle can sustain the premium for longer than valuation alone would suggest.**

**Rating: MARKET WEIGHT** (12-month target $850; horizon 12 months).
Rationale: The business quality and revision momentum justify holding/owning a benchmark-weight position, but the ~2x premium to intrinsic fair value (~$470) and the GAAP earnings-quality flags preclude an Overweight at $920. This is not a fundamentals-driven Buy at this price; it is a quality compounder that has run ahead of its cash flows. An Underweight would be too aggressive against +19% growth, a net-cash balance sheet, and unanimous Street support.

**Entry strategy:** Initiate at half benchmark weight near current levels only for momentum/thematic mandates. For valuation-disciplined mandates, wait for a pullback into the **$700-$760 zone** (prior YTD base / closer to the relative-valuation floor) to add. Add-on trigger: a clean quarter showing operating income converging toward net income *and* adjusted EBITDA margin tracking to the ~10% milestone.

**Stop-loss / thesis invalidation:** Below **$640** on a closing basis (decisively under the relative-valuation floor and prior support) the thematic premium is breaking — exit. Thesis invalidation: a large project charge, a Wind blow-up, or evidence that data-center power orders are decelerating.

**Hedge:** Pair-trade vs a lower-multiple grid/electrification peer (long-quality / short-rich), or buy out-of-the-money puts funded by call overwrites (collar) given 40% realized vol makes options expensive but protection cheap relative to drawdown risk. Sector hedge: short XLI or a clean-energy/utility ETF basket against the position.

**Position sizing:** Benchmark weight (no overweight). Cap at ~3-4% of an industrials/thematic sleeve. Correlation consideration: GEV is highly correlated with the AI-capex/data-center complex (NVDA, VRT, ETN, utilities) — size it as part of a single "AI-power" risk bucket, not as a diversifier.

**Key catalysts to watch (with dates):**
- **2026-07-22** — Q2 2026 earnings (consensus rev ~$10.7B, EPS ~$2.96): watch *clean* operating margin and any guidance raise.
- **2026-06-16** — ex-dividend date.
- Ongoing — gas-turbine/grid order announcements tied to data-center deals (the single most important real-time signal).
- 2028 framework targets — any update to the adjusted EBITDA margin / FCF roadmap.

---

## Section 17 — Data Gaps

| Item | Gap type | Impact |
|---|---|---|
| Segment revenue/margin (Power, Wind, Electrification) | [ESTIMATED] — not exposed by yfinance; derived from disclosure/commentary | High (drives SOTP) |
| Geographic revenue split | [ESTIMATED] — not exposed by yfinance | Medium |
| Top customer detail | [ESTIMATED] — no >10% customer disclosed | Low |
| Cross-source social sentiment | Unavailable — `ADANOS_API_KEY` not set (finance-sentiment) | Medium |
| Twitter / bear-side commentary | Unavailable — opencli not installed (twitter-reader) | Medium |
| non-GAAP / adjusted EPS for FY25/FY26 | [ESTIMATED] — yfinance gives GAAP + consensus only; clean EPS inferred | High (earnings quality) |
| FY2021 financials | Not populated (pre-spin) in yfinance | Low |
| Adjusted EBITDA (management-defined) | yfinance EBITDA differs from mgmt adjusted; used reported + estimates | Medium |
| FY2026E/FY2027E margins, capex | Consensus revenue/EPS only; segment-level forward margins [ESTIMATED] | Medium |

---

*Research/educational output. Not financial advice. Data primarily from yfinance (unofficial Yahoo Finance), supplemented by consensus estimates. Figures labeled [ESTIMATED] are not from primary filings. GAAP figures flagged ⚠ are distorted by non-operating items.*
