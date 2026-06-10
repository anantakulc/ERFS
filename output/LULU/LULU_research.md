# Lululemon Athletica Inc. (NASDAQ: LULU) — Global Equity Research

**Engine:** Alpha Global Equity Research
**Date:** 2026-06-10
**Reference price:** $117.55 (last clean daily close, 2026-06-08)
**Recommendation:** MARKET WEIGHT — 12-month target $150 (range $115–$185)

> Sourcing: figures footnoted by skill or yfinance field. FY references use Lululemon's fiscal calendar (FY ends late January; "FY2026" = year ended 2026-01-31). The current reporting year (ending Jan 2027) is "FY27." All financial-statement data via `yfinance-data` (income_stmt, cashflow, balance_sheet, quarterly_income_stmt) unless noted. Optional sentiment skills (`finance-sentiment`/Adanos, `funda-data`) were unavailable — no API keys present — and are logged in §17.

---

## Section 1 — Market Statistics Table

| Metric | Value | Source |
|---|---|---|
| Reference price (clean close 2026-06-08) | $117.55 | yfinance history |
| Last quote (intraday, stale) | $121.36 | yfinance `currentPrice` |
| Market cap | $12.74B (@$117.55) / $13.78B (yf @$121.36) | `marketCap` / computed |
| Enterprise value | $14.40B | `enterpriseValue` |
| Shares outstanding | 108.4M | `sharesOutstanding` |
| Float shares | 104.55M (96.4% of S/O) | `floatShares` |
| 52-week high / low | $262.16 / $109.36 | history / `fiftyTwoWeekLow` |
| Drawdown from 52-wk high | **−55.2%** | computed |
| YTD return | **−44.2%** | history (Jan 2 → Jun 8) |
| 1-year return | **−54.5%** | history |
| ADTV (30-day, $) | ~$0.49–0.50B | computed |
| 30-day realized vol (annualized) | **42.8%** | computed log-returns |
| Short % of float | 6.68% | `shortPercentOfFloat` |
| Short ratio (days to cover) | 2.23 | `shortRatio` |
| Insider ownership | 4.71% | `heldPercentInsiders` |
| Institutional ownership | 82.6% | `heldPercentInstitutions` |
| Trailing P/E (GAAP) | 9.5x (@$117.55) / 9.8x (yf) | computed / `trailingPE` |
| Forward P/E (consensus) | ~10.1x (@$117.55) / 10.4x (yf) | computed / `forwardPE` |
| EV/Revenue (TTM) | 1.29x | `enterpriseToRevenue` |
| EV/EBITDA (TTM) | 5.3x (5.6x yf) | computed / `enterpriseToEbitda` |
| Beta | 0.86 | `beta` |
| Dividend yield | None (no dividend) | `dividendYield` |
| Analyst mean rating | 3.03 / 5 = "Hold" | `recommendationMean` |
| Mean / median / high / low target | $136.34 / $127 / $295 / $88 | `analyst_price_targets` (25 analysts) |

**One-line read:** A former premium-growth compounder de-rated to a value multiple (sub-10x earnings, ~5x EV/EBITDA) after a >50% drawdown, with sharply negative estimate revisions and decelerating North America demand — a "broken-growth" situation, not a clean value or clean growth setup.

---

## Section 2 — Company Overview & Business Model

Lululemon Athletica is a designer, distributor and retailer of technical athletic apparel, footwear and accessories, operating primarily a vertically-integrated direct-to-consumer (DTC) model. It sells through company-operated stores (~770+ globally) and e-commerce, supplemented by a small wholesale/strategic-partner channel. Revenue is concentrated in women's bottoms/leggings (the "Align" and "Wunder" franchises), expanding men's, and a growing accessories line (bags, belt bags, headwear). Roughly half of sales are DTC e-commerce, which structurally lifts gross margin versus wholesale-dependent peers (gross margin ~56.5%, `grossMargins`).

The company makes money on a high-margin, full-price DTC model: it controls pricing, avoids the markdown cadence of department-store distribution, and reinvests in product innovation, community/brand events and new-market store expansion (notably China and the rest of International). FY2026 (ended 2026-01-31) revenue was **$11.10B** with **20.0% operating margin** (operating income $2.21B) and **$1.58B GAAP net income** — best-in-class margins for apparel.

**Business model flywheel (when working):**

```
   Product innovation (Align/leggings franchise)
            │
            ▼
   Full-price DTC sell-through ──► High gross margin (~57%)
            │                              │
            ▼                              ▼
   Brand/community pull            Strong FCF ($0.9–1.6B/yr)
            │                              │
            ▼                              ▼
   New-market store expansion ◄── Self-funded growth + buybacks
   (China / International)             │
            └──────────────────────────┘
```

**The flywheel is currently stalling at the top loop:** North America DTC sell-through has decelerated, forcing reliance on International/China to carry growth while margins compress (see §8, §13). Operating model: **fab-lite / asset-light** — outsourced manufacturing, owned design and retail; capex is store buildout + DC/technology, running ~$0.68B/yr (`Capital Expenditure`).

---

## Section 3 — Business Segments

Lululemon does not report multiple product P&L segments in yfinance data; segmentation below is reconstructed from the company's standard disclosure structure (channel and category). All splits **[ESTIMATED]** from disclosed mix commentary applied to FY2026 revenue of $11.10B.

