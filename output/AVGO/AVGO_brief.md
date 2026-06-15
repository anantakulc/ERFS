# AVGO — Institutional Investment Brief
**Date:** 2026-06-15 | **Price:** $382.07 | **Rating:** MARKET WEIGHT | **Our Target:** $350 (-8.4%) | **Horizon:** 12-18 months
**Prob-Weighted Expected Value:** $404 (+5.7%) | **Street consensus:** $522 (reference only)

---

## Valuation Summary

| Method | Weight | Implied Price | Note |
|---|---|---|---|
| DCF Prob-Weighted (35% bull $324 / 45% base $289 / 20% bear $258) | 40% | $295 | WACC 10.21% (Blume 1.290, ERP 4.6%) |
| Relative NTM blended (P/E $387 / EV/EBITDA $303 / EV/Rev $315) | 40% | $335 | Peer median 20.0x Fwd P/E |
| SOTP (semi 22x + software 25x EV/EBITDA on FY2025 bases) | 20% | $189 | Conservative; FY2025 EBITDA |
| Blended Intrinsic Value (BIV) | 100% | $290 | -- |
| FY+2E P/E Cross-check | -- | $387 | 20.0x x $19.35 FY+2E EPS |
| Adopted Target (analyst override) | -- | $350 | 40% BIV + 60% P/E; semi convention |

WACC: RF 4.49% + Beta_Blume 1.290 x ERP 4.6% = ke 10.42%. Formula WACC 10.21% (sector 10-12%; peer median 11.49%; GAP -128bps, no switch). Market-implied ke 7.56% (AI optionality premium = 262bps gap vs adopted WACC). BIV vs P/E divergence 33.5% -- analyst override applied.

---

## DCF Sensitivity -- WACC x Terminal g

| WACC / g | g=1.5% | g=2.0% | g=2.5%* | g=3.0% | g=3.5% |
|---|---|---|---|---|---|
| 8.5% | $320 | $328 | $338 | $350 | $365 |
| 9.5% | $294 | $300 | $307 | $315 | $325 |
| 10.2%* | $278 | $283 | $289 | $296 | $303 |
| 11.5% | $253 | $257 | $261 | $266 | $271 |
| 12.5% | $237 | $240 | $244 | $247 | $251 |

---

## Top 3 Bull Catalysts

1. Network fabric moat intact despite compute internalization -- Google builds TPU compute in-house but Broadcom retains Tomahawk/Jericho switching. Cluster scale growth = more switching ASICs per cluster. FY2026E rev +66%; EPS revised +10.4% in 90d.
2. VMware annuity + deleveraging -- Net Debt/EBITDA 1.1x and falling. Post-delever FCF redirects to buybacks ($0.85 EPS accretion per $10B at $382). GAAP amortisation cliff post-FY2027 narrows GAAP/non-GAAP gap.
3. Highest revenue growth in peer set at below-median P/E -- FY2026E +66% at 19.7x Fwd P/E vs MRVL 45.3x (+28%), AMD 39.0x (+38%). -22.8% from 52W high on stronger fundamentals. New XPU win (4th hyperscaler) triggers consensus revision to $25+ NTM EPS.

---

## Bear Case

At 63.7x GAAP P/E and 44.3x EV/EBITDA, AVGO has zero tolerance for execution failures. The ASIC moat is migrating: Google has already removed AVGO from the compute die (TPU v6); the network fabric layer (Tomahawk/Jericho) is the 2027-2029 re-tender risk, where Marvell is qualifying as an alternate. If one hyperscaler defects from the fabric layer, FY2027E EPS cuts 25-40% and the stock trades $240-290 at 20x P/E. Apple wireless ($8-10B/yr) is a confirmed multi-year exit; iPhone 17 cycle (September 2026) is the first observable data point. VMware ARR conversion is tracking below initial guidance. The -17% single-session drop on May 29 (on an EPS beat) demonstrates how crowded positioning amplifies any negative catalyst.

---

## Key Risks

- ASIC moat migration: Marvell qualifying as Google fabric alternate in 2026 design cycle; $2-4B/yr revenue at risk by FY2028E
- Apple wireless exit: $8-10B/yr at risk; iPhone 17 cycle (September 2026) is key data point
- EV/EBITDA de-rating: 44.3x -> 25.2x peer median (no earnings change) implies $214/share (-44%)

---

## Entry & Position Management

Current stance: Market Weight. $382 is 9% above our $350 target -- insufficient risk/reward for overweight.
Add trigger: Pullback to $320-340 (DCF base convergence zone).
Full entry: Post-Q3 FY2026 confirmation at $330-360.
Stop-loss: $270 (XPU defection confirmed, VMware churn >15%, or AI capex cut >15%).
Hedge: Long QCOM puts + long VIX calls.
Position size: 2-3% market weight; 4-6% post-Q3 confirmed beat + new XPU win.
Key catalyst: Q3 FY2026 earnings, September 2026 ($29.4B revenue guide).

---

## Delta Verdict

PASS WITH NOTES -- All primary figures verified from yfinance 2026-06-15. Three flags:
1. GAAP/non-GAAP delta $13.35/share -- P/E tables use non-GAAP convention (disclosed)
2. Hyperscaler XPU revenue by customer [UNVERIFIED] -- not in SEC filings
3. SOTP segment EBITDA [ESTIMATED] -- not disclosed by company

---

| Metric | Value | Source |
|---|---|---|
| Revenue TTM | $75.5B | yfinance totalRevenue |
| EBITDA TTM | $42.1B | yfinance ebitda |
| FCF TTM | $27.2B (36% margin) | yfinance freeCashflow |
| Net Debt | $45.3B (1.1x EBITDA) | derived from balance_sheet |
| Capex % Revenue | 1.0% | yfinance cashflow |
| 4/4 EPS beats | Avg +2.27% | yfinance earnings_history |
| EPS consensus trend (90d) | $17.53 -> $19.35 (+10.4%) | yfinance eps_trend |
| WACC (adopted) | 10.21% | Blume beta 1.290 + ERP 4.6% |

---
*Alpha Engine · ERP 4.6% Damodaran implied · Blume beta · yfinance 1.4.1 · 2026-06-15 · Not financial advice*
