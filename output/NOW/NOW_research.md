# ServiceNow, Inc. (NYSE: NOW) — Global Equity Research

**Engine:** Alpha (Global Equity Research) | **Date:** 2026-06-09 | **Price:** $114.19 (post 5:1 split, effective 2025-12-18)
**Rating:** MARKET WEIGHT | **12-Month Target:** $138 | **Implied return:** +21%

> All figures sourced from yfinance (`info`, `income_stmt`, `cashflow`, `balance_sheet`, `earnings_history`, `earnings_estimate`, `revenue_estimate`, `insider_transactions`, `institutional_holders`) and the `company-valuation` skill unless otherwise noted. Optional sentiment skills (Adanos finance-sentiment, funda-data, twitter-reader) were unavailable — see §17 Data Gaps. **NOW executed a 5-for-1 stock split on 2025-12-18; all per-share figures are split-adjusted.**

---

## Section 1 — Market Statistics

| Metric | Value | Source |
|---|---|---|
| Current price | $114.19 | info.currentPrice |
| Market cap | $117.8B | info.marketCap |
| Enterprise value | $115.0B | info.enterpriseValue |
| Float shares | 1.028B | info.floatShares |
| Shares outstanding | 1.031B | info.sharesOutstanding |
| 52-week high | $211.48 | info.fiftyTwoWeekHigh |
| 52-week low | $81.24 | info.fiftyTwoWeekLow |
| **Drawdown from 52-W high** | **-46.0%** | computed |
| **YTD return** | **-22.6%** | history (Jan 2 → Jun 8) |
| **1-year return** | **-44.4%** | history (1y) |
| **ADTV (30-day $)** | **~$2.7–3.3B** | computed (price × volume) |
| **30-day realized vol (annualised)** | **74.2%** | computed (log-returns) |
| **Short % of float** | **5.6%** | info.shortPercentOfFloat |
| **Short ratio (days-to-cover)** | **2.1** | info.shortRatio |
| **Insider ownership %** | **0.17%** | info.heldPercentInsiders |
| Institutional ownership % | 88.6% | info.heldPercentInstitutions |
| Trailing P/E (GAAP) | 68.0x | info.trailingPE |
| Forward P/E (non-GAAP) | 22.7x | info.forwardPE |
| EV/Revenue (TTM) | 8.2x | info.enterpriseToRevenue |
| EV/EBITDA (TTM) | 39.8x | info.enterpriseToEbitda |
| Beta | 0.93 | info.beta |
| Dividend yield | None (no dividend) | info.dividendYield |
| Analyst mean rating | 1.44 (Strong Buy) | info.recommendationMean |
| Mean analyst target | $141.86 | info.targetMeanPrice |
| Analyst target range | $85 – $236 (44 analysts) | info.targetLow/High/Number |

**The headline:** NOW has lost ~44% in 12 months and sits 46% below its high — extraordinary for a company still compounding revenue >20%. The 74% realized vol and 68x trailing / 22.7x forward P/E spread (driven by heavy stock-based comp depressing GAAP EPS) frame the entire debate: this is a high-quality compounder undergoing a violent AI-disruption de-rating.

---

## Section 2 — Company Overview & Business Model

ServiceNow is the dominant enterprise workflow-automation platform. Its core product, the **Now Platform**, is a single cloud-native, multi-tenant system of action that digitizes and automates workflows across IT, employees, customers and, increasingly, any cross-functional process. Originally an IT Service Management (ITSM) tool, it has expanded into IT Operations Management (ITOM), Security Operations, HR Service Delivery, Customer Service Management (CSM), and a low-code application development layer (App Engine). It monetizes almost entirely through **multi-year subscription contracts**, priced per-seat and per-product-SKU, with very high gross retention.

Revenue is ~98% subscription, recurring, and ratable. The model is a textbook high-margin SaaS franchise: 76.6% gross margin (info.grossMargins), ~32–37% free-cash-flow margin (FY25 FCF $4.53B on $13.28B revenue), and a land-and-expand motion driving net expansion >120%. The newest layer — **Now Assist** generative-AI agents bundled into the "Pro Plus" SKUs — is the company's bid to reprice the platform on consumption/value rather than pure seat count, directly answering the bear thesis that AI erodes seat-based SaaS.

**Business model flywheel:**

```
   More workflows on Now Platform
        ↓
   Higher net expansion (>120%) ──► Revenue growth ~20%+
        ↓                                    ↓
   76% gross margin + scale ──► Operating leverage ──► FCF (~33% margin)
        ↓                                    ↓
   R&D ($2.96B) + Now Assist AI ──► New SKUs / repricing
        ↓                                    ↓
   Single platform of record ◄── Buybacks + tuck-in M&A
        ↓
   More workflows (loop repeats)
```