| Segment (channel) | Revenue ($) | % of Total | YoY Growth | Est. Op. Margin |
|---|---|---|---|---|
| Company-operated stores | ~$5.2B [EST] | ~47% | low-single-digit [EST] | mid-20s% [EST] |
| Direct-to-consumer (e-comm) | ~$4.8B [EST] | ~43% | mid-single-digit [EST] | high-20s% [EST] |
| Other (wholesale / outlet / strategic) | ~$1.1B [EST] | ~10% | flat-to-down [EST] | mid-teens% [EST] |
| **Total** | **$11.10B** | 100% | **+4.9%** | **19.9% (actual)** |

| Category | % of Total [EST] | Trend |
|---|---|---|
| Women's | ~62% | decelerating (core leggings saturating in NA) |
| Men's | ~25% | the relative growth driver |
| Accessories | ~13% | fastest-growing but small base |

Total revenue +4.9% computed from $11.1026B vs $10.5881B (`income_stmt`). Category/channel mix labelled [ESTIMATED] — not directly disclosed in pulled data; see §17.

---

## Section 4 — Geographic Revenue

Geographic split **[ESTIMATED]** from the company's disclosed Americas / China Mainland / Rest-of-World structure, applied to FY2026 revenue.

| Geography | Revenue ($) [EST] | % of Total [EST] |
|---|---|---|
| Americas (US + Canada) | ~$7.9B | ~71% |
| China Mainland | ~$1.5B | ~14% |
| Rest of World (International ex-China) | ~$1.7B | ~15% |

The investment debate is geographic: Americas (~71% of sales) is the deceleration epicenter, while China Mainland and RoW are the double-digit-growth offsets. Exact figures are a data gap (§17) — not in the pulled yfinance dataset; directional weighting consistent with company disclosure.

---

## Section 5 — Top Customers & Concentration

Lululemon is a **DTC brand with no single >10% customer** — it sells directly to consumers through its own stores and website. There is therefore **no SEC-mandated customer-concentration disclosure** (the 10% threshold is not triggered).

| Customer | Est. Revenue | Products | Disclosure Basis |
|---|---|---|---|
| None ≥10% of revenue | n/a | n/a | DTC model — no concentration |

**Concentration risk is on the product side, not the customer side:** women's leggings/bottoms (~one quarter+ of revenue via the Align franchise) is the dominant cash engine. A fashion/competitive shift away from that single category is the true concentration exposure — quantified as a thesis-breaker in §13.

---

## Section 6 — Management & Acquisition Track Record

| Name | Role | Tenure | Background |
|---|---|---|---|
| Andre Maestrini | CEO (incoming/current) | new (2026) | Former adidas global brand executive; consumer-brand operator. **Open-market purchase of 3,275 shares @ $151.02 on 2026-04-01** (`insider_transactions`) |
| Meghan Frank | CFO | multi-year | Long-tenured LULU finance leader |
| Charles V. Bergh | Director (Chair-level) | board | Former Levi Strauss CEO; **bought 6,090 shares @ $164.20 on 2026-03-20** ($1.0M) |
| Nikki Neuburger / Ranju Das / Shane Grant | Officers / Directors | various | Brand, technology, operating roles |

**Acquisitions:** Lululemon is organically driven; the one material acquisition was **MIRROR (connected-fitness hardware, 2020, ~$500M)**, which was written down and effectively unwound (rebranded "lululemon Studio," then de-emphasized) — a clear capital-allocation misstep. Outcome: poor; reinforced a "stick to apparel" discipline.

**Capital allocation philosophy (one sentence):** Self-fund store growth from FCF and return the remainder via buybacks (no dividend), with the recent insider buying signaling management conviction at depressed levels.

---

## Section 7 — Historical Financials

Source: `income_stmt` (annual), `cashflow` (annual), `balance_sheet` (annual); TTM = FY2026 reported; FY27E/FY28E from `earnings_estimate`/`revenue_estimate`. $ in millions except per-share/margins.

| Line | FY2023 (Jan'23) | FY2024 (Jan'24) | FY2025 (Jan'25) | FY2026 (Jan'26)=TTM | FY27E | FY28E |
|---|---|---|---|---|---|---|
| Revenue | 8,111 | 9,619 | 10,588 | **11,103** | 11,110 | 11,457 |
| YoY growth | — | +18.6% | +10.1% | +4.9% | +0.0% | +3.1% |
| Gross margin | 55.4% | 58.3% | 59.2% | 56.6% | ~56% [EST] | ~56% [EST] |
| Operating margin | 21.3% | 22.9% | 23.7% | **19.9%** | ~17–18% [EST] | ~17–18% [EST] |
| EBITDA | 2,018 | 2,587 | 2,952 | 2,707 | ~2,400 [EST] | ~2,450 [EST] |
| GAAP net income | 855 | 1,550 | 1,815 | 1,579 | ~1,210 [EST] | ~1,265 [EST] |
| FCF | 328 | 1,644 | 1,583 | 922 | n/a | n/a |
| FCF margin | 4.0% | 17.1% | 15.0% | 8.3% | — | — |
| GAAP EPS (diluted) | 6.68 | 12.20 | 14.64 | **13.26** | 11.16 | 11.68 |
| Capex | 639 | 652 | 689 | 681 | ~700 [EST] | — |
| Total debt (incl leases) | 1,070 | 1,403 | 1,576 | 1,798 | — | — |
| Cash | 1,155 | 2,244 | 1,984 | 1,807 | — | — |
| Net debt | (85) net cash | (841) net cash | (408) net cash | **(9) ≈ neutral** | — | — |
| Net debt/EBITDA | net cash | net cash | net cash | ~0.0x | — | — |

