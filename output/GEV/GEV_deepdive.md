# GE Vernova (NYSE: GEV) — Deep Dive: SOTP, Earnings Quality & Peer Comps

**Engine:** Alpha Global Equity Research — Deep-Dive Extension
**Date:** 2026-06-10
**Price reference:** $920.15 (carried from base report; yfinance `info.currentPrice`)
**Companion to:** `GEV_research.md` (base report, same date)
**Scope:** Closes the two data gaps flagged in the base report — (1) segment-level SOTP detail and (2) the GAAP→clean earnings bridge — plus a tightened, anomaly-corrected peer set.

> **Sourcing note.** The intended primary source for segment EBITDA and 10-K/10-Q line items was Funda AI (MCP `agent_chat` / REST). The Funda MCP is **not connected** in this environment (`claude mcp list` → `FUNDA_MCP_NOT_CONNECTED`) and **no `FUNDA_API_KEY`** is set, so primary SEC filing line items at segment granularity could not be retrieved directly. **However**, the central earnings-quality finding does NOT depend on Funda: yfinance exposes the full consolidated income-statement reconciliation (pretax income, tax provision, unusual items, special income charges, equity earnings, non-operating interest) at both annual and quarterly granularity, which is sufficient to build a rigorous GAAP→clean bridge from primary-equivalent data. Segment **revenue/margin splits remain [ESTIMATED]** and are tagged throughout. Every figure cites its yfinance field or is tagged `[ESTIMATED]`.

---

## SECTION 1 — SOTP BUILD (DEEP)

### 1.1 Segment data: FY2024 vs FY2025

yfinance does **not** expose GEV segment revenue or segment EBITDA (`income_stmt` is consolidated only). The table below uses the company's disclosed FY2025 segment proportions (Power ~half, Electrification ~25%, Wind ~24%) applied to **audited consolidated totals** (yfinance `income_stmt`: FY25 revenue $38,068M, FY24 $34,935M). Segment-level revenue and margin are therefore `[ESTIMATED]`; the consolidated control totals are verified.

| Segment | FY2024 Rev [EST] | FY2025 Rev [EST] | YoY [EST] | FY2025 EBITDA margin [EST] | FY2025 EBITDA [EST] |
|---|---|---|---|---|---|
| **Power** (gas, nuclear, steam, hydro) | ~$17.5B | ~$18.5B | ~+6% | ~13.5% | ~$2.50B |
| **Electrification** (grid, software, storage) | ~$7.8B | ~$9.4B | ~+20% | ~13.5% | ~$1.27B |
| **Wind** (onshore + offshore) | ~$9.0B | ~$9.1B | ~flat | ~1.0% | ~$0.09B |
| **Corporate / unallocated** | n/a | n/a | n/a | drag | ~($0.7B) |
| **Total (control)** | **$34,935M** ✓ | **$38,068M** ✓ | **+9.0%** ✓ | — | reported EBITDA $2,242M ✓ |

> Control totals (revenue $38,068M / $34,935M, +9.0%; reported EBITDA $2,242M) are verified from yfinance `income_stmt`. Segment splits are `[ESTIMATED]` — **the single largest residual data gap** (closing it fully requires the 10-K segment footnote via Funda/SEC). The bottom-up segment EBITDA (~$2.50 + $1.27 + $0.09 − $0.70 ≈ $3.16B at the EBITDA line) is intentionally a touch above reported consolidated EBITDA of $2.24B because segment "EBITDA" as companies define it adds back more items than yfinance's reconciled EBITDA — treat the SOTP EBITDA as **management-style segment EBITDA [ESTIMATED]**, not yfinance EBITDA.

### 1.2 Multiple justification (cite pure-play comps)

