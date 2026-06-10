#!/usr/bin/env python3
"""Multi-name valuation engine: DCF (FCFF) + Relative for 20 semis/hardware names.
Data: yfinance (as-of run date). Currency: ADRs converted to USD via TWDUSD.
Not financial advice."""
import yfinance as yf
import numpy as np
import json, datetime, sys

RF   = 0.0453          # live 10Y UST
ERP  = 0.046           # Damodaran implied ERP (US)
GTV  = 0.025           # terminal growth
KD_DEFAULT = 0.055
TWDUSD = 0.031632554   # USD per TWD

NAMES = ['MU','AMD','INTC','AMAT','DELL','MRVL','STX','WDC','ASX','COHR',
         'CIEN','LITE','HPE','STM','TER','FLEX','UMC','ON','TSEM','SNX']

PEERS = {
 'MU':  ['STX','WDC','MRVL','STM','ON'],
 'STX': ['WDC','MU','DELL','HPE','ON'],
 'WDC': ['STX','MU','DELL','ON','MRVL'],
 'AMD': ['INTC','MRVL','STM','ON','MU'],
 'INTC':['AMD','STM','ON','MRVL','UMC'],
 'MRVL':['AMD','ON','STM','COHR','INTC'],
 'STM': ['ON','INTC','AMD','MRVL','MU'],
 'ON':  ['STM','MRVL','INTC','AMD','MU'],
 'UMC': ['TSEM','ASX','STM','ON','INTC'],
 'TSEM':['UMC','ASX','ON','STM','MRVL'],
 'ASX': ['UMC','TSEM','STM','ON','FLEX'],
 'AMAT':['TER','MRVL','AMD','STM','ON'],
 'TER': ['AMAT','MRVL','ON','STM','COHR'],
 'COHR':['LITE','CIEN','MRVL','AMAT','TER'],
 'CIEN':['LITE','COHR','MRVL','HPE','AMD'],
 'LITE':['COHR','CIEN','MRVL','AMAT','ON'],
 'DELL':['HPE','STX','WDC','SNX','FLEX'],
 'HPE': ['DELL','CIEN','SNX','FLEX','STX'],
 'FLEX':['SNX','DELL','HPE','ON','ASX'],
 'SNX': ['FLEX','DELL','HPE','STX','WDC'],
}

NAME_FULL = {
 'MU':'Micron Technology','AMD':'Advanced Micro Devices','INTC':'Intel',
 'AMAT':'Applied Materials','DELL':'Dell Technologies','MRVL':'Marvell Technology',
 'STX':'Seagate Technology','WDC':'Western Digital','ASX':'ASE Technology (ADR)',
 'COHR':'Coherent','CIEN':'Ciena','LITE':'Lumentum','HPE':'Hewlett Packard Enterprise',
 'STM':'STMicroelectronics','TER':'Teradyne','FLEX':'Flex','UMC':'United Microelectronics (ADR)',
 'ON':'ON Semiconductor','TSEM':'Tower Semiconductor','SNX':'TD Synnex',
}

_cache = {}
def get(tk):
    if tk in _cache: return _cache[tk]
    t = yf.Ticker(tk)
    d = {'info': t.info}
    try: d['inc'] = t.income_stmt
    except Exception: d['inc'] = None
    try: d['cf'] = t.cashflow
    except Exception: d['cf'] = None
    try: d['bs'] = t.balance_sheet
    except Exception: d['bs'] = None
    _cache[tk] = d
    return d

def row(df, label, col=0):
    try:
        if df is not None and label in df.index:
            v = df.loc[label].iloc[col]
            return float(v) if v == v else None
    except Exception:
        pass
    return None

def med(xs):
    xs = [x for x in xs if x is not None and x == x and np.isfinite(x) and x > 0]
    return float(np.median(xs)) if xs else None

def fx_to_usd(info):
    return TWDUSD if info.get('financialCurrency') == 'TWD' else 1.0