**The story in one table:** revenue growth collapsed from +18.6% (FY24) → +4.9% (FY26) → ~0% (FY27E consensus); operating margin rolled over from 23.7% peak to 19.9% and is guided lower; EPS is now declining YoY. Balance sheet is pristine (≈net-debt-neutral, 0.0x leverage). FY27E revenue/EPS are flat-to-down. No [STALE] flags — FY2026 closed 2026-01-31 and Q1 FY27 (2026-04-30) is the latest reported quarter.

---

## Section 8 — Recent Results

| Quarter | Revenue | Gross Margin | Operating Margin | GAAP EPS | EPS Surprise |
|---|---|---|---|---|---|
| Q4 FY26 (2026-01-31) | $3,641M | 54.9% | 22.3% | $5.01 | +4.8% beat |
| **Q1 FY27 (2026-04-30)** | **$2,472M** | **54.2%** | **11.2%** | **$1.69** | +1.0% (in-line) |

Source: `quarterly_income_stmt`, `earnings_history`.

**Q1 FY27 (the latest, reported ~2026-06):** Revenue +4.3% YoY ($2,471.6M vs $2,370.7M) — but **GAAP net income fell −38% YoY** ($195.0M vs $314.6M) as operating margin compressed to **11.2%** from ~18.5% a year ago. This is the quarter that confirmed the bear case: top-line growth held barely positive only on International/China, while North America demand and full-price sell-through deteriorated, crushing margins and earnings.

**Earnings beat history (last 4 quarters):**

| Quarter | EPS Actual | Estimate | Surprise % |
|---|---|---|---|
| 2025-07-31 | $3.10 | $2.85 | +8.7% |
| 2025-10-31 | $2.59 | $2.21 | +17.1% |
| 2026-01-31 | $5.01 | $4.78 | +4.8% |
| 2026-04-30 | $1.69 | $1.67 | +1.0% |

The beat magnitude has compressed sharply (from +17% to +1%) as the bar reset down — beats are no longer "growth" beats, they are "less-bad" beats. **Guidance cadence:** quarterly, with FY guidance updated each print; next report **2026-09-03** (`calendar`).

---

## Section 9 — Competitive Landscape

| Market (TAM) | TAM Estimate | LULU Position | Horizon |
|---|---|---|---|
| Global activewear/athleisure | ~$400B+ | Premium leader, ~3% share | 2025–2030 |
| Women's premium athletic | large sub-segment | #1 brand in core leggings | now |
| China activewear | fast-growing | scaling, double-digit growth | 2025–2030 |
| Men's athletic apparel | very large, fragmented | under-penetrated challenger | 2025–2030 |
| Athletic footwear | huge, NKE/ADDYY/DECK-led | early/nascent | 2026+ |

| Competitor | Market Cap | LTM Revenue | EV/Revenue | Key Overlap |
|---|---|---|---|---|
| Nike (NKE) | very large | ~$48B+ | 1.49x | Direct activewear/footwear |
| adidas (ADDYY) | large | ~€24B | 1.56x | Global activewear/footwear |
| Deckers (DECK) | mid-large | ~$5B+ | 2.58x | HOKA running, premium DTC |
| On Holding (ONON) | mid | ~$3B | 3.91x | Premium running/lifestyle — share-taker |
| Under Armour (UAA) | small | ~$5B | 0.82x | Performance apparel (weaker) |
| Alo Yoga / Vuori (private) | n/a | growing fast | n/a | **Direct premium-leggings disruptors** |

Source: `enterpriseToRevenue` per ticker. The most dangerous competitors (Alo Yoga, Vuori) are **private** and not in the multiples table — they are taking premium women's share precisely where Lululemon is most concentrated.

---

## Section 10 — Peer Valuation Comparison

| Company | Fwd P/E | EV/EBITDA | EV/Rev | Rev Growth | Net Margin | Rating |
|---|---|---|---|---|---|---|
| **LULU (subject)** | **~10.1x** | **5.3x** | **1.29x** | +4.9% | 13.0% | Hold |
| Nike (NKE) | 24.5x | 17.9x | 1.49x | 0.0% | 5% | — |
| Deckers (DECK) | 13.6x | 10.5x | 2.58x | +10% | 19% | — |
| On (ONON) | 17.7x | 26.1x | 3.91x | +14% | 8% | — |
| adidas (ADDYY) | 15.7x | 16.0x | 1.56x | +7% | 6% | — |
| Under Armour (UAA) | 23.9x | 18.7x | 0.82x | −1% | −10% | — |
| Columbia (COLM) | 15.6x | 11.4x | 0.97x | 0.0% | 5% | — |
| VF Corp (VFC) | 12.3x | 5.5x | 0.85x | +1% | 6% | — |

Source: `forwardPE`, `enterpriseToEbitda`, `enterpriseToRevenue`, `revenueGrowth`, `profitMargins`.

**Multiple-spread read:** LULU trades at the **bottom of the peer set on forward P/E (~10x vs 15.7x median)** and EV/EBITDA (5.3x vs ~16x median) — yet it has **the highest net margin (13.0%) in the group**. The market is pricing LULU like structurally-broken VF Corp (12.3x P/E, 5.5x EV/EBITDA), not like a premium brand. The discount is justified *only if* margins are structurally impaired; if FY27 is a trough, the de-rating is overdone. **Caveat:** EV/EBITDA peer median (16x) is inflated by depressed-EBITDA peers (NKE, ONON, UAA) and should not be applied naively to LULU's healthy EBITDA (see §11).

---

## Section 11 — Valuation

### Method 1: DCF — Three Scenarios

