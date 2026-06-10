import yfinance as yf
import numpy as np
import pandas as pd

t = yf.Ticker("AXTI")
info = t.info
price = info.get("currentPrice")
shares = 65423184
cash = 107144000
debt = 78627000
net_debt = debt - cash  # negative => net cash
rev_ttm = 95894000

print(f"Price ${price}  Shares {shares/1e6:.1f}M  NetDebt ${net_debt/1e6:.1f}M (negative=net cash)")

# ---- WACC ----
rf = 0.0455
erp = 0.055
beta = 1.811
ke = rf + beta*erp
# net cash -> equity-only WACC effectively
wacc = ke
print(f"\nWACC adjudication: ke = {rf} + {beta}*{erp} = {ke:.4f}")
print(f"Net cash position -> use ke as WACC = {wacc:.2%}")
print(f"Semis/materials sector WACC band ~10-13%. ke {ke:.1%} is at upper end due to beta 1.81.")
# Sector-midpoint alternative
wacc_sector = 0.115
print(f"Sector-midpoint alt WACC = {wacc_sector:.1%}")

g_term = 0.03  # secondary materials, long-run

def dcf(base_rev, growth_path, ebit_margin_path, wacc, g_term, da_pct=0.09, capex_pct=0.10, nwc_pct=0.03, tax=0.21):
    rev = base_rev
    pv = 0
    fcffs=[]
    for i,(g,m) in enumerate(zip(growth_path, ebit_margin_path)):
        rev = rev*(1+g)
        ebit = rev*m
        nopat = ebit*(1-tax) if ebit>0 else ebit
        fcff = nopat + rev*da_pct - rev*capex_pct - rev*nwc_pct
        fcffs.append(fcff)
        pv += fcff/(1+wacc)**(i+1)
    tv = fcffs[-1]*(1+g_term)/(wacc-g_term)
    pv_tv = tv/(1+wacc)**len(growth_path)
    ev = pv+pv_tv
    equity = ev - net_debt  # net_debt negative adds cash
    return equity/shares, ev, pv_tv/ev

print("\n" + "="*70)
print("DCF — THREE SCENARIOS (5yr explicit, base rev = TTM $95.9M)")
print("="*70)

# BEAR: cyclical, stays low-margin, modest growth
bear = dcf(rev_ttm,
           [0.05,0.08,0.08,0.06,0.05],
           [-0.02,0.01,0.03,0.05,0.06],
           wacc=wacc, g_term=0.02)
# BASE: recovery, InP/datacenter demand, margins normalize to historical ~8-10% operating
base = dcf(rev_ttm,
           [0.15,0.20,0.18,0.15,0.12],
           [0.02,0.06,0.09,0.11,0.12],
           wacc=wacc, g_term=0.03)
# BULL: gallium/germanium criticality + InP datacenter laser substrate boom; hyper growth, margin expansion
bull = dcf(rev_ttm,
           [0.35,0.40,0.35,0.28,0.20],
           [0.05,0.10,0.14,0.17,0.19],
           wacc=wacc, g_term=0.035)

for name,(p,ev,tvr) in [("BEAR",bear),("BASE",base),("BULL",bull)]:
    print(f"{name:5s} implied ${p:7.2f}  EV ${ev/1e6:8.0f}M  TV/EV {tvr:.0%}")

# probability weighting
pw = 0.35*bear[0] + 0.45*base[0] + 0.20*bull[0]
print(f"\nProb-weighted DCF (35/45/20): ${pw:.2f}")

# Sector-midpoint WACC recompute base
base_s = dcf(rev_ttm,[0.15,0.20,0.18,0.15,0.12],[0.02,0.06,0.09,0.11,0.12],wacc=wacc_sector,g_term=0.03)
print(f"Base @ sector-mid WACC {wacc_sector:.1%}: ${base_s[0]:.2f}")

print("\n" + "="*70)
print("RELATIVE VALUATION vs SEMI MATERIALS / SUBSTRATE PEERS")
print("="*70)
PEERS = ["IIVI" if False else "COHR","WOLF","ONTO","FORM","CRUS","SITM"]
# COHR=Coherent (InP/photonics), WOLF=Wolfspeed (SiC substrates), ONTO=Onto Innov,
# FORM=FormFactor, CRUS=Cirrus, SITM=SiTime
mult={}
for p in PEERS:
    try:
        pi=yf.Ticker(p).info
        mult[p]={"evr":pi.get("enterpriseToRevenue"),"eveb":pi.get("enterpriseToEbitda"),
                 "fpe":pi.get("forwardPE"),"mcap":pi.get("marketCap"),
                 "rev":pi.get("totalRevenue"),"gm":pi.get("grossMargins")}
    except Exception as e:
        print("peer err",p,e)
print(f"{'Peer':6} {'EV/Rev':>8} {'EV/EBITDA':>10} {'FwdPE':>8} {'GM':>6}")
for p,v in mult.items():
    print(f"{p:6} {str(round(v['evr'],1) if v['evr'] else 'na'):>8} {str(round(v['eveb'],1) if v['eveb'] else 'na'):>10} {str(round(v['fpe'],1) if v['fpe'] else 'na'):>8} {str(round(v['gm']*100,0) if v['gm'] else 'na'):>6}")

evr_med = np.nanmedian([v['evr'] for v in mult.values() if v['evr'] and v['evr']>0])
fpe_med = np.nanmedian([v['fpe'] for v in mult.values() if v['fpe'] and v['fpe']>0])
print(f"\nPeer median EV/Rev: {evr_med:.1f}x   Fwd P/E: {fpe_med:.1f}x")

# Apply to AXTI. Forward rev est ~ +10-15% => ~$108M; fwd EPS 0.75
rev_fwd = 108e6
implied_evr = (evr_med*rev_fwd - net_debt)/shares
implied_pe = fpe_med*0.752
print(f"AXTI implied @ peer EV/Rev on fwd rev $108M: ${implied_evr:.2f}")
print(f"AXTI implied @ peer Fwd P/E on EPS $0.75: ${implied_pe:.2f}")
rel_blend = np.nanmean([implied_evr, implied_pe])
print(f"Relative blended: ${rel_blend:.2f}")

print("\n" + "="*70)
print("TRIANGULATION")
print("="*70)
blended = 0.6*pw + 0.4*rel_blend
print(f"DCF prob-weighted: ${pw:.2f} (60%)")
print(f"Relative blended:  ${rel_blend:.2f} (40%)")
print(f"BLENDED TARGET:    ${blended:.2f}")
print(f"vs current ${price}: {(blended/price-1)*100:+.1f}%")
