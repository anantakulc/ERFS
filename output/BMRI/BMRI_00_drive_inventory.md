# BMRI — Stage 0 Drive Inventory & Data Sourcing Log
**Orchestrator:** Alpha | **Date:** 10 June 2026 | **Ticker:** BMRI.JK (PT Bank Mandiri (Persero) Tbk) | **Country:** Indonesia (IDX, OJK, Bank Indonesia)

## Data Engine Availability Check (Hard Rule 6)

| Source | Status | Action |
|---|---|---|
| S&P Capital IQ MCP (`S_P_Global`) | **`[CAPIQ UNAVAILABLE]`** — requires interactive OAuth callback that cannot be completed in this remote session | Fall back to Tier-1 chain. Every figure marked `[NON-CAPIQ: <source>]` |
| Google Drive ticker folder (`search_files`/`read_file_content`) | **Not provisioned** in this environment — no Drive MCP tool exposed | Local repo `output/` used as workspace; primary data via WebSearch/WebFetch fallback chain |
| Company IR (bankmandiri.co.id/en/web/ir) | Available (WebFetch) | Used for FY25/1Q26 cross-check |
| IDX / exchange filings | Available via aggregators | Used |
| WebSearch (date-filtered) | Available | Primary fallback |

**Conclusion:** Capital IQ is unavailable. Per fallback order, primary data is sourced from (a) Indonesian financial press and IR-derived aggregators, (b) company IR, (c) broker note summaries, (d) date-filtered WebSearch. All financial figures below and downstream are tagged `[NON-CAPIQ]`. Golf (§6.4) audits these; Hotel (§7.1) bias-audits sources.

## Comparable Precedent
`output/BBCA/BBCA_research.md` (Bank Central Asia, 8 Jun 2026) — same Indonesian banking framework, GGM/DDM valuation, Rupiah conventions, identical macro cycle (IDR record low, BI hike 20 May 2026 to 5.25%, MSCI EM/Frontier risk, Fitch Negative outlook, Prabowo populist policy). Macro and sector-wide data points carried forward and applied to BMRI where sector-common.

## Selected Source Batch (15 documents prioritised; transcripts/IR/broker)

| # | Document | Type | Date | Access |
|---|---|---|---|---|
| 1 | BMRI 1Q26 Results — net profit Rp15.4tn (+16.6%), post-BRIS deconsolidation | Earnings/press (IDNFinancials, Tempo, Databoks) | Apr 2026 | Read |
| 2 | Samuel Sekuritas — BMRI 1Q26 Results note | Broker | 28 Apr 2026 | 403-blocked; summary triangulated |
| 3 | BRI Danareksa (BRIDS) — BMRI 22 Apr 2026 note | Broker | 22 Apr 2026 | 403-blocked; summary triangulated |
| 4 | IndoPremier — "BMRI 1Q26: beat from strong NII/PPOP and lower CoC" | Broker | Apr 2026 | Read (summary) |
| 5 | Jakarta Globe — "Bank Mandiri Books $3bn Profit in 2025" (FY25 actuals) | Press/IR | Feb 2026 | Read |
| 6 | BMRI Q3 FY2025 earnings call transcript (Yahoo/Quartr) | Transcript | Oct 2025 | Read (summary) |
| 7 | Bank Mandiri Investor Relations portal | IR primary | Current | Read |
| 8 | sectors.app BMRI stock analysis (P/BV 1.22x, ROE 21.04%) | Data aggregator | Jun 2026 | Read |
| 9 | Yahoo Finance BMRI.JK quote + key statistics | Market data | 10 Jun 2026 | Read |
| 10 | Databoks — BMRI profit +16% Q1 2026 | Press | Apr 2026 | Read |
| 11 | Caproasia / Jakarta Globe — Danantara buys bank AM subsidiaries (1 Apr 2026) | Governance/M&A | Apr 2026 | Read |
| 12 | Danantara / Wikipedia + Lexology + ASEAN Briefing — SOE holding structure | Governance | 2025–26 | Read |
| 13 | "The Big Bank Theory" — fundamental analysis BBCA/BBRI/BMRI/BBNI 2026 | Peer/sector | 13 Apr 2026 | Read (summary) |
| 14 | IDNFinancials — BMRI lending +15.62% Jan 2026 | Press | Feb 2026 | Read |
| 15 | BBCA_research.md (precedent, shared macro cycle) | Internal | 8 Jun 2026 | Read in full |

## Key Recency-Verified Anchors (all `[NON-CAPIQ]`)
- Spot price Rp 4,060; mkt cap Rp 381.4tn; 52w 3,650–5,375; mean PT Rp 5,699 (10 Jun 2026 — Yahoo/Google Finance)
- 1Q26: NP Rp15.4tn (+16.6% YoY); NIM 4.7%; gross NPL 0.98%; net NPL 0.41%; loan growth +16.2% (BRIS-distorted) (Apr 2026)
- FY25: NP Rp56.3tn (+0.9%); NII Rp106.2tn (+4.4%); loans +13.4% to Rp1,895tn; deposits +23.9% to Rp2,106tn; CASA Rp1,431tn (+12.6%) (Feb 2026)
- Ownership: GoI ~52% + INA/Danantara ~8%; Persero SOE; ROE ttm ~21%; P/BV ~1.22x

Stage 0 complete. Dispatching Bravo → Charlie → Delta → Echo → Foxtrot → Golf → Hotel → India sequentially.