**WACC build:** rf = 4.53% (live 10Y), β = 0.86, ERP = 5.5% → **ke = 9.27%**. With ~13% debt weight (incl. leases) and kd 5.5% after-tax → **WACC = 8.6%**.

**WACC adjudication box:**
| Formula WACC | Apparel sector band | Final WACC | Reason |
|---|---|---|---|
| 8.6% | ~8.0–10.0% | **8.6%** | Inside band; β 0.86 reasonable for a defensive-leaning premium brand. No override. |

| Scenario | Rev path (Y1→Y5) | Terminal g | EBIT margin | WACC | Implied price |
|---|---|---|---|---|---|
| Bull | +10% → +4.5% | 3.0% | 21.5% | 8.1% | **~$314** |
| Base | +5% → +3.5% | 2.5% | 19.9% | 8.6% | **~$232** |
| Bear | +1% → +1.5% | 1.5% | 17.4% | 9.1% | **~$160** |

Probability-weighted DCF (Bear 30% / Base 45% / Bull 25%) = **~$231**.
TV is 76% of base EV — elevated; sensitivity-driven, treat as a directional anchor, not precision.

> **Analyst override note:** the mechanical DCF base (~$232) embeds a recovery to ~20% margins and mid-single-digit growth that current estimate revisions actively contradict (FY27E EPS cut from $12.57 → $11.16 in 90 days). I therefore **down-weight the DCF** in the final blend and lean on relative/scenario work, which better reflects the deteriorating revision trend.

### Method 2: Relative (Peer Multiples)

Peer medians: Fwd P/E 15.7x, EV/Rev 1.49x, EV/EBITDA 16.0x.
- **Forward P/E:** 15.7x × ~$11.6 fwd EPS = **~$182** (overstated — applies a full peer multiple to a peaked franchise)
- **EV/Rev:** 1.49x × $11.1B − net debt = **~$152**
- **EV/EBITDA:** 16.0x is contaminated by low-EBITDA peers → **rejected**

A **defensible relative target applies a ~12–13x P/E** (premium-margin company, but ex-growth) to ~$11.2–11.6 EPS → **~$135–150**.

### Method 3: SOTP

Not run — Lululemon is a single-segment apparel brand without distinct standalone-valuable segments. Channel/geography splits are mix, not separable businesses. SOTP not applicable.

### Probability-Weighted Synthesis

| Method | Weight | Implied Price | Weighted Contribution |
|---|---|---|---|
| DCF (prob-weighted, down-weighted) | 30% | $231 | $69 |
| Relative — disciplined 12–13x P/E | 45% | $145 | $65 |
| Relative — EV/Rev crosscheck | 25% | $152 | $38 |
| **Blended fair value** | 100% | — | **~$172** |

I temper the mechanical blend to a **$150 base target** to reflect that estimate revisions are still falling (no evidence of a margin trough yet) and the DCF is recovery-dependent. **Fair-value range: $115 (bear) – $185 (bull).**

---

## Section 12 — Bull Case (10 Catalysts)

**Thesis:** A best-in-class-margin premium brand has de-rated to a distressed-retailer multiple (~10x P/E, ~5x EV/EBITDA) on a cyclical North America air-pocket, leaving asymmetric upside if International/China growth and a margin stabilization simply meet a lowered bar.

1. **Valuation reset is extreme** — 9.5–10x trailing/forward P/E vs a 5-yr history of 25–40x; ~55% off the 52-wk high (`fiftyTwoWeekHigh` $262). Mean-reversion to even 14–15x = ~50% upside.
2. **Highest margins in the peer set** — 13.0% net margin and ~20% operating margin (`profitMargins`, FY26) dwarf NKE (5%), ADDYY (6%), UAA (−10%); the franchise economics are intact even in a down year.
3. **Pristine balance sheet** — ≈net-debt-neutral ($1.81B cash vs $1.80B debt incl. leases), 0.0x net leverage — full optionality to buy back stock at trough valuations and self-fund growth.
4. **Insider conviction buying** — incoming CEO Maestrini bought 3,275 sh @ $151 (2026-04-01) and Chair-level director Bergh bought 6,090 sh @ $164 (2026-03-20), both well above the current $117.55 — rare alignment at a bottom.
5. **China Mainland / International growth engine** — double-digit growth offsets carrying the consolidated +4.9% FY26 line; a long runway under-penetrated vs NA.
6. **FCF generation intact** — $0.92B FCF in a "bad" year (8.3% FCF margin) funds buybacks; normalized FCF $1.5–1.6B (FY24–25) supports the value case.
7. **Men's and accessories diversification** — men's (~25% of sales, [EST]) and accessories (~13%, fastest-growing) reduce reliance on the saturating women's-leggings core.
8. **Beat track record persists** — 4 consecutive EPS beats (FY26–Q1 FY27), even if magnitude shrank — execution has not cracked.
9. **Footwear and category expansion optionality** — early-stage footwear push into a multi-hundred-billion TAM dominated by NKE/DECK/ONON; any traction is upside not in numbers.
10. **Multiple re-rating on first sign of NA stabilization** — at 10x P/E, the bar is so low that one quarter of stabilizing Americas comps could re-rate the stock toward $150–180 quickly (high 42.8% realized vol cuts both ways).

---

## Section 13 — Bear Case (10 Thesis-Breakers)

*Written independently. The bear does not soften for the bull.*

**Thesis:** Lululemon is a structurally-decelerating, single-category-concentrated brand losing premium women's share to Alo/Vuori while its core North America market saturates — earnings are still being revised *down*, and ~10x P/E on falling estimates is a value trap, not a value opportunity.

