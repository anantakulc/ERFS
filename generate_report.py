#!/usr/bin/env python3
"""Generate markdown valuation report from valuation_results.json."""
import json

R = json.load(open('valuation_results.json'))
meta = R.pop('_meta')
ORDER = ['MU','AMD','INTC','AMAT','DELL','MRVL','STX','WDC','ASX','COHR',
         'CIEN','LITE','HPE','STM','TER','FLEX','UMC','ON','TSEM','SNX']
WHAT = {
 'MU':'DRAM & NAND memory chips','AMD':'CPUs, GPUs & adaptive processors',
 'INTC':'CPU design + foundry','AMAT':'Semiconductor fab equipment',
 'DELL':'Servers, PCs & storage','MRVL':'Data-center & infra silicon',
 'STX':'Hard disk drives','WDC':'HDDs & flash storage',
 'ASX':'Chip assembly, packaging & test (OSAT)','COHR':'Lasers, optics & networking',
 'CIEN':'Optical networking systems','LITE':'Optical/photonics components',
 'HPE':'Enterprise servers & networking','STM':'Broad-line analog/MCU chips',
 'TER':'Automated chip test equipment','FLEX':'Contract electronics mfg (EMS)',
 'UMC':'Foundry (mature nodes)','ON':'Power & analog semis (auto/industrial)',
 'TSEM':'Specialty analog foundry','SNX':'IT product distribution',
}
def f(x, d=0, pre='', suf=''):
    if x is None: return 'n/a'
    try: return f"{pre}{x:,.{d}f}{suf}"
    except Exception: return 'n/a'
def pct(x):
    return f"{x*100:+.0f}%" if x is not None else 'n/a'

# ---- master table sorted by upside ----
rows = [(tk, R[tk]) for tk in ORDER if 'error' not in R[tk]]
rows.sort(key=lambda kv: (kv[1]['upside'] if kv[1]['upside'] is not None else -9))

out = []
out.append("# Semiconductor & IT-Hardware Valuation Screen\n")
out.append(f"**Run date:** {meta['run_date']}  |  **Data source:** yfinance (as-of quotes)  "
           f"|  **Method:** DCF (FCFF) + Relative (peer-median multiples), 50/50 blend\n")
out.append(f"**Assumptions:** risk-free {meta['rf']*100:.2f}% (10Y UST) · ERP {meta['erp']*100:.1f}% "
           f"(Damodaran implied) · terminal g {meta['gtv']*100:.1f}% · Blume-adjusted beta · "
           f"TWD→USD {meta['twdusd']:.5f} for ADRs (ASX, UMC)\n")
out.append("> ⚠️ **Educational research, not financial advice.** Quotes reflect the data feed's "
           "as-of values on the run date and across this universe sit at historically elevated "
           "absolute levels — see *Reading the results* below.\n")

out.append("\n## Master table — fair value vs market (sorted by upside)\n")
out.append("| Ticker | Company | What they do | Price | DCF | Relative | **Fair (blend)** | **Upside** | Fwd P/E |")
out.append("|---|---|---|--:|--:|--:|--:|:--:|--:|")
for tk, d in rows:
    out.append(f"| **{tk}** | {d['name']} | {WHAT[tk]} | {f(d['price'],2,'$')} | "
               f"{f(d['dcf_price'],0,'$')} | {f(d['rel_price'],0,'$')} | "
               f"**{f(d['blended'],0,'$')}** | **{pct(d['upside'])}** | {f(d['fwd_pe'],1)} |")

out.append("\n*DCF is an absolute valuation; Relative is cross-sectional (vs sector peers). "
           "Blend = 50% DCF / 50% Relative.*\n")

# reading the results
out.append("""
## Reading the results

Two signals, two different questions:

- **DCF (absolute):** discounts each company's own normalized free cash flow. Across this
  universe DCF lands **well below market** for almost every name. That is the screen telling
  you absolute price levels are rich relative to mid-cycle cash generation — typical late in a
  semiconductor up-cycle when trailing/forward earnings sit near a peak.
- **Relative (cross-sectional):** values each name on peer-median P/E, EV/Revenue and
  EV/EBITDA. Because the *whole* sector is richly priced, this filters out the common
  inflation and surfaces who is cheap or expensive **relative to the group**. This is the more
  useful read inside a uniformly extended sector.

**Where the two agree** is where conviction is highest. Names cheap on *both* DCF and relative
are the most defensible longs; names expensive on both are the most exposed if the cycle rolls.
""")