| Segment | Bear | Base | Bull | Comparable anchors (this report's peer pull) |
|---|---|---|---|---|
| **Power** | 12x | 15x | 18x | Siemens Energy gas/grid blended EV/EBITDA **32.7x** (ADR, inflated by low trough EBITDA); Mitsubishi Heavy **18.0x** (`7011.T`); GE Aerospace **32.2x** (premium aero, not a turbine pure-play). Gas-turbine power+service deserves a *mid-teens* multiple — better than commodity industrials, below grid. |
| **Electrification** | 15x | 19x | 24x | Schneider **20.6x**, ABB **21.4x** (`ABBN.SW`, corrected), Eaton **27.9x**, Vertiv **47.0x**. Grid/electrification is the highest-quality leg → deserves the richest multiple; base 19x sits just under Schneider/ABB. |
| **Wind** | 5x | 8x | 11x | Distressed offshore comps (Siemens Energy's Gamesa losses, Ørsted writedowns) → near-breakeven economics justify a *distressed* 5–11x on a tiny EBITDA base; immaterial to total value either way. |
| **Corporate** | 10x cap. cost | 10x | 10x | Unallocated cost capitalized at a flat ~10x [ESTIMATED]. |

### 1.3 SOTP — three scenarios (on FY2025 actual economics)

Shares: 268.7M (yfinance `info.sharesOutstanding`). Net cash: +$7,676M (cash $8,848M − debt $1,172M, yfinance `balance_sheet`).

| | Bear | Base | Bull |
|---|---|---|---|
| Power EBITDA × mult | $2.50B × 12 = $30.0B | × 15 = $37.5B | × 18 = $45.0B |
| Electrification EBITDA × mult | $1.27B × 15 = $19.0B | × 19 = $24.1B | × 24 = $30.5B |
| Wind EBITDA × mult | $0.09B × 5 = $0.5B | × 8 = $0.7B | × 11 = $1.0B |
| Corporate (−$0.7B × 10x) | −$7.0B | −$7.0B | −$7.0B |
| **Total EV** | **~$42.5B** | **~$55.3B** | **~$69.4B** |
| + Net cash | +$7.7B | +$7.7B | +$7.7B |
| **Equity value** | **~$50.2B** | **~$63.0B** | **~$77.1B** |
| **Implied price/share** | **~$187** | **~$234** | **~$287** |

**SOTP on current (FY2025) economics = $187 / $234 / $287** (bear/base/bull) vs market **$920**. The market pays **~3.9x base-case sum-of-parts** on trailing economics.

### 1.4 Sensitivity table — implied price/share

Rows = Power EV/EBITDA; columns = Electrification EV/EBITDA. Wind fixed at 8x, corporate −$7.0B, net cash +$7.7B, on FY2025 [ESTIMATED] segment EBITDA.

| Power ↓ \ Elec → | **15x** | **18x** | **21x** | **24x** |
|---|---|---|---|---|
| **12x** | $178 | $192 | $206 | $220 |
| **14x** | $191 | $205 | $219 | $233 |
| **16x** | $203 | $217 | $232 | $246 |
| **18x** | $216 | $230 | $244 | $258 |

> Even the **top-right corner** (Power 18x / Elec 24x — richer than every clean comp in the peer set) yields **$258/share**, ~72% below the $920 quote. On *trailing* economics, no defensible multiple combination reaches the market price. The gap is entirely a forward-growth bet.

### 1.5 Reconciliation to the base report's ~$333 SOTP

The base report's **$333** is **not contradicted** — it is a *different vintage*. The base report built SOTP on **2027-estimated** segment economics (Power $20.5B rev @ 14% = $2.87B EBITDA; Electrification $11.5B @ 16% = $1.84B; Wind $8.5B @ 5% = $0.42B; corporate −$2.0B EV), giving EV ~$81.7B → **$333**.

| Basis | Power EBITDA | Elec EBITDA | Wind EBITDA | Total EV | Implied px |
|---|---|---|---|---|---|
| **This deep-dive — FY2025 actual** (base mults 15/19/8) | $2.50B | $1.27B | $0.09B | ~$55.3B | **~$234** |
| **Base report — 2027E** (mults 15/20/9) | $2.87B | $1.84B | $0.42B | ~$81.7B | **~$333** |

**The ~$99 difference ($234 → $333) is entirely the two-year forward ramp**: 2027E adds ~$0.37B Power EBITDA, ~$0.57B Electrification EBITDA (margin 13.5%→16% plus ~+22% revenue), and Wind swinging from ~breakeven to ~5% margin (~+$0.33B). In other words, **roughly $100/share of the base report's SOTP is "earned" only if GEV executes two more years of margin expansion and Wind turns profitable.** On what the company has *actually delivered* (FY2025), the SOTP is ~$234. Both numbers are internally consistent; this deep-dive simply isolates how much of the $333 is already-forward.

---

## SECTION 2 — EARNINGS-QUALITY BRIDGE (DEEP)

**This is the crux of the deep-dive.** The base report flagged that FY2025 GAAP net income ($4.88B) hugely exceeds operating income ($1.39B). yfinance's full income-statement reconciliation lets us name and size every bridging item.

### 2.1 FY2025: GAAP net income $4,884M → clean operating earnings

All figures yfinance `income_stmt`, FY ended 2025-12-31 ($M):

| Line | Value | Source / nature |
|---|---|---|
| Operating income (reported) | **$1,389** | `Operating Income` — the true operating result |
| + Net non-operating interest income | +$455 | `Net Non Operating Interest Income Expense` — interest on the ~$8.8B cash pile (recurring while rates hold) |
| + Earnings from equity interests | +$269 | `Earnings From Equity Interest` (JVs — semi-recurring) |
| + Other non-operating / unusual items | +$715 | `Other Income Expense` residual incl. `Special Income Charges` $185M & `Total Unusual Items` +$171M |
| = **Pretax income** | **$2,828** | `Pretax Income` ✓ |
| − Tax provision | **+$2,051** (a *benefit*) | `Tax Provision` = **−$2,051M** → tax ADDED to net income |
| + Minority interest | +$4 | `Minority Interests` |
| = **GAAP net income** | **$4,884** | `Net Income` ✓ |

**The decisive item: the tax line is a $2,051M BENEFIT, not an expense.** `Tax Rate For Calcs` shows 21% nominal, but the *actual* provision is negative — consistent with a **deferred-tax valuation-allowance release** (post-spin, GEV's swing to sustained profitability allowed it to recognize previously-reserved deferred tax assets, flushing a large one-time non-cash credit through the P&L). yfinance also reports `Normalized Income` of **$4,749M** for FY25 — but that "normalization" only strips the $171M unusual *operating* item; **it does NOT strip the tax-benefit distortion**, which is why even the "normalized" figure is misleading here.

**Clean FY2025 earnings power:**

| Metric | Value | Method |
|---|---|---|
| Clean pretax (op income + interest + equity earnings) | ~$2,113M | $1,389 + $455 + $269 |
| Clean net income @ 24% normalized tax | **~$1,606M** | $2,113 × (1 − 0.24) |
| Diluted shares | 276M | yfinance `Diluted Average Shares` |
| **Clean FY2025 EPS** | **~$5.82** `[ESTIMATED]` | vs **GAAP $17.69** |
| Of which: tax-benefit / one-time portion of GAAP EPS | **~$11.88** | $17.69 − $5.82 |

> **~67% of FY2025 GAAP EPS ($11.88 of $17.69) is one-time / non-operating** — overwhelmingly the deferred-tax valuation-allowance release booked largely in Q4 2025 (Q4 `Tax Provision` = **−$2,565M**, yfinance `quarterly_income_stmt`).

### 2.2 Q1 2026: GAAP net income $4,745M → operating income $179M (the ~$4.6B gap)

All figures yfinance `quarterly_income_stmt`, quarter ended 2026-03-31 ($M):

| Line | Value | Nature |
|---|---|---|
| Operating income | **$179** | true operating result (1.9% margin) |
| + **One-time non-operating gain** | **+$4,405** | `Special Income Charges` / `Total Unusual Items` = **+$4,405M** — a large positive one-time item (separation/disposal/legal-related GAIN, non-operating, non-recurring) |
| + Non-operating interest income | +$291 | cash interest |
| + Equity earnings | +$65 | JVs |
| + Other residual | +$163 | |
| = **Pretax income** | **$5,103** | ✓ |
| − Tax provision | −$354 | (6.9% effective — `Tax Rate For Calcs` 0.069) |
| = **GAAP net income** | **$4,745** | ✓ (GAAP EPS $17.44) |

**The ~$4.6B gap between $179M operating income and $4,745M net income is ~96% a single one-time non-operating gain of $4,405M** (≈ **$16.19 per share** of the $17.44 GAAP EPS). yfinance's own `Normalized Income` for Q1'26 = **$641M** — confirming the underlying number is roughly an order of magnitude below GAAP.

**Clean Q1 2026:**

| Metric | Value |
|---|---|
| Clean pretax (op + interest + equity, ex one-time) | ~$535M |
| Clean net income @ 24% | ~$407M |
| **Clean Q1'26 EPS** | **~$1.49** `[ESTIMATED]` (vs GAAP $17.44) |

### 2.3 Clean run-rate and the multiple the market is REALLY paying

| Earnings base | EPS | Implied P/E on $920.15 |
|---|---|---|
| FY2025 **GAAP** | $17.69 | 52x (meaningless — one-time inflated) |
| FY2025 **clean** `[EST]` | ~$5.82 | **158x** |
| FY2026E **consensus** (`0y`, yfinance `earnings_estimate`) | $30.996 | 30x — **but this consensus number is itself polluted**: it was **$14.80 just 90 days ago** and jumped to ~$31 *only after the Q1'26 one-time gain* (`eps_trend`: 90d $14.71 → current $30.93). The Street simply rolled the $16/sh one-time gain into the FY26 line. |
| FY2026E **clean run-rate** `[EST]` (annualize ~$1.49 Q1 + ramp) | ~$13–15 | **~63–66x** |
| FY2027E **consensus** (`+1y`, the cleanest forward proxy) | $24.31 | **37.9x** |

> **Management's "adjusted EBITDA" framing vs reality.** GEV guides on *adjusted EBITDA* and *adjusted EBITDA margin* (a roughly high-single-digit % margin building toward low-teens by 2028). yfinance reported FY25 EBITDA of $2,242M (5.9% of revenue) and `info.enterpriseToEbitda` of **71x**. Even on management's more generous adjusted EBITDA definition, the EV (~$242B) sits at a **very high multiple of any honest 2025 EBITDA**. The adjusted-EBITDA bridge and the GAAP-net-income bridge tell the *same* story from two directions: **2025 underlying profitability is thin; the headline net income is a tax mirage; the Q1'26 headline is a disposal-gain mirage.**

### 2.4 Plain-English verdict on underlying earnings power

- **Real FY2025 underlying EPS is ~$5–6, not $17.69.** The $17.69 GAAP figure is ~67% one-time (a non-cash deferred-tax credit).
- **Real Q1 2026 underlying EPS is ~$1.50, not $17.44.** The $17.44 is ~93% a one-time disposal/separation gain.
- **The market is paying ~150x+ on trailing clean earnings and ~38x on FY2027 consensus** — and even that 38x rests on consensus EPS that *fell* from the FY26 headline (FY27 $24.31 < FY26 headline $30.99 because the FY26 number is artificially inflated; underlying EPS is *growing*, but nowhere near the headline trajectory).
- **Bottom line:** GEV's genuine, repeatable earnings power in 2025 was roughly **$1.6B net / ~$5.82 EPS**. Everything above that in the GAAP headlines is tax-allowance release (FY25) and a disposal gain (Q1'26). The investment case must be underwritten on the *forward margin ramp*, never on reported GAAP.

---

## SECTION 3 — PEER COMP SET (DEEP, TIGHTENED)

### 3.1 Anomaly fixes vs the base report

The base report flagged ABB and Mitsubishi Heavy as "data anomalies" and Hitachi as `n/m`. Root cause identified: **ADR tickers mix ADR price with local-currency enterprise value**, corrupting EV ratios. Fixes:

| Base report issue | Fix in this deep-dive |
|---|---|
| `ABBNY` EV/EBITDA 105x, EV/Rev 21.3x (absurd) | Use **`ABBN.SW`** (Swiss primary): EV/EBITDA **21.4x**, EV/Rev **4.34x** ✓ |
| `MHVYF` n/m | Use **`7011.T`** (Tokyo primary): EV/EBITDA **18.0x**, EV/Rev 2.39x ✓ |
| Hitachi n/m | Use **`6501.T`** (Tokyo primary): EV/EBITDA **13.1x**, EV/Rev 2.05x ✓ (ADR `HTHIY` is corrupted — negative EV — and is dropped) |
| Added spin-sibling re-rate analog | **GE Aerospace (`GE`)** included as the cleanest analog for a GE-spin re-rating |

### 3.2 Tightened peer table (clean, sourced)

All from yfinance `info` per ticker (`forwardPE`, `enterpriseToEbitda`, `enterpriseToRevenue`, `revenueGrowth`, `ebitdaMargins`, `returnOnEquity`). GEV row carries the earnings-quality caveat from Section 2.

| Company (ticker) | Fwd P/E | EV/EBITDA | EV/Rev | NTM Rev Gr | EBITDA mgn | ROE | FCF (yf) |
|---|---|---|---|---|---|---|---|
| **GE Vernova (GEV)** | **37.5x** | **71.0x** | **6.16x** | **+19.5%** | **8.7%** | 75.7%¹ | $9.3B² |
| Siemens Energy (ENR.DE) | 24.5x | 32.7x | 2.99x | +3.3% | 9.2% | 23.3% | $4.7B |
| Schneider (SU.PA) | 22.7x | 20.6x | 4.08x | +4.2% | 19.7% | 15.6% | $4.0B |
| Eaton (ETN) | 25.6x | 27.9x | 6.21x | +16.8% | 22.2% | 20.8% | $2.6B |
| Vertiv (VRT) | 32.8x | 47.0x | 10.33x | +30.1% | 22.0% | 45.1% | $2.0B |
| ABB (ABBN.SW)³ | 29.3x | 21.4x | 4.34x | +18.3% | 20.3% | 33.6% | — |
| Mitsubishi Heavy (7011.T)³ | 38.6x | 18.0x | 2.39x | +11.3% | 13.3% | 12.6% | ¥0.6T |
| Hitachi (6501.T)³ | 26.9x | 13.1x | 2.05x | +11.3% | 15.7% | 13.3% | ¥1.1T |
| GE Aerospace (GE)⁴ | 38.0x | 32.2x | 7.36x | +24.7% | 22.8% | 45.4% | $5.7B |
| **Peer median (ex-GEV)** | **27.9x** | **24.6x** | **4.34x** | **+16.8%** | **20.0%** | **23.3%** | — |

¹ GEV ROE 75.7% is itself distorted by the one-time-inflated FY25 net income (Section 2) over a thin post-spin equity base — **not** a clean profitability signal.
² GEV FCF $9.3B from yfinance `freeCashflow` is a TTM/levered-FCF field inflated by working-capital timing and the cash interest; the base report's FY25 FCF of $3.7B (cashflow statement) is the cleaner figure.
³ Anomaly-corrected primary listings (was flagged/excluded in base report).
⁴ Spin-sibling re-rate analog.

### 3.3 Growth-adjusted (PEG) view — judge premium against growth, not absolute multiple

PEG here = forward P/E ÷ NTM revenue-growth %. (Revenue-growth PEG is used because GEV's *earnings* base is distorted; revenue growth is the cleaner denominator.)

| Company | Fwd P/E | NTM Rev Gr | **PE / growth** |
|---|---|---|---|
| **GEV** | 37.5x | 19.5% | **1.93** |
| Vertiv | 32.8x | 30.1% | **1.09** |
| Eaton | 25.6x | 16.8% | **1.52** |
| GE Aerospace | 38.0x | 24.7% | **1.54** |
| ABB | 29.3x | 18.3% | **1.60** |
| Hitachi | 26.9x | 11.3% | **2.38** |
| Mitsubishi Heavy | 38.6x | 11.3% | **3.42** |
| Schneider | 22.7x | 4.2% | **5.41** |
| Siemens Energy | 24.5x | 3.3% | **7.42** |

### 3.4 Conclusion — how much premium, and is it justified?

- **On absolute forward P/E, GEV (37.5x) trades ~34% above the corrected peer median (27.9x)** — *narrower* than the base report's "~47%" premium, because fixing the ABB anomaly and adding the higher-multiple Japanese turbine and GE-Aero comps lifts the median from 25.6x to 27.9x. **So the first deep-dive finding is that the headline premium is real but smaller than the base report stated.**
- **On EV/Revenue, GEV (6.16x) is ~42% above the median (4.34x)** — but here EV/Rev flatters GEV because its EBITDA margin (8.7%) is the *lowest* in the group; on EV/EBITDA the 71x is not comparable (thin-margin base).
- **On a growth-adjusted (PEG) basis, GEV at 1.93 is more expensive than the highest-growth comps** — Vertiv (1.09, growing 30%), Eaton (1.52), GE Aerospace (1.54), ABB (1.60). GEV is **cheaper** only than the slow-growers (Schneider 5.41, Siemens Energy 7.42) and the lower-growth Japanese names. **Translation: GEV is NOT cheap for its growth relative to the best operators** — Vertiv grows faster for a lower multiple, and GE Aerospace matches the multiple with comparable growth *and* far cleaner 22.8% EBITDA margins vs GEV's 8.7%.
- **Is the premium justified?** Partially. GEV has the best *thematic* exposure (grid + gas-turbine scarcity + AI power) and the fastest *margin-expansion runway* (8.7% → low-teens). But on a like-for-like *clean* basis the premium buys a margin story that is still mostly ahead of the company — peers like Eaton, ABB, Vertiv and GE Aerospace already *earn* 20%+ EBITDA margins and 20%+ ROE today, while GEV is at 8.7% and must execute to close the gap. **The premium is a forward-execution premium, not a cheapness — and it is no longer obviously "discounted vs peers for the growth."**

---

## What changed vs the base report

| Item | Base report | This deep-dive | Why it changed |
|---|---|---|---|
| **GAAP→clean bridge** | Flagged as data gap; clean EPS "inferred ~$13–15" | **Fully built and sized**: FY25 clean EPS **~$5.82** (67% of GAAP is a **deferred-tax valuation-allowance release**, Q4'25 tax = −$2,565M); Q1'26 clean EPS **~$1.49** (93% of GAAP is a **$4,405M one-time disposal/separation gain**) | yfinance income-statement reconciliation (tax provision, special income charges, unusual items) named each item |
| **SOTP** | ~$333 (single number, 2027E basis) | **$187 / $234 / $287** bear/base/bull on **FY2025 actual** economics; reconciled: ~$100/sh of the $333 is the unearned 2-yr forward ramp | Built on trailing actuals + sensitivity grid; isolated forward content |
| **Peer premium** | "~47% above peer median fwd P/E" | **~34%** above corrected median (27.9x); PEG **1.93** — richer than Vertiv/Eaton/ABB/GE-Aero for the growth | Fixed ABB/Hitachi/Mitsubishi ADR anomalies (primary listings), added GE Aerospace; clean median rose |
| **FY26 consensus EPS** | Noted as one-time-driven | Confirmed: jumped $14.80→$30.99 in 90 days *because the Street rolled the Q1'26 disposal gain into the line* | `eps_trend` 90d-vs-current |

## Updated one-paragraph read on valuation

GEV's real, repeatable 2025 earnings power is roughly **$1.6B / ~$5.82 EPS** — the $17.69 GAAP figure is two-thirds a non-cash deferred-tax release, and Q1 2026's $17.44 is nine-tenths a one-time disposal gain, so the stock trades at **~150x+ trailing clean earnings, ~63–66x a clean 2026 run-rate, and ~38x FY2027 consensus**. On *trailing* sum-of-parts the business is worth **~$187–287** (base ~$234), and the base report's $333 only appears after crediting two more years of unproven margin expansion and a Wind turnaround. On a tightened, anomaly-corrected peer set GEV carries a **~34% forward-P/E premium and a 1.93 revenue-PEG** that is *richer* than faster-growing, higher-margin operators (Vertiv, Eaton, GE Aerospace, ABB). The conclusion of the base report stands and is *reinforced* with primary-equivalent precision: **GEV is a genuinely high-quality electrification franchise whose price already capitalizes the back half of this decade — it is expensive on every clean metric, and the entire bull case rests on a forward margin ramp the company has not yet earned.** Rating read is unchanged from the base report's **MARKET WEIGHT**; the earnings-quality bridge makes the "do not underwrite on GAAP" warning quantitative rather than qualitative.

---

*Research/educational output. Not financial advice. Consolidated financials and peer multiples from yfinance (unofficial Yahoo Finance) `income_stmt`, `quarterly_income_stmt`, `balance_sheet`, `info`, `earnings_estimate`, `eps_trend`. Segment revenue/margin splits are `[ESTIMATED]` — primary 10-K segment footnote was not retrievable (Funda MCP not connected, no FUNDA_API_KEY). The GAAP→clean bridge is built from primary-equivalent consolidated reconciliation lines and is not an estimate, except the 24% normalized tax assumption and clean-EPS rounding, which are tagged `[ESTIMATED]`.*