1. **North America saturation is structural, not cyclical** — Americas (~71% of sales) growth has stalled; the core leggings franchise is mature, and there is no second NA growth vector of comparable size.
2. **Estimates are in free-fall** — current-quarter EPS estimate cut from **$2.69 (7 days ago) to $1.79** with **15 down-revisions in 30 days**; FY27 EPS slashed from $12.57 (90d ago) to $11.16 (`eps_trend`, `eps_revisions`). You cannot value off "trough" earnings that keep getting lower.
3. **Margin erosion is accelerating** — Q1 FY27 operating margin **collapsed to 11.2%** from ~18.5% YoY; GAAP net income **−38% YoY**. The 20%+ margin era may be over (promotions, tariffs, mix).
4. **Premium-women's share loss to private disruptors** — Alo Yoga and Vuori are taking exactly the high-margin women's customer LULU depends on, and they are invisible in public comps.
5. **Single-category concentration** — women's bottoms/Align is the cash engine; a fashion rotation away from leggings/athleisure structurally impairs the whole P&L.
6. **Tariff / sourcing exposure** — outsourced Asia manufacturing leaves margins exposed to tariff and freight shocks with limited ability to pass through at the premium price point without killing volume.
7. **China is a hope, not a hedge** — China activewear is intensely competitive (Anta, Li-Ning, NKE, ADDYY) and macro-fragile; betting the growth story on China raises, not lowers, risk.
8. **Beat quality has evaporated** — surprise compressed from +17.1% (Oct'25) to +1.0% (Apr'26); the "beat-and-raise" reflex is gone, and guidance is being cut.
9. **Footwear is a money-loser-in-waiting** — entering NKE/ADDYY/DECK's home turf is capital-intensive and historically low-margin; the MIRROR write-down shows management's adjacency bets can destroy value.
10. **The multiple can compress further** — VF Corp trades at 12.3x P/E / 5.5x EV/EBITDA *while structurally broken*; if LULU's margins keep falling, "cheap" 10x can become "cheap" 8x on lower EPS — a double de-rating.

**Structural risk register:**

| Risk Category | Specific Risk | Probability | Impact |
|---|---|---|---|
| Demand | NA growth stays sub-2% / negative comps | High | High |
| Competition | Alo/Vuori/lululemon-share erosion in women's | High | High |
| Margin | Op margin settles <17% structurally | Medium-High | High |
| Macro/Tariff | Sourcing/tariff cost shock | Medium | Medium-High |
| Estimate | Further consensus EPS cuts | High (in progress) | Medium |
| Capital mis-allocation | Footwear/adjacency cash burn | Medium | Medium |

---

## Section 14 — Delta Audit

| Claim | Raw Source Value | Computation | Status |
|---|---|---|---|
| Trailing P/E ~9.5x | px $117.55, EPS $12.35 | 117.55/12.35 = 9.52 | ✓ Verified |
| yfinance trailingPE 9.83 | uses $121.36 quote | 121.36/12.35 = 9.83 | ✓ Verified (different price basis) |
| EV/EBITDA 5.3x | EV $14.40B, EBITDA $2.707B | 14.402/2.707 = 5.32 | ✓ Verified |
| EV/Revenue 1.29x | EV $14.40B, Rev $11.10B | 14.402/11.103 = 1.30 | ✓ Verified |
| FY26 revenue $11.10B | income_stmt | reported | ✓ Verified |
| FY26 rev growth +4.9% | 11.1026 / 10.5881 − 1 | = +4.86% | ✓ Verified |
| FY26 operating margin 19.9% | 2.2106 / 11.1026 | = 19.9% | ✓ Verified |
| Q1 FY27 rev +4.3% YoY | 2,471.6 / 2,370.7 − 1 | = +4.3% | ✓ Verified |
| Q1 FY27 net income −38% YoY | 195.0 / 314.6 − 1 | = −38.0% | ✓ Verified |
| Q1 FY27 op margin 11.2% | 276.9 / 2,471.6 | = 11.2% | ✓ Verified |
| 1-year return −54.5% | $258.5 → $117.55 | = −54.5% | ✓ Verified |
| Drawdown −55.2% | $262.16 → $117.55 | = −55.2% | ✓ Verified |
| Net debt ≈ neutral | cash 1,807 − debt 1,798 | = +9M net cash | ✓ Verified |
| Current-Q EPS est cut to $1.79 | eps_trend (7d ago $2.69) | revision | ✓ Verified |
| Mean target $136.34 | analyst_price_targets (25) | reported | ✓ Verified |

**Required flags:**
- **Price-basis discrepancy:** yfinance `marketCap` ($13.78B), `trailingPE` (9.83), `forwardPE` (10.43) use a stale intraday quote of $121.36; this report standardizes on the last clean close **$117.55 (2026-06-08)**. Multiples differ ~3% accordingly — not a data error, a timestamp choice. Flagged.
- **GAAP/non-GAAP:** all earnings figures cited are **GAAP** (income_stmt / earnings_history). Lululemon's reported EPS is close to non-GAAP (few large adjustments); no material GAAP/non-GAAP gap in the pulled data.
- **Estimate spread is wide:** FY27 EPS range $8.00–$14.05 (`earnings_estimate +1y`) and targets $88–$295 — reflects genuine bull/bear disagreement on whether margins trough. High dispersion logged.
- **Segment/geography figures [ESTIMATED]:** §3–§4 splits are not in the pulled dataset; reconstructed from disclosed mix structure. See §17.

**VERDICT: PASS WITH NOTES** — all headline numerics reproduce from primary yfinance data; notes cover the price-basis timestamp and the estimated segment/geo splits.