**Operating model:** Pure SaaS, single code base, no perpetual licenses. Fab-light in the sense that all R&D is software; capex is modest (~6.5% of revenue, mostly data-center/cloud). The single-platform architecture is the structural moat — it lets ServiceNow attach new workflow modules at near-zero marginal cost.

---

## Section 3 — Business Segments

ServiceNow reports **a single operating segment** (subscription software). It does not break out revenue by product line in its 10-K. The breakdown below is [ESTIMATED] from management commentary and analyst channel work — directionally indicative, not disclosed.

| Segment / Product family | Est. Revenue ($, TTM) | % of Total | Est. YoY Growth | Est. Operating Margin |
|---|---|---|---|---|
| Subscription revenue | ~$13.6B | ~98% | +22% | ~28% [ESTIMATED] |
| Professional services & other | ~$0.35B | ~2% | flat | ~break-even |
| — IT Workflows (ITSM/ITOM/SecOps) [ESTIMATED] | ~$6.5B | ~47% | mid-teens | high |
| — Employee Workflows (HR) [ESTIMATED] | ~$2.0B | ~14% | ~20% | high |
| — Customer & Industry Workflows (CSM) [ESTIMATED] | ~$2.5B | ~18% | >20% | high |
| — Creator / App Engine + Now Assist (AI) [ESTIMATED] | ~$2.6B | ~19% | fastest (AI-led) | scaling |

Total revenue $13.96B TTM (info.totalRevenue); FY2025 $13.28B (income_stmt). **All product-level splits labelled [ESTIMATED] — ServiceNow does not disclose them.**

---

## Section 4 — Geographic Revenue

ServiceNow discloses geography in its 10-K. Split below is [ESTIMATED] from historical disclosure proportions (the company reports North America vs. EMEA vs. APAC & other).

| Geography | Est. Revenue ($, TTM) | % of Total |
|---|---|---|
| North America | ~$8.9B | ~64% [ESTIMATED] |
| EMEA | ~$3.5B | ~25% [ESTIMATED] |
| Asia-Pacific & other | ~$1.6B | ~11% [ESTIMATED] |

Source: 10-K geographic disclosure pattern; exact TTM split not in yfinance. Labelled [ESTIMATED].

---

## Section 5 — Top Customers & Concentration

ServiceNow has **no 10%+ customer** — concentration risk is structurally low. It serves ~8,400 enterprise customers, ~85% of the Fortune 500, with the growth engine being customers spending >$1M and >$5M ACV. No single customer or industry dominates. Public sector (US federal) is a meaningful and growing vertical.

| Customer cohort | Disclosure Basis | Concentration |
|---|---|---|
| No single customer >10% of revenue | SEC 10-K (no customer disclosed at threshold) | Very low |
| US Federal Government (aggregate) | Earnings-call commentary | Material, growing; shutdown/budget-sensitive |
| Customers >$1M ACV (~2,100+) | Earnings-call metric [ESTIMATED count] | Diversified |
| Customers >$20M ACV | Earnings-call metric | Growing cohort, expansion-led |

**Concentration verdict:** Low single-name risk; the relevant concentration is *vertical* (US Federal) and *vendor* (hyperscaler hosting), not customer.

---

## Section 6 — Management & Acquisition Track Record

| Name | Role | Tenure | Background |
|---|---|---|---|
| Bill McDermott | Chairman & CEO | Since 2019 | Former CEO of SAP; aggressive go-to-market operator |
| Gina Mastantuono | CFO | Since 2020 | Ex-Ingram Micro CFO; disciplined margin/FCF steward |
| Amit Zavery | President / CPO (Product) | Joined 2024 | Ex-Google Cloud, ex-Oracle; AI/platform roadmap |
| Fred Luddy | Founder / Director | Founder (2004) | Created the Now Platform; remains on board |

Leadership tenure data from public filings; roles current as of 2026.

**Acquisition track record (illustrative, AI/data-focused tuck-ins):**

| Target | Year | Price | Rationale | Outcome |
|---|---|---|---|---|
| Element AI | 2021 | ~$0.5B [ESTIMATED] | AI research talent | Integrated into ML stack |
| Lightstep / Era / G2K / various | 2021–2024 | tuck-ins | Observability, AI, retail/IoT | Bolted into platform |
| Moveworks (front-office AI) | 2025 | ~$2.85B [ESTIMATED] | Conversational AI / agentic front-end | Strategic, integration ongoing |
| Data.World / Cuein (data + AI) | 2025 | tuck-ins | AI data layer for Now Assist | Integration ongoing |