# ---- per-name detail ----
out.append("\n## Per-name detail\n")
for tk in ORDER:
    d = R[tk]
    if 'error' in d:
        out.append(f"\n### {tk} — ERROR: {d['error']}\n"); continue
    rel = d['rel']; dcf = d['dcf']
    out.append(f"\n### {tk} — {d['name']}")
    out.append(f"*{WHAT[tk]}* · {d['industry']}\n")
    out.append(f"| Metric | Value |")
    out.append(f"|---|--:|")
    out.append(f"| Market price | {f(d['price'],2,'$')} |")
    out.append(f"| Market cap | {f(d['mcap']/1e9,1,'$','B')} |")
    out.append(f"| Forward P/E | {f(d['fwd_pe'],1)} |")
    out.append(f"| Beta (raw) | {f(d['beta'],2)} |")
    out.append(f"| **DCF fair value** | **{f(d['dcf_price'],2,'$')}** |")
    out.append(f"| **Relative fair value** | **{f(d['rel_price'],2,'$')}** |")
    out.append(f"| **Blended fair value** | **{f(d['blended'],2,'$')}** |")
    out.append(f"| **Upside / (downside)** | **{pct(d['upside'])}** |")
    if dcf:
        out.append(f"\n**DCF inputs:** WACC {dcf['wacc']*100:.1f}% · ke {dcf['ke']*100:.1f}% · "
                   f"beta(adj) {dcf['beta_adj']:.2f} · Y1 rev growth {dcf['y1_growth']*100:.1f}% · "
                   f"hist rev CAGR {dcf['hist_cagr']*100:.1f}% · EBIT margin {dcf['ebit_m']*100:.1f}% · "
                   f"capex {dcf['capex_p']*100:.1f}% of rev · TV/EV {f(dcf['pv_tv_ev']*100 if dcf['pv_tv_ev'] else None,0,suf='%')}")
    if rel and rel['implied']:
        im = rel['implied']; pmd = rel['peer_med']
        parts = []
        if 'pe' in im: parts.append(f"P/E {f(im['pe'],0,'$')} (peer med {f(pmd['pe'],1)}x)")
        if 'evr' in im: parts.append(f"EV/Rev {f(im['evr'],0,'$')} (peer med {f(pmd['evr'],1)}x)")
        if 'eve' in im: parts.append(f"EV/EBITDA {f(im['eve'],0,'$')} (peer med {f(pmd['eve'],1)}x)")
        out.append(f"\n**Relative legs:** " + " · ".join(parts))
        out.append(f"\n**Peers:** " + ", ".join(p['t'] for p in rel['peer_rows']))

out.append("\n\n---\n")
out.append("## Method notes & caveats\n")
out.append("""
- **DCF (FCFF):** 5-year revenue fade from a consensus/historical Year-1 growth rate toward a
  2.5% terminal rate; 3-year-median operating margin, D&A, capex and working-capital ratios;
  NOPAT-based free cash flow; terminal value = midpoint of Gordon-growth and a 14× EV/EBITDA
  exit; discounted at a Blume-adjusted-beta WACC. Equity = EV + cash − debt.
- **Relative:** peer-median forward P/E, EV/Revenue and EV/EBITDA. EV multiples are
  self-computed in USD with a proper net-debt bridge so levered names (DELL, HPE) and ADRs
  (ASX, UMC, TWD financials) are currency- and leverage-consistent. Implied price = median of
  the available legs.
- **Cyclicality:** these are cyclical businesses. Trailing/forward margins near a cycle peak
  flatter relative multiples and depress DCF upside; near a trough the reverse. Treat point
  estimates as a screen, not a target.
- **Intel (INTC):** 3-year-median operating margin is negative (recent losses / foundry
  build-out), which produces a negative DCF — flagged rather than suppressed. Relative carries
  the call for INTC.
- **Known limitations:** single-scenario point estimates (no per-name bull/base/bear or
  sensitivity grid in this batch run); SOTP not applied (yfinance does not expose segments —
  DELL and HPE would warrant it); peer sets are pragmatic, not exhaustive; quotes are as-of the
  data feed and not independently verified.
- **Not financial advice.** Research/educational output only.
""")

open('SEMICONDUCTOR_VALUATIONS.md','w').write("\n".join(out))
print("wrote SEMICONDUCTOR_VALUATIONS.md")
print("lines:", len(out))