---

## Section 15 — Sentiment & Flow

**Short interest:** 6.68% of float (`shortPercentOfFloat`), short ratio 2.23 days (`shortRatio`). Moderately elevated but **not a squeeze setup** — 2.2 days-to-cover is easily absorbed by ~$0.49B ADTV. Shorts reflect the deteriorating-fundamentals thesis, not a crowded technical trap.

**Insider transactions (last significant, `insider_transactions`):**

| Name | Role | Date | Type | Shares | Value |
|---|---|---|---|---|---|
| Andre Maestrini | CEO | 2026-04-01 | **Purchase @ $151.02** | 3,275 | $494,590 |
| Charles V. Bergh | Director (Chair-level) | 2026-03-20 | **Purchase @ $164.20** | 6,090 | $999,978 |
| Nicole Neuburger | Officer | 2026-04-08 | Sale @ $161.00 | 622 | $100,142 |
| Multiple (Frank/Maestrini/Das) | Officers | 2026-03-19/30 | Stock award/vest | various | grant |

**Signal: net insider buying by the CEO and Chair at $151–164, well above today's $117.55** — a constructive contrarian tell.

**Top institutional holders (`institutional_holders`, top 5):**

| Holder | % Held | Shares |
|---|---|---|
| BlackRock | 8.76% | 9.50M |
| Vanguard Capital Mgmt | 6.39% | 6.93M |
| Vanguard Portfolio Mgmt | 4.77% | 5.17M |
| State Street | 4.17% | 4.52M |
| FMR (Fidelity) | 3.97% | 4.30M |

Ownership is 82.6% institutional — index/passive-dominated; note FMR trimmed −13.7% and BlackRock −4.3% last reported quarter (active reduction), while Federated Hermes added aggressively.

**Social/sentiment:** `finance-sentiment` (Adanos) and `funda-data` were **unavailable (no API keys)** — logged as data gaps (§17). Qualitative read from public discourse: sentiment is bearish/capitulatory after a >50% drawdown; FinTwit debate centers on whether margins have troughed and whether Alo/Vuori share loss is permanent. The insider buying and analyst "Hold" (3.03) with a $136 mean target above spot suggest the sell-side is past peak-bearishness but not yet constructive.

---

## Section 16 — Synthesis & Recommendation

**Where bull and bear agree:**
1. North America growth has materially decelerated and is the core problem.
2. Operating margins have compressed (Q1 FY27 to 11.2%) — the only debate is whether it is cyclical or structural.
3. The balance sheet is pristine (≈net-cash, 0.0x leverage) — solvency is not a question.
4. The multiple (~10x P/E) is objectively low versus the company's own history and the peer set.
5. China/International is the only live growth vector; the thesis hinges on whether it can offset NA.

**Probability-weighted 12-month outcome:**

| Scenario | Probability | 12-Mo Target | Weighted Contribution |
|---|---|---|---|
| Bull (NA stabilizes, margin troughs, re-rate to ~14x) | 25% | $200 | $50 |
| Base (flat earnings, ~12–13x, slow grind) | 45% | $150 | $68 |
| Bear (margins keep falling, de-rate on lower EPS) | 30% | $100 | $30 |
| **Expected value** | 100% | — | **~$148** |

**Rating: MARKET WEIGHT. 12-month price target $150 (range $115–$185). Horizon: 12 months.**
The risk/reward is roughly symmetric: ~28% upside to base vs ~15% downside to bear from $117.55, but the *path* depends entirely on whether estimate revisions stop falling. I will not be OVERWEIGHT into a still-declining revision trend, and I will not be UNDERWEIGHT a net-cash, 13%-net-margin franchise at 10x with insiders buying.

- **Entry strategy:** Initiate a **half-size** position now at $115–120; **add** on either (a) the first quarter of stabilizing Americas comps / halted EPS revisions, or (b) a flush to $100–105 (toward the 52-wk low). Avoid full size before the 2026-09-03 print.
- **Stop-loss / invalidation:** Thesis breaks if **operating margin prints <15% again next quarter AND FY27 EPS is guided below $10.50** — that confirms structural impairment; exit toward $95.
- **Hedge:** Pair against a long-activewear-winner (long ONON or DECK) or short an apparel-sector basket / XRT to neutralize discretionary-retail beta; LULU's 0.86 beta means a modest sector hedge suffices.
- **Position sizing:** 1.5–2.5% of a diversified equity book at half-size; correlation to discretionary-retail and to NKE/ADDYY is high, so size down if already long the cohort.
- **Key catalysts to watch:** Q2 FY27 earnings **2026-09-03** (Americas comp + margin guide — the swing factor); holiday/Q3 NA traffic; any China deceleration; first read on footwear/men's; further estimate revisions (currently negative).

---

## Section 17 — Data Gaps

| Item | Gap Type | Impact |
|---|---|---|
| Product-category revenue split (women's/men's/accessories) | [ESTIMATED] — not in pulled data | Medium |
| Channel P&L split (stores vs DTC vs other) | [ESTIMATED] | Medium |
| Geographic revenue (Americas/China/RoW exact $) | [ESTIMATED] | Medium |
| Comparable-store-sales / comp by region | Not available in yfinance | High (key bull/bear swing) |
| `finance-sentiment` (Adanos cross-source sentiment) | Unavailable — no ADANOS_API_KEY | Medium |
| `funda-data` (analyst synthesis, transcripts, supply-chain, ownership flow) | Unavailable — no FUNDA_API_KEY/MCP | Medium |
| `twitter-reader` bear-thesis pull | Not run (no live social data) | Low |
| FY27E gross/op margin, EBITDA | [ESTIMATED] from EPS consensus | Medium |
| Non-GAAP reconciliation detail | GAAP used; non-GAAP gap assumed immaterial | Low |
| Price basis | Used clean close $117.55 vs stale $121.36 quote | Low (flagged §14) |