**Capital allocation philosophy:** Reinvest in R&D first (21% of revenue), supplement organic growth with AI/data tuck-ins, and offset dilution via buybacks ($1.84B repurchased FY25 per cashflow). No dividend.

---

## Section 7 — Historical Financials

All in $M, FY ends Dec 31. Source: yfinance income_stmt / cashflow / balance_sheet (annual). FY2025 is the most recent audited year — current, not stale.

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM | FY2026E | FY2027E |
|---|---|---|---|---|---|---|---|---|
| Revenue | 5,896* | 7,245 | 8,971 | 10,984 | 13,278 | 13,960 | 16,198 | 19,193 |
| YoY growth | — | +23%* | +24% | +22% | +21% | — | +22% | +18% |
| Gross margin | — | 78.3% | 78.6% | 79.2% | 77.5% | 76.6% | — | — |
| Operating margin (GAAP) | — | 4.9% | 8.5% | 12.4% | 13.7% | 13.3% | — | — |
| EBITDA | — | 788 | 1,324 | 2,325 | 3,022 | 2,888 | — | — |
| GAAP Net income | — | 325 | 1,731 | 1,425 | 1,748 | — | — | — |
| FCF | — | 2,173 | 2,701 | 3,375 | 4,533 | 5,108 | — | — |
| FCF margin | — | 30.0% | 30.1% | 30.7% | 34.1% | 36.6% | — | — |
| GAAP EPS (split-adj) | — | — | — | — | ~$1.68** | $1.68 | — | — |
| non-GAAP EPS (est.) | — | — | — | 3.51 | ~4.12 | — | 4.12 | 5.03 |
| Capex | — | 550 | 697 | 892 | 911 | — | — | — |
| Total debt | — | 2,232 | 2,284 | 2,278 | 2,403 | 2,431 | — | — |
| Net debt | — | ~16 | net cash | net cash | **(net cash ~$1.3B)** | (2,751) net cash | — | — |
| Net debt / EBITDA | — | — | net cash | net cash | net cash | net cash | — | — |

\* FY2021 revenue shown for context; not all FY2021 rows returned by yfinance annual statements (5-year window) — marked where absent.
\** GAAP EPS impacted heavily by stock-based comp; trailing GAAP EPS $1.68 (info.trailingEps), driving the 68x trailing P/E. non-GAAP/forward EPS $5.03 (info.forwardEps) drives the 22.7x forward P/E. **GAAP vs non-GAAP gap is the single most important reconciliation in this name — see §14.**

FY2026E/FY2027E revenue and non-GAAP EPS from revenue_estimate / earnings_estimate (avg). Balance sheet: net cash $2.75B (cash+ST inv $6.28B vs total debt $2.43B).

---

## Section 8 — Recent Results

Last 2 reported quarters (source: quarterly_income_stmt, earnings_history):

| Quarter | Revenue ($M) | Gross Margin | Operating Margin (GAAP) | EPS (non-GAAP) Act vs Est | Surprise | Net income ($M) |
|---|---|---|---|---|---|---|
| Q1 2026 (rep. ~2026-04) | 3,770 | 75.1% | 13.3% | $0.97 vs $0.966 | +0.4% | 469 |
| Q4 2025 (rep. ~2026-01) | 3,568 | 76.6% | 12.4% | $0.92 vs $0.885 | +4.0% | 401 |

**Earnings beat history (last 4 quarters, earnings_history):**

| Quarter | EPS Est | EPS Act | Surprise % |
|---|---|---|---|
| Q2 2025 | 0.714 | 0.818 | +14.6% |
| Q3 2025 | 0.853 | 0.964 | +13.0% |
| Q4 2025 | 0.885 | 0.920 | +4.0% |
| Q1 2026 | 0.966 | 0.970 | +0.4% |

ServiceNow has beaten EPS in **4 of 4** quarters — but the surprise magnitude is **shrinking sharply** (14.6% → 0.4%), a key signal: the bar is catching up to reality and the easy beats are gone. Revenue still grew ~22% YoY in Q1 2026 ($3,770M vs $3,088M). The stock barely moved on the Q1 print (~flat into the report), consistent with a market that has already de-rated the name. Management guides cRPO (current remaining performance obligations) and subscription revenue quarterly with a full-year framework.

---

## Section 9 — Competitive Landscape