def ev_metrics(tk):
    """Self-computed, currency-consistent (USD) EV multiples for one ticker."""
    info = get(tk)['info']
    price = info.get('currentPrice'); mcap = info.get('marketCap')
    if not price or not mcap: return None
    fx = fx_to_usd(info)
    shares = mcap / price
    debt = (info.get('totalDebt') or 0) * fx
    cash = (info.get('totalCash') or 0) * fx
    rev  = (info.get('totalRevenue') or 0) * fx
    ebitda = (info.get('ebitda') or 0) * fx
    ev = mcap + debt - cash
    return {'price': price, 'shares': shares, 'net_debt': debt-cash,
            'rev': rev, 'ebitda': ebitda, 'ev': ev,
            'evr': ev/rev if rev > 0 else None,
            'eve': ev/ebitda if ebitda > 0 else None,
            'pe': info.get('forwardPE')}

def relative_val(tk):
    """Peer-median multiples in consistent USD; proper net-debt bridge for EV multiples."""
    m = ev_metrics(tk)
    if not m: return None
    price = m['price']; shares = m['shares']; nd = m['net_debt']
    pm = {'pe': [], 'evr': [], 'eve': []}
    peer_rows = []
    for p in PEERS[tk]:
        pmx = ev_metrics(p)
        if not pmx: continue
        if pmx['pe'] and pmx['pe'] > 0: pm['pe'].append(pmx['pe'])
        if pmx['evr'] and pmx['evr'] > 0: pm['evr'].append(pmx['evr'])
        if pmx['eve'] and pmx['eve'] > 0: pm['eve'].append(pmx['eve'])
        peer_rows.append({'t': p, 'pe': pmx['pe'], 'evr': pmx['evr'], 'eve': pmx['eve']})
    m_pe, m_evr, m_eve = med(pm['pe']), med(pm['evr']), med(pm['eve'])
    implied = {}
    if m['pe'] and m['pe'] > 0 and m_pe:
        implied['pe'] = price * m_pe / m['pe']            # P/E ratio scaling (clean)
    if m['rev'] > 0 and m_evr:
        implied['evr'] = (m_evr * m['rev'] - nd) / shares  # EV/Rev bridge
    if m['ebitda'] > 0 and m_eve:
        implied['eve'] = (m_eve * m['ebitda'] - nd) / shares  # EV/EBITDA bridge
    implied = {k: v for k, v in implied.items() if v and v > 0}
    rel = med(list(implied.values())) if implied else None
    return {'price': price, 'co_mult': {'pe': m['pe'], 'evr': m['evr'], 'eve': m['eve']},
            'peer_med': {'pe': m_pe, 'evr': m_evr, 'eve': m_eve},
            'implied': implied, 'rel_price': rel, 'peer_rows': peer_rows}