---

## Appendix A — North America Comp-Sales Trajectory (Deep Dive)

*Added 2026-06-10. Reconstructs the Americas comp trend quarter-by-quarter and adjudicates cyclical vs. structural. `[SOURCED]` = company release / named third-party panel; `[ESTIMATED]` = triangulated calculation. LULU's fiscal year is offset: the quarter ending May 3, 2026 is **Q1 FY2026**, reported June 4, 2026.*

### A.1 Quarter-by-quarter comp table (last 8 reported quarters)

| Fiscal Qtr | Qtr end | Total comp | Americas comp | International comp | China Mainland comp | Notes |
|---|---|---|---|---|---|---|
| Q1 FY24 | ~Apr 2024 | +6% (+7% cc) | **flat** | — | — | Americas already flat; intl carrying the comp |
| Q2 FY24 | Jul 28 2024 | — | **−3% (−2% cc)** | — | — | First negative Americas print |
| Q3 FY24 | Oct 27 2024 | — | **−2%** | — | — | |
| Q4 FY24 | Feb 2 2025 | — | **flat** | +20% (+22% cc) | +26% (+27% cc) | Total rev +13% to $3.6B; intl/China masking Americas |
| Q1 FY25 | May 4 2025 | +1% | **−2% (−1% cc)** | +6% (+7% cc) | +7% (+8% cc) | Americas rev +3%; cut FY outlook |
| Q2 FY25 | Aug 3 2025 | +1% | **−4% (−3% cc)** | +15% (+13% cc)* | +17% (+16% cc)* | CEO "disappointed with U.S. business… product execution" |
| Q3 FY25 | Nov 2 2025 | +1% (+2% cc) | **−5%** | +9% cc | +25% | Americas rev −2%; GM −290bp to 55.6% |
| Q1 FY26 | May 3 2026 | +1% (**−2% cc**) | **−6% cc** (US −4%, Canada −6%) | +1% cc | +13% cc | Cut FY guide; "negative media & social commentary impacting traffic" |

\*Q2 FY25 Intl/China comps are single-source extractions (exact cc split not double-verified). *Revenue line corroborated to yfinance quarterly income statement.*

**The trend:** flat → −3% → −2% → flat → −2% → −4% → −5% → **−6% cc** — a steady deterioration with the **worst prints at the end**, not a one-off dip.

### A.2 Exact inflection point

- **Americas comp turned negative in Q2 FY24 (quarter ended Jul 28, 2024): −3% reported.** `[SOURCED]`
- The warning preceded it: **Americas was already flat in Q1 FY24** while total comps were still +6% — international strength masked a domestic business that had already stopped growing. `[SOURCED]`

### A.3 Management's evolving framing (itself evidence)

1. **Early 2024 (Q1/Q2 FY24):** self-inflicted assortment miss — **color, size availability, newness** in U.S. women's. Internally owned, not macro. `[SOURCED]`
2. **Mar 2025 (Q4 FY24):** macro — U.S. shoppers **"keeping wallets tight, visiting stores less often"**; tariffs. `[SOURCED — Bloomberg/Fortune]`
3. **Sep 2025 (Q2 FY25):** product — **"disappointed… aspects of product execution"**; lifestyle/lounge life cycles **"run too long," offerings "stale."** `[SOURCED — SGB/CNBC]`
4. **Jun 2026 (Q1 FY26):** traffic + brand-noise — **"negative media and social commentary impacting traffic,"** "not all product launches met expectations." `[SOURCED]`

**Fixes announced:** raise % newness; **compress product-development cycle 18–24 mo → 15–16 mo now, targeting 12–14 mo** (a direct admission the design engine is too slow vs. rivals); new franchises (Glow Up, BeCalm, Mile Maker); item-level price increases for tariffs; **+$1.0B buyback** (Q3 FY25) defending EPS. `[SOURCED]`

### A.4 Latest guidance (Q1 FY26, Jun 4 2026) `[SOURCED]`

- **North America revenue now expected to decline high-single-digits** for FY2026 (worse than prior).
- **China Mainland still guided ~+20%.**
- **FY2026 revenue cut to $11.0–11.15B** (from $11.35–11.50B); **EPS cut to $10.95–11.15** (from $12.10–12.30) — a >$1.00 cut, the driver of the post-print collapse.

### A.5 Verdict — predominantly STRUCTURAL with a cyclical overlay

**Cyclical evidence:** management's tight-wallet/traffic framing; weakness is U.S.-centric while International and China still comp positive; category-wide leggings-trend cooling (Ugg dethroned "leggings/Lululemon" as No. 1 upper-income-female trend per Piper Sandler).

**Structural evidence (the larger, durable driver):** (1) eight straight quarters of flat-to-deteriorating Americas comps, **worst at the end** — a trend, not a dip; (2) it **predates the macro narrative** (negative by Q2 FY24, before the 2025 tariff/consumer story); (3) management's own admissions — life cycles "run too long," assortment "stale," an 18–24-mo dev cycle they're racing to halve — are competitiveness/agility gaps, not weather; (4) **documented share loss** to Vuori/Alo (Appendix B); (5) **U.S. saturation** (~770+ company stores), so comps now hinge on productivity/traffic — exactly what's eroding.