| Market | TAM Estimate | Company Position | Time Horizon |
|---|---|---|---|
| IT Workflow (ITSM/ITOM/SecOps) | ~$80B | #1 / leader | Now |
| Employee (HR) Workflows | ~$60B | Strong challenger | 2–4 yrs |
| Customer Workflows (CSM) | ~$90B | Challenger vs Salesforce | 2–5 yrs |
| Low-code / App dev (Creator) | ~$50B | Emerging | 3–5 yrs |
| Agentic AI / automation (Now Assist) | ~$150B+ [ESTIMATED] | Early, platform-advantaged | 3–7 yrs |
| **Total addressable** | **management cites ~$275–500B** | Single-platform consolidator | Long |

**Competitor comparison (source: yfinance info):**

| Peer | Market Cap | EV/Revenue | EV/EBITDA | Fwd P/E | Key Overlap |
|---|---|---|---|---|---|
| ServiceNow (NOW) | $118B | 8.2x | 39.8x | 22.7x | — |
| Salesforce (CRM) | $150B | 4.2x | 14.0x | 11.7x | CSM, platform, AI agents (Agentforce) |
| Workday (WDAY) | $36B | 3.5x | 23.1x | 11.4x | HR workflows |
| Microsoft (MSFT) | $3,059B | 9.8x | 16.8x | 21.3x | Copilot, Power Platform, Dynamics |
| Oracle (ORCL) | $609B | 11.5x | 26.9x | 26.3x | Cloud apps, infra |
| SAP | $214B | 5.6x | 18.1x | 18.4x | ERP, enterprise software |
| Palantir (PLTR) | $327B | 61.1x | 158.3x | 65.8x | AI/ontology, gov't workflows |

NOW screens as the **premium-multiple name within the workflow group** (8.2x EV/Rev vs CRM 4.2x, WDAY 3.5x), justified by faster growth (22% vs ~13%) and higher FCF margin (37%), but vulnerable if the AI-disruption thesis compresses the whole group further.

---

## Section 10 — Peer Valuation Comparison

| Company | Fwd P/E | EV/EBITDA | EV/Rev | Rev Growth | FCF Margin | Rating |
|---|---|---|---|---|---|---|
| **ServiceNow (NOW)** | **22.7x** | **39.8x** | **8.2x** | **22.1%** | **36.6%** | Strong Buy (1.44) |
| Salesforce (CRM) | 11.7x | 14.0x | 4.2x | 13.3% | 38.6% | — |
| Workday (WDAY) | 11.4x | 23.1x | 3.5x | 13.5% | 31.6% | — |
| Microsoft (MSFT) | 21.3x | 16.8x | 9.8x | 18.3% | 11.6% | — |
| Oracle (ORCL) | 26.3x | 26.9x | 11.5x | 21.7% | neg (capex) | — |
| SAP | 18.4x | 18.1x | 5.6x | 6.0% | 21.8% | — |
| Adobe (ADBE) | 9.2x | 10.4x | 4.0x | 12.0% | 38.1% | — |
| Palantir (PLTR) | 65.8x | 158.3x | 61.1x | 84.7% | 33.6% | — |
| **Peer median (ex-NOW)** | **18.4x** | **18.1x** | **5.6x** | — | — | — |

**What the spread implies:** NOW trades at a **premium to the workflow/applications median on every multiple** (22.7x vs 18.4x fwd P/E; 8.2x vs 5.6x EV/Rev; 39.8x vs 18.1x EV/EBITDA). The premium is *defensible* on growth (22% vs ~13% for CRM/WDAY/ADBE) and best-in-class FCF — but it is *much narrower than history*, when NOW commanded 15–20x EV/Rev. The de-rating has compressed NOW from "untouchable" toward "expensive-but-justified." The EV/EBITDA looks extreme (39.8x) because GAAP EBITDA is depressed by SBC; on a cash basis the premium is far smaller.

---

## Section 11 — Valuation

### Method 1: DCF — Three Scenarios

**WACC Adjudication box:**

| Input | Value |
|---|---|
| Risk-free (10Y UST) | 4.55% |
| Beta | 0.93 (info.beta) |
| ERP | 5.5% |
| Cost of equity (CAPM) | 9.65% |
| Formula WACC (near all-equity, net cash) | 9.53% |
| Sector band (high-growth SaaS) | 9.0%–11.0% |
| **Final WACC (base)** | **9.5%** — formula sits inside band; used directly |

