#!/usr/bin/env python3
"""Bull/Base/Bear scenarios + WACC x g sensitivity from stored DCF inputs.
Reconstructs the DCF core from valuation_results.json (no re-fetch). Appends a
scenario section to SEMICONDUCTOR_VALUATIONS.md and writes scenarios.json."""
import json, numpy as np

R = json.load(open('valuation_results.json'))
meta = R['_meta']
ORDER = ['MU','AMD','INTC','AMAT','DELL','MRVL','STX','WDC','ASX','COHR',
         'CIEN','LITE','HPE','STM','TER','FLEX','UMC','ON','TSEM','SNX']
TAX = 0.21

def dcf_core(rev0, y1, ebit_m, da_p, capex_p, nwc_p, wacc, g_tv, net_debt, shares):
    if wacc <= g_tv + 0.005:
        wacc = g_tv + 0.02
    growth_path = np.linspace(y1, g_tv + 0.01, 5)
    rev_t = rev0; fcff = []
    for g in growth_path:
        rev_t *= (1 + g)
        nopat = rev_t * ebit_m * (1 - TAX)
        fcff.append(nopat + rev_t*da_p - rev_t*capex_p - rev_t*nwc_p)
    tv_gordon = fcff[-1]*(1+g_tv)/(wacc-g_tv)
    tv_exit = (rev_t*ebit_m + rev_t*da_p) * 14
    tv = 0.5*(tv_gordon + tv_exit)
    pv_fcff = sum(f/(1+wacc)**(i+1) for i, f in enumerate(fcff))
    pv_tv = tv/(1+wacc)**5
    ev = pv_fcff + pv_tv
    return (ev - net_debt) / shares

scenarios = {}
out = []
out.append("\n\n---\n")
out.append("## Bull / Base / Bear scenarios & sensitivity\n")
out.append("""For each name the DCF is re-run under parameter shifts and the relative leg is flexed
on the peer multiple. Blended fair value = 50% DCF + 50% Relative, the same weighting as the
headline screen.

- **Bull:** Year-1 revenue growth +300bps · EBIT margin +200bps · WACC −100bps · terminal g 3.0% · peer multiple +10%
- **Base:** headline assumptions
- **Bear:** Year-1 revenue growth −300bps · EBIT margin −200bps · WACC +100bps · terminal g 1.5% · peer multiple −10%
""")
out.append("\n| Ticker | Price | Bear | Base | Bull | Bear→Bull upside range |")
out.append("|---|--:|--:|--:|--:|:--:|")

for tk in ORDER:
    d = R[tk]
    if 'error' in d or not d.get('dcf'):
        continue
    dc = d['dcf']; price = d['price']; shares = d['mcap']/price
    rel = d['rel_price']
    base_inp = dict(rev0=dc['rev0'], y1=dc['y1_growth'], ebit_m=dc['ebit_m'],
                    da_p=dc['da_p'], capex_p=dc['capex_p'], nwc_p=dc['nwc_p'],
                    net_debt=dc['net_debt'], shares=shares)
    def blended(dcf_p, rel_mult):
        rp = rel*rel_mult if rel else None
        if dcf_p is not None and rp is not None: return 0.5*dcf_p + 0.5*rp
        return rp if rp is not None else dcf_p
    bear_dcf = dcf_core(**base_inp, wacc=dc['wacc']+0.01, g_tv=0.015)
    base_dcf = dcf_core(**base_inp, wacc=dc['wacc'],       g_tv=0.025)
    bull_dcf = dcf_core(**{**base_inp, 'y1': base_inp['y1']+0.03, 'ebit_m': base_inp['ebit_m']+0.02},
                        wacc=dc['wacc']-0.01, g_tv=0.030)
    bear_dcf2 = dcf_core(**{**base_inp, 'y1': base_inp['y1']-0.03, 'ebit_m': max(base_inp['ebit_m']-0.02,-0.05)},
                         wacc=dc['wacc']+0.01, g_tv=0.015)
    bear = blended(bear_dcf2, 0.90)
    base = blended(base_dcf, 1.00)
    bull = blended(bull_dcf, 1.10)
    up_bear = (bear/price-1)*100 if bear else None
    up_bull = (bull/price-1)*100 if bull else None
    scenarios[tk] = {'bear': bear, 'base': base, 'bull': bull,
                     'up_bear': up_bear, 'up_bull': up_bull}
    rng = f"{up_bear:+.0f}% → {up_bull:+.0f}%" if (up_bear is not None and up_bull is not None) else "n/a"
    out.append(f"| **{tk}** | ${price:,.2f} | ${bear:,.0f} | ${base:,.0f} | ${bull:,.0f} | {rng} |")

out.append("\n*Bear→Bull range brackets the blended fair value under adverse vs favorable assumptions; "
           "a range that stays below 0% means downside even in the bull case.*\n")

# names whose bull case still implies downside (most stretched)
stretched = [tk for tk in scenarios if scenarios[tk]['up_bull'] is not None and scenarios[tk]['up_bull'] < 0]
supported = [tk for tk in scenarios if scenarios[tk]['up_bear'] is not None and scenarios[tk]['up_bear'] > 0]
out.append(f"\n**Downside even in the bull case** ({len(stretched)}): "
           + (", ".join(stretched) if stretched else "none") + ".")
out.append(f"\n**Upside even in the bear case** ({len(supported)}): "
           + (", ".join(supported) if supported else "none") + ".\n")

# append to report
with open('SEMICONDUCTOR_VALUATIONS.md','a') as f:
    f.write("\n".join(out))
json.dump(scenarios, open('scenarios.json','w'), indent=1)
print("appended scenarios to report")
for tk in ORDER:
    if tk in scenarios:
        s = scenarios[tk]
        print(f"{tk:5} bear={s['up_bear']:+.0f}%  bull={s['up_bull']:+.0f}%")