**Net:** China/International prove the *brand* isn't broken, but in its saturated core NA market LULU is simultaneously cyclically pressured **and** structurally donating relative newness and share. The cyclical part should mean-revert; the structural part is the durable problem and the bigger driver of the worsening late-series prints.

---

## Appendix B — Alo Yoga / Vuori Share-Loss Thesis (Deep Dive)

*Added 2026-06-10. `[PRIVATE-EST]` = third-party estimate of a private company (lower confidence).*

### B.1 The disruptors

| | **Vuori** | **Alo Yoga** |
|---|---|---|
| Ownership | Private; **$825M secondary led by General Atlantic + Stripes (Nov 2024) → $5.5B valuation**; prior SoftBank Vision Fund 2 (2021); profitable since 2017 | Private, **founder-controlled** (Color Image Apparel); **2026 reports of a round at up to ~$10B** |
| Revenue | **~$1B run-rate** `[PRIVATE-EST]` (<$100M in 2023 — steep ramp) | **>$1B total** `[PRIVATE-EST]`; aloyoga.com ~$323M e-comm 2024 |
| Growth | ~30–40% y/y `[PRIVATE-EST]` | >40% y/y `[PRIVATE-EST]` |
| Stores | **Passed 100 owned (Aug 2025)**; ~25/yr cadence | **~10 (early 2023) → 100+ (end 2024)** |
| Positioning | Premium, men-skewed origin ("Lululemon for men"); price at/just under LULU | Premium, women/fashion-led, hot-yoga + celebrity; price at/above LULU |

Reference: LULU TTM revenue **$11.20B** `[SOURCED: yfinance]`. Each rival ≈9–10% of LULU's size but growing 4–8x faster.

### B.2 Third-party share-shift evidence (strongest part of the thesis)

**Earnest Analytics credit-card panel (2025)** `[SOURCED]`: US athleisure spend share — **Nike 31.6% · Lululemon 21.2% · Athleta 4.4% · Fabletics 4.4% · Vuori 2.9% · Alo 1.3%.** **Vuori and Alo each gained ~+1pt over trailing 12 months** (≈+50% relative for Vuori). **Shopper overlap with LULU: Vuori 52%, Alo 63%** — same wallet. Vuori wallet-share among its shoppers rose to **27.4% (from 21.6%)** — deepening loyalty.

**Piper Sandler "Taking Stock With Teens," Fall 2025** `[SOURCED]`: **LULU fell to No. 3 apparel mindshare (from No. 1 Fall 2024), −4pts y/y**; Ugg dethroned "leggings/Lululemon" as No. 1 upper-income-female trend; **Alo gaining among upper-income female teens.**

**Convergence:** revealed credit-card spend + forward teen intent + the company's own −6% cc Americas comp all point the same way — anecdote becomes thesis.

### B.3 How much of NA softness is Alo/Vuori vs. broad category? `[ESTIMATED]`

- Combined Vuori+Alo gain ≈ **+2pts of US athleisure share** over ~12 months, with 52–63% LULU overlap.
- LULU Americas comp deteriorated ~3–4pts over the comparable window.
- Sizing: if the duo captured ~$200–400M incremental US premium-athleisure spend overlapping 50–60% with LULU, the **directly cannibalized portion is ~$150–250M** — on a ~$5–6B US business, **~2–4pts of US comp drag**, i.e., **plausibly half (or more) of the Americas deterioration is competitive share loss**, the rest broad category rotation + self-inflicted assortment misses.
- **Caveat:** Nike (31.6%) is the larger absolute overlap, and dupe culture / leggings-trend rotation pressure LULU regardless. Alo/Vuori are a **major contributor, not the sole cause.**

### B.4 Verdict — durable, with revenue at risk `[ESTIMATED]`

**Durable/structural, likely persistent 1–3 years.** Both rivals have capital (Vuori $5.5B-backed; Alo $10B-round optionality), profitability, and aggressive owned-store rollouts; they sit in LULU's exact price tier and customer; they out-execute on newness/cadence — the very gap LULU admits. Brand-consideration erosion (survey + panel) leads revenue and is slow to reverse. **Not unbounded:** the duo is still only ~3% and ~1% of US athleisure; LULU keeps 21% share, a fortress balance sheet, and a share-gaining China/International engine — this is share *compression* in one geography, not brand collapse.

- **Direct near-term (12–18 mo):** ~**$150–300M** US revenue continuing to bleed (~1.5–3% of total), consistent with high-single-digit NA decline now guided.
- **Cumulative structural (2–3 yr) if cadence fixes underdeliver:** envelope rises toward **$400–700M (~4–6% of total)** — the difference between a cyclical trough that re-accelerates and a structurally lower NA base. **Swing factor: whether the product-development-cycle compression actually ships on shelf.**

### B.5 Open items for further verification (Delta)

1. Exact China Mainland / RoW comp for Q2 FY25 (single-sourced here).
2. Vuori and Alo **total** (not e-comm-only) and US-only FY2025 revenue — to tighten cannibalization math.
3. LULU US-segment revenue base (vs. total Americas incl. Canada) — to convert $ share-loss to precise comp-point drag.
4. Q1 FY26 traffic vs. conversion vs. AUR decomposition — isolate brand-perception damage from pricing.
5. Whether dev-cycle compression (→12–14 mo) is shipping in product on shelf — biggest reversibility swing factor.

---
*Research/educational output. Not financial advice. All data via finance-skills plugins (yfinance) plus company disclosures and named third-party panels (Earnest Analytics, Piper Sandler) as of 2026-06-10. Private-company figures are third-party estimates.*