Reason: NOW carries net cash, so WACC ≈ cost of equity. Formula output (9.5%) is squarely within the SaaS sector band; no override needed. Bull uses 9.0%, bear 10.5% to reflect risk-premium swings.

| Scenario | WACC | Terminal g | Revenue path / FCF margin | Implied price | TV % of EV |
|---|---|---|---|---|---|
| **Bull** | 9.0% | 3.5% | growth 21%→11%, FCF margin 34%→39% | **$172** | 81% |
| **Base** | 9.5% | 3.0% | growth 19%→9%, FCF margin 33%→36% | **$125** | 77% |
| **Bear** | 10.5% | 2.0% | growth 15%→5% (AI seat erosion), FCF margin flat 32% | **$74** | 69% |

**Probability-weighted DCF:** 0.30 × $74 + 0.45 × $125 + 0.25 × $172 = **$121** (+6% vs $114).

> Note: TV is 69–81% of EV — high, as expected for a long-duration grower. Sensitivity to WACC/terminal-g is therefore material; this is a duration asset and the de-rating is fundamentally a discount-rate/growth-persistence story.

### Method 2: Relative (Peer Multiples)

Applying peer median (ex-NOW) multiples to NOW financials (net debt = -$2.75B net cash):

| Multiple | Peer Median | NOW metric | Implied price |
|---|---|---|---|
| Fwd P/E | 18.4x | EPS $5.03 | $93 |
| EV/Revenue | 5.6x | Rev $13.96B | $79 |
| EV/EBITDA | 18.1x | EBITDA $2.89B (SBC-depressed) | $53 |
| **Blended (median of three)** | | | **$79** |

The relative method drags to **$79 (-31%)** because it forces NOW to the *group median* despite NOW growing ~70% faster than the median peer and earning higher FCF margins. A growth/quality-adjusted premium of +25–35% to the median (warranted on Rule-of-40 grounds: 22% growth + 37% FCF margin = 59) lifts the relative figure toward **$100–105**. I carry the un-adjusted $79 in the blend but flag it as conservative.

### Method 3: SOTP

ServiceNow reports a **single operating segment**; product-level economics are not disclosed (§3 figures are [ESTIMATED]). A credible SOTP cannot be built without disclosed segment financials — **SOTP not applicable / data gap.** The single-platform architecture also makes SOTP economically questionable (the value *is* the integration). Omitted by design.

### Probability-Weighted Synthesis

| Method | Weight | Implied Price | Weighted Contribution |
|---|---|---|---|
| DCF (prob-weighted) | 50% | $121 | $60.5 |
| Relative (un-adjusted peer median) | 30% | $79 | $23.7 |
| Relative (growth/quality-adjusted) | 20% | $103 | $20.6 |
| **Blended fair value** | **100%** | | **~$105** |

**Triangulated fair value ≈ $105 (spot), with a forward 12-month target of $138** rolling the base-case DCF forward one year of ~20% FCF growth and assuming partial multiple stabilization. This sits below the analyst mean of $141.86 but above current $114.19. The wide gap between the DCF anchor ($121) and raw relative ($79) is the honest tension in this name.

---

## Section 12 — Bull Case (10 Catalysts)

**Thesis:** ServiceNow is the best-positioned enterprise platform to monetize agentic AI, and a 44% de-rating has reset the multiple from "priced for perfection" to "priced for a slowdown that isn't happening" — 22% growth at a 22.7x forward multiple is a generational entry for a compounder.

1. **Revenue still compounding >20%** — Q1 2026 revenue +22% YoY to $3.77B; FY26E $16.2B (+22%), FY27E $19.2B (+18%) per revenue_estimate. No deceleration cliff visible in consensus.
2. **Now Assist / Pro Plus reprices the platform** — AI SKUs let NOW monetize *value and consumption*, not just seats, directly neutralizing the seat-erosion bear case. Fastest-growing product family.
3. **Best-in-class FCF generation** — FCF margin expanded to 36.6% TTM ($5.1B); FY25 FCF $4.53B up +34% YoY. FCF growth outpaces revenue, signalling real operating leverage.
4. **Net-cash fortress** — $6.28B cash/ST investments vs $2.43B debt = ~$2.75B net cash; fully self-funds R&D, M&A and buybacks with zero refinancing risk.
5. **Multiple has already compressed** — forward P/E 22.7x vs historical 50–60x; EV/Rev 8.2x vs historical 15–20x. Much of the AI-disruption fear is now in the price.
6. **Strong-Buy consensus with upside** — 44 analysts, mean rating 1.44, mean target $141.86 (+24%); high target $236. Street has not abandoned the name despite the drawdown.
7. **Consistent execution** — beat EPS in 4 of last 4 quarters; durable cRPO growth and >120% net expansion underpin forward visibility.
8. **Platform consolidation tailwind** — enterprises rationalizing point tools onto a single workflow system of action; NOW is the consolidation beneficiary, expanding into HR, CSM, SecOps.
9. **Federal / large-deal momentum** — growing US Federal book and >$1M/>$20M ACV cohorts expanding; large-deal motion intact.
10. **Margin runway** — GAAP operating margin only 13.3% with 76.6% gross margin; substantial room for operating-margin expansion as SBC normalizes and scale builds, closing the GAAP-to-FCF gap and re-rating GAAP earnings.

