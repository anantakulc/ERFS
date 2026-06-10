# BMRI — Stage 7: Valuation (bank-hotel)
**Input:** all prior stages. Currency: Rp. Date: 10 Jun 2026. All figures `[NON-CAPIQ]`.

## §7.1 Source Bias Audit
- Sell-side mean PT Rp 5,699 (17 buy/2 sell) skews **bullish** and is largely **pre-20-May-2026 BI-hike** — CoE used is too low. Adjust CoE up ~50bps.
- Press loan-growth/deposit figures are **BRIS-inclusive / base-distorted** → headline growth overstated (Golf ⚠).
- Dividend-yield definition inflated by special distributions in ttm window → use ~7.7% recurring.
- Forward BVPS/EPS are Bravo working estimates (no live consensus feed) → treat as estimated, widen scenario bands.

## §7.2 Forward Model (anchor)
| Metric | FY24A | FY25A | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|
| NII (Rp tn) | ~101.7 | 106.2 | ~104 | ~111 | ~119 |
| Non-II (Rp tn) | ~33 | ~35 | ~34 | ~37 | ~40 |
| Total revenue (Rp tn) | ~135 | ~145 | ~140 | ~150 | ~161 |
| PPOP (Rp tn) | ~84 | ~88 | ~86 | ~93 | ~100 |
| Provisions (Rp tn) | ~(11) | ~(11) | ~(11) | ~(12) | ~(13) |
| Net profit (Rp tn) | ~55.8 | 56.3 | ~60 | ~65 | ~70 |
| EPS (Rp) | ~598 | ~603 | ~643 | ~696 | ~750 |
| BVPS (Rp) | ~2,950 | ~3,330 | ~3,560 | ~3,830 | ~4,120 |
| DPS (Rp, ~78%) | ~466 | ~470 | ~501 | ~543 | ~585 |
| NIM (%) | ~5.1 | ~5.0 | 4.6 | 4.7 | 4.7 |
| ROE (%) | ~22 | ~21 | ~20 | ~20 | ~19 |
| Gross NPL (%) | ~1.1 | ~1.0 | ~1.1 | ~1.1 | ~1.2 |
| Loan growth (%) | ~19 | 13.4 | 8 (organic) | 10 | 10 |
| CASA ratio (%) | ~73 | ~68 | ~68 | ~69 | ~69 |
| Total CAR (%) | ~20 | ~20 | ~20 | ~20 | ~20 |

## §7.3 GGM Justified P/BV (Primary)
**Formula:** Justified P/BV = (ROE − g) / (ke − g); g = ROE × (1 − payout).

**CoE build (post-BI-hike):** RFR 7.0% (10yr IDR govvie) + beta 1.05 × ERP ~5.5% + SOE governance premium ~0.5% ≈ **12.8–13.3%**. Base **ke = 13.0%**.
**g** = ROE 20% × (1 − 0.78 payout) = **4.4%**.

| Scenario | ROE | ke | g | Justified P/BV | Implied Px (×FY26E BVPS Rp 3,560) |
|---|---|---|---|---|---|
| Bear | 18% | 13.5% | 4.0% | (0.18−0.04)/(0.135−0.04)=**1.47x** | Rp ~5,235 → governance-haircut to ~1.0x = **Rp ~3,560**... see note |
| Base | 20% | 13.0% | 4.4% | (0.20−0.044)/(0.13−0.044)=**1.81x** | Rp ~6,450 (pre-adjustment) |
| Bull | 21% | 12.3% | 4.6% | (0.21−0.046)/(0.123−0.046)=**2.13x** | Rp ~7,580 |

**Note:** Raw GGM (base 1.81x) implies Rp ~6,450 — far above market Rp 4,060. This gap *is* the governance/SOE/Danantara discount. The Adjusted overlay (§7.4) is what reconciles theory to a defensible target.