def dcf_val(tk):
    d = get(tk); info = d['info']; inc = d['inc']; cf = d['cf']
    price = info.get('currentPrice'); mcap = info.get('marketCap')
    if not price or not mcap: return None
    shares = mcap / price  # effective traded units (handles ADR)
    fx = fx_to_usd(info)
    # revenue series (financial currency -> USD)
    revs = []
    if inc is not None and 'Total Revenue' in inc.index:
        for i in range(min(4, inc.shape[1])):
            v = row(inc, 'Total Revenue', i)
            if v: revs.append(v * fx)
    if len(revs) < 2: return None
    revs = revs[::-1]  # oldest..latest
    rev0 = revs[-1]
    hist_cagr = (revs[-1]/revs[0])**(1/(len(revs)-1)) - 1 if revs[0] > 0 else 0.05
    # consensus +1y growth if available
    y1 = hist_cagr
    try:
        re = yf.Ticker(tk).revenue_estimate
        if re is not None and '+1y' in re.index:
            g = float(re.loc['+1y','growth'])
            if g == g and -0.5 < g < 1.0: y1 = g
    except Exception: pass
    y1 = max(min(y1, 0.40), -0.10)
    growth_path = np.linspace(y1, GTV + 0.01, 5)
    # margins: 3y median
    def margin_series(num_df, num_label, denom_df=inc, sign=1):
        out = []
        n = min(3, inc.shape[1]) if inc is not None else 0
        for i in range(n):
            r = row(num_df, num_label, i); rv = row(inc, 'Total Revenue', i)
            if r is not None and rv and rv != 0:
                out.append(sign*r/rv)
        return med(out)
    ebit_m = margin_series(inc, 'Operating Income')
    if ebit_m is None: ebit_m = margin_series(inc, 'EBIT') or 0.12
    da_p = margin_series(cf, 'Depreciation And Amortization') or 0.05
    capex_p = margin_series(cf, 'Capital Expenditure', sign=-1) or 0.05
    capex_p = abs(capex_p)
    nwc_p = margin_series(cf, 'Change In Working Capital', sign=-1)
    nwc_p = abs(nwc_p) if nwc_p is not None else 0.01
    nwc_p = min(nwc_p, 0.05)
    tax = 0.21
    # WACC
    beta_raw = info.get('beta') or 1.1
    beta_adj = 0.33 + 0.67*beta_raw
    ke = RF + beta_adj*ERP
    total_debt = (info.get('totalDebt') or 0) * fx
    cash = (info.get('totalCash') or 0) * fx
    mcap_usd = mcap  # already USD (traded ccy)
    ev_w = mcap_usd/(mcap_usd+total_debt) if (mcap_usd+total_debt) > 0 else 1.0
    wacc = ev_w*ke + (1-ev_w)*KD_DEFAULT*(1-tax)
    wacc = max(wacc, GTV + 0.02)  # gate
    # FCFF
    rev_t = rev0; fcff = []
    for g in growth_path:
        rev_t *= (1+g)
        nopat = rev_t*ebit_m*(1-tax)
        fcff.append(nopat + rev_t*da_p - rev_t*capex_p - rev_t*nwc_p)
    tv_gordon = fcff[-1]*(1+GTV)/(wacc-GTV)
    ebitda_t = rev_t*ebit_m + rev_t*da_p
    tv_exit = ebitda_t * 14
    tv = 0.5*(tv_gordon+tv_exit)
    pv_fcff = sum(f/(1+wacc)**(i+1) for i,f in enumerate(fcff))
    pv_tv = tv/(1+wacc)**5
    ev = pv_fcff+pv_tv
    equity = ev + cash - total_debt
    dcf_price = equity/shares
    return {'dcf_price': dcf_price, 'wacc': wacc, 'ke': ke, 'beta_raw': beta_raw,
            'beta_adj': beta_adj, 'y1_growth': y1, 'hist_cagr': hist_cagr,
            'ebit_m': ebit_m, 'da_p': da_p, 'capex_p': capex_p, 'nwc_p': nwc_p,
            'pv_tv_ev': pv_tv/ev if ev else None, 'fcff': fcff, 'rev0': rev0,
            'fx': fx, 'net_debt': total_debt-cash}

results = {}
for tk in NAMES:
    try:
        info = get(tk)['info']
        rel = relative_val(tk)
        dcf = dcf_val(tk)
        price = info.get('currentPrice')
        dcf_p = dcf['dcf_price'] if dcf else None
        rel_p = rel['rel_price'] if rel else None
        if dcf_p and rel_p: blended = 0.5*dcf_p + 0.5*rel_p
        elif rel_p: blended = rel_p
        elif dcf_p: blended = dcf_p
        else: blended = None
        upside = (blended/price - 1) if (blended and price) else None
        results[tk] = {
            'name': NAME_FULL[tk], 'sector': info.get('sector'),
            'industry': info.get('industry'), 'price': price,
            'mcap': info.get('marketCap'), 'fwd_pe': info.get('forwardPE'),
            'beta': info.get('beta'), 'fin_ccy': info.get('financialCurrency'),
            'rel': rel, 'dcf': dcf, 'dcf_price': dcf_p, 'rel_price': rel_p,
            'blended': blended, 'upside': upside}
        u = f"{upside*100:+.0f}%" if upside is not None else "n/a"
        print(f"{tk:5} px={price:>8.2f}  DCF={dcf_p if dcf_p else 0:>8.1f}  REL={rel_p if rel_p else 0:>8.1f}  FAIR={blended if blended else 0:>8.1f}  {u}")
    except Exception as e:
        print(f"{tk:5} ERROR {e}")
        results[tk] = {'error': str(e)}

results['_meta'] = {'run_date': str(datetime.date.today()), 'rf': RF, 'erp': ERP,
                    'gtv': GTV, 'twdusd': TWDUSD}
with open('valuation_results.json','w') as f:
    json.dump(results, f, default=str, indent=1)
print('\nSaved valuation_results.json')