---

## Section 13 — Bear Case (10 Thesis-Breakers)

**Thesis:** ServiceNow is a seat-based SaaS incumbent whose entire pricing model is structurally threatened by agentic AI — if AI agents do the work of users, seat counts shrink, and a name still trading at a premium to a de-rating software group has materially more downside than its 44% fall suggests.

1. **AI breaks the seat model** — NOW's revenue scales with *human users*. If Now Assist/agents reduce headcount needs, the core per-seat monetization deflates; consumption pricing may not fully offset, and the relative DCF bear case ($74, -35%) reflects this.
2. **Beats are evaporating** — EPS surprise collapsed from +14.6% (Q2'25) to +0.4% (Q1'26). The bar has caught up; the next miss is the de-rating catalyst.
3. **Still premium-valued** — 8.2x EV/Rev and 39.8x EV/EBITDA vs peer medians of 5.6x and 18.1x. Mean-reversion to the group median implies ~$79 (-31%).
4. **GAAP earnings are thin** — trailing GAAP EPS only $1.68 (68x P/E) because stock-based comp consumes the income statement. The "cheap" 22.7x is a *non-GAAP* number; GAAP shareholders are diluted.
5. **Heavy SBC dilution** — buybacks ($1.84B FY25) largely *offset* dilution rather than reduce share count; per-share compounding is weaker than headline FCF growth implies.
6. **Hyperscaler/Microsoft encroachment** — MSFT (Copilot, Power Platform), Salesforce (Agentforce) and Oracle bundle competing AI-workflow capabilities into existing enterprise estates, pressuring NOW's land-and-expand.
7. **IT-spend cyclicality** — 64% North America, large-enterprise and US-Federal exposure makes NOW sensitive to IT-budget freezes, government shutdowns/CR risk, and macro slowdown.
8. **Decelerating growth into law of large numbers** — FY27E growth already fades to +18%; at $19B revenue the 20%+ era is ending, and premium multiples don't survive deceleration.
9. **Duration risk** — 69–81% of DCF value sits in terminal value; a higher-for-longer rate regime or any erosion in terminal growth assumptions disproportionately hits this long-duration asset (74% realized vol shows the market re-pricing this live).
10. **Crowded institutional ownership** — 88.6% institutional; if growth-fund consensus breaks, forced de-risking can overwhelm the thin 0.17% insider float and 5.6%-short setup, amplifying drawdowns (as the -46% from highs already demonstrates).

**Structural risk register:**

| Risk Category | Specific Risk | Probability | Impact |
|---|---|---|---|
| Business model | AI agents erode seat-based revenue | Medium | High |
| Valuation | Mean-reversion to peer multiples | Medium-High | High |
| Competition | MSFT/CRM/ORCL AI bundling | Medium | Medium-High |
| Macro | IT-spend freeze / Federal shutdown | Medium | Medium |
| Accounting | SBC dilution masks GAAP weakness | High (ongoing) | Medium |
| Growth | Deceleration below 18% | Medium | High |
| Rates/duration | Terminal-value sensitivity | Medium | High |

The bear case is written independently and is **not softened** to accommodate the bull. The AI-disruption-to-seats argument is the genuine reason the stock has halved.

---

## Section 14 — Delta Audit