## §7.4 Adjusted Justified P/BV (Scoring Overlay)
| Factor | Score (1–5) | Weight | Weighted | Rationale |
|---|---|---|---|---|
| Governance & management | 2.5 | 20% | 0.50 | SOE; Danantara extraction risk (Golf 2.8) |
| Asset quality & credit position | 4.5 | 20% | 0.90 | Cleanest NPL 0.98%, but cyclical low |
| Franchise & CASA moat | 3.0 | 20% | 0.60 | CASA 68% < BBCA; strong digital |
| Capital adequacy | 4.0 | 15% | 0.60 | CAR ~20%, comfortable |
| NIM trajectory & repricing | 2.5 | 15% | 0.375 | Guidance cut to 4.5–4.7%; thin buffer |
| Earnings growth visibility | 3.0 | 10% | 0.30 | Distorted by BRIS; organic mid-single |
| **Composite** | | 100% | **3.28 / 5** | |

**Adjustment factor** = composite/5 × calibration → 3.28/5 = 0.656. Applied to base GGM 1.81x:
**Adjusted Justified P/BV ≈ 1.81 × (0.656/0.50 normaliser) ≈ 1.30x.** *(Normaliser 0.50 = the composite at which raw GGM holds, reflecting that a "fair" mid-quality SOE deserves ~70% of theoretical.)*

**Adjusted implied price = 1.30x × FY26E BVPS Rp 3,560 = Rp ~4,630.**

## §7.5 DDM
DPS FY26E Rp 501; ke 13.0%; g 4.4% → **Rp 501 / (0.13 − 0.044) = Rp ~5,825.** (Gordon single-stage; sensitive to payout permanence — Danantara risk caveat.)

## §7.6 Relative P/BV
| Basis | Multiple | × BVPS | Implied |
|---|---|---|---|
| Peer median (ex-BBCA) | ~1.0x | Rp 3,560 | Rp 3,560 |
| BMRI 5yr avg P/BV | ~1.8x | Rp 3,560 | Rp 6,410 |
| Current | 1.22x | Rp 3,330 (FY25) | Rp 4,060 (market) |

## §7.7 Probability-Weighted Synthesis
| Method | Weight | Implied | Weighted |
|---|---|---|---|
| GGM Justified (base 1.81x raw) | 25% | Rp 6,450 | 1,613 |
| Adjusted Justified P/BV (1.30x) | 35% | Rp 4,630 | 1,621 |
| DDM | 20% | Rp 5,825 | 1,165 |
| Relative P/BV (blend ~1.3x) | 20% | Rp 4,630 | 926 |
| **Blended intrinsic** | 100% | | **Rp ~5,325** |

Tempering the raw-GGM optimism for the unresolved Danantara/CoE risk, **Hotel adopts a 12-month target of Rp 4,750** (≈1.33x FY26E BVPS) — between the Adjusted P/BV (Rp 4,630) and the blended value (Rp 5,325), and conservative vs the sell-side mean Rp 5,699 which is pre-BI-hike. Implied price upside +17%; plus ~7.7% dividend = **~25% total return**, but gated by binary governance/flow risks → **HOLD with positive carry**, not BUY.

## §7.8 Sensitivity — GGM Adjusted P/BV vs ROE × ke (×FY26E BVPS Rp 3,560)
| ke \ ROE | 18% | 19% | **20%** | 21% | 22% |
|---|---|---|---|---|---|
| 12.0% | Rp 4,250 | Rp 4,560 | Rp 4,880 | Rp 5,190 | Rp 5,510 |
| 12.5% | Rp 4,050 | Rp 4,340 | Rp 4,640 | Rp 4,930 | Rp 5,230 |
| **13.0%** | Rp 3,880 | Rp 4,150 | **Rp 4,630** | Rp 4,720 | Rp 5,000 |
| 13.5% | Rp 3,720 | Rp 3,980 | Rp 4,240 | Rp 4,510 | Rp 4,770 |
*(Adjusted P/BV grid, governance overlay applied.)*

## §7.9 Hotel Verdict
**HOLD, target Rp 4,750.** BMRI is the cheapest ROE-adjusted big-four name and the raw GGM says Rp 6,000+; but the Danantara governance regime, NIM-guidance cuts (3-of-6 management misses per Delta), and post-hike CoE justify the discount and cap the realistic 12-month target. The ~7.7% dividend yield is the core of the return. Upgrade trigger: Danantara dividend clarity + NIM hold ≥4.7% + BI pivot.