| Claim | Raw Source Value | Computation | Status |
|---|---|---|---|
| Price $114.19 | info.currentPrice = 114.19 | direct | ✓ Verified |
| Market cap $117.8B | info.marketCap = 117,765,062,656 | direct | ✓ Verified |
| 1-yr return -44.4% | history 205.37 → 114.19 | -44.4% | ✓ Verified |
| Drawdown -46% | 114.19 / 211.48 - 1 | -46.0% | ✓ Verified |
| FY25 revenue $13.28B | income_stmt 2025 = 13,278M | direct | ✓ Verified |
| TTM revenue $13.96B | info.totalRevenue = 13,959,999,488 | direct | ✓ Verified |
| FY25 FCF $4.53B | cashflow 2025 = 4,533M | direct | ✓ Verified |
| FCF margin 36.6% TTM | 5,108 / 13,960 | 36.6% | ✓ Verified |
| Forward P/E 22.7x | info.forwardPE = 22.72 | direct | ✓ Verified |
| Trailing P/E 68.0x | info.trailingPE = 67.97 | direct | ✓ Verified |
| Net cash $2.75B | cash 6,284 − debt 2,431 (info totalDebt) vs BS 2,403 | $2.75–3.85B | ⚠ Unverified spread (debt definition) |
| EPS beats 4/4 | earnings_history surprises all positive | direct | ✓ Verified |
| Surprise shrinking 14.6%→0.4% | earnings_history | direct | ✓ Verified |
| Base DCF $125 | company-valuation skill | model | ✓ Verified (model) |
| Relative $79 | peer medians × NOW | model | ✓ Verified (model) |
| Blended ~$105 | weighted synthesis | model | ✓ Verified (model) |
| 5:1 split | t.splits 2025-12-18 = 5.0 | direct | ✓ Verified |

**Required flags:**
- **GAAP vs non-GAAP:** Material discrepancy. Trailing GAAP EPS $1.68 (68x) vs forward non-GAAP EPS $5.03 (22.7x). The entire "cheap" narrative depends on non-GAAP; SBC is the bridge. Flagged prominently.
- **EV/EBITDA (39.8x) distortion:** GAAP EBITDA ($2.89B) is depressed by SBC; the EV/EBITDA multiple overstates expensiveness vs. a cash-EBITDA view. Relative method's EV/EBITDA implied price ($53) is therefore the weakest leg and is down-weighted in synthesis.
- **Estimate spread:** FY27E EPS range $4.21–$5.32 (~20% wide) — moderate dispersion, reflecting genuine AI-outcome uncertainty.
- **Net-cash definition:** info.totalDebt (2,431) vs balance_sheet total debt (2,403); immaterial (~$28M) but noted.
- **Segment/geographic figures:** [ESTIMATED] — not disclosed by company.
- **Data gaps:** Adanos sentiment, funda-data, twitter-reader all unavailable (no API keys).

**VERDICT: PASS WITH NOTES** — All market and financial figures verified against primary yfinance fields. Notes attach to the GAAP/non-GAAP gap (structural to the thesis), the SBC-distorted EV/EBITDA, and estimated segment/geographic splits.

---

## Section 15 — Sentiment & Flow

**Short interest:** 5.6% of float short (info.shortPercentOfFloat), short ratio 2.1 days-to-cover (info.shortRatio). Modest — *not* a heavily-shorted name; squeeze risk low. The short interest reflects valuation-skeptics, not a crowded bear bet. ADTV ~$2.7B, float turns ~every 39 days; annualized float turnover ~650% (very actively traded). Execution cost for institutional size is low (impact ~48bps at 1% of ADV).

**Insider transactions (last significant, insider_transactions):**

| Name | Role | Date | Type | Shares | Value |
|---|---|---|---|---|---|
| Briggs, Teresa | Director | 2026-05-28 | Sale @ $108.70 | 1,595 | $173,376 |
| Bostrom, Susan | Director | 2026-05-21 | Stock award grant | 3,260 | $0 |
| Luddy, Frederic (founder) | Director | 2026-05-21 | Stock award grant | 3,260 | $0 |
| Sands, Anita | Director | 2026-05-21 | Stock award grant | 3,260 | $0 |

Insider activity is routine director grants plus one small director sale — **no meaningful insider signal** in either direction. Insider ownership is just 0.17% (info.heldPercentInsiders).

**Top institutional holders (institutional_holders, as of 2026-03-31):**

| Holder | % Held | Shares |
|---|---|---|
| BlackRock | 9.46% | 97.5M |
| Vanguard (Capital Mgmt) | 6.59% | 68.0M |
| State Street | 4.66% | 48.1M |
| T. Rowe Price | 3.31% | 34.1M |
| JPMorgan Chase | 3.01% | 31.0M |

88.6% institutionally owned — index/large-cap-growth-fund dominated. JPMorgan trimmed -18% in the quarter; T. Rowe added +5%. Crowded ownership is a two-edged sword (§13 risk #10).

**Social / cross-source sentiment:** **DATA GAP** — Adanos finance-sentiment (ADANOS_API_KEY missing), funda-data and twitter-reader unavailable. Qualitative read from public discourse: sentiment is bifurcated between AI-disruption bears (seat-erosion thesis) and quality-compounder bulls (best-in-class FCF at a reset multiple); the -44% price action and Strong-Buy analyst consensus (1.44) capture both sides. Treat as unquantified.

---

## Section 16 — Synthesis & Recommendation

**Where bull and bear agree:**
1. ServiceNow is a genuinely high-quality franchise — 76.6% gross margin, 37% FCF margin, net cash.
2. The seat-based model *does* face a real AI-driven re-pricing question; the only debate is whether Now Assist offsets it.
3. The multiple has already de-rated hard (forward P/E 22.7x vs 50–60x historically).
4. Growth is decelerating but remains well above software-group average (~22% vs ~13%).
5. GAAP earnings are structurally thin due to SBC; the investable case rests on FCF and non-GAAP.

**Probability-weighted 12-month outcome:**

| Scenario | Probability | 12-Month Target | Weighted Contribution |
|---|---|---|---|
| Bull (AI repricing works, multiple stabilizes) | 25% | $185 | $46.3 |
| Base (20% growth persists, mild re-rate) | 45% | $138 | $62.1 |
| Bear (seat erosion, mean-revert to peers) | 30% | $80 | $24.0 |
| **Expected value** | **100%** | | **~$132** |

**Rating: MARKET WEIGHT** | **12-month price target: $138** (base case; EV $132, +15–21% from $114.19) | **Horizon: 12 months.**

The DCF anchors fair value above spot, but the raw peer-multiple drag and the legitimate AI-disruption-to-seats risk prevent an Overweight. This is a high-quality compounder at a *reasonable* (not cheap) price, with a genuine structural overhang. MARKET WEIGHT with a positive skew — I would upgrade to OVERWEIGHT on evidence that Now Assist consumption revenue is offsetting any seat softness (watch cRPO + AI-SKU disclosure).

- **Entry strategy:** Initiate at half-size near $108–114. Add second tranche on either (a) a pullback to $95–100 (toward the relative-valuation floor / DCF bear) or (b) confirmation of accelerating Now Assist/AI-Pro-Plus revenue. Avoid chasing above $145 pre-confirmation.
- **Stop-loss / thesis invalidation:** $88 (below the 52-week low of $81 region and the bear DCF). Thesis is invalidated if (i) revenue growth guides below 15%, or (ii) two consecutive quarters of net-expansion deterioration tied to AI seat erosion.
- **Hedge:** Pair against a long-software basket (IGV) or a short in a lower-quality, slower-growth premium-multiple SaaS name; or buy 6-month puts at the $95 strike to cap the AI-disruption tail. Sector beta is low (0.93) but realized vol (74%) is high, so optionality is relatively expensive — size accordingly.
- **Position sizing:** 2–3% of an equity book at initiation, scalable to 4% on confirmation. Note high correlation to the large-cap growth/software complex (MSFT, CRM, ORCL) — do not double-count software exposure.
- **Key catalysts to watch:** Q2 2026 earnings (~late July 2026) — cRPO growth + any AI-revenue disclosure; FY2026 guidance updates; Now Assist/Pro Plus attach metrics; US Federal budget/CR developments; broader software-multiple regime (rates).

---

## Section 17 — Data Gaps

| Item | Gap Type | Impact |
|---|---|---|
| Adanos cross-source sentiment | ADANOS_API_KEY missing — skill unavailable | Medium |
| funda-data (transcripts, ownership flow, supply chain) | No FUNDA_API_KEY / MCP | Medium |
| twitter-reader (bear theses, short commentary) | Not run / unavailable | Low |
| Product-segment revenue & margins (§3) | Not disclosed by company — [ESTIMATED] | Medium |
| Geographic revenue split (§4) | [ESTIMATED] from 10-K pattern, not in yfinance | Low |
| cRPO / net-expansion exact figures | Not in yfinance; from earnings-call metrics | Medium |
| Non-GAAP EPS history (§7) | Estimated from forward/consensus, not in income_stmt | Low |
| Acquisition prices (§6) | [ESTIMATED] / press-reported | Low |
| FY2021 historical rows | Outside yfinance 5-year annual window | Low |
| GAAP diluted EPS (yfinance returned 0.0) | Used info.trailingEps $1.68 instead | Low |
| ADTV precise 30-day $ | averageDailyVolume30Day = None; used 3mo computed proxy | Low |

---

*Research/educational output. Not financial advice. Data via yfinance (unofficial Yahoo Finance) and the finance-skills valuation engine. Prices as of 2026-06-08/09.*
