import yfinance as yf
import pandas as pd
import numpy as np
import json, math

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 220)

t = yf.Ticker("AXTI")

print("="*80); print("INFO"); print("="*80)
info = {}
try:
    info = t.info
except Exception as e:
    print("info err", e)

keys = ["longName","currentPrice","regularMarketPrice","previousClose","marketCap","enterpriseValue",
        "floatShares","sharesOutstanding","fiftyTwoWeekHigh","fiftyTwoWeekLow","averageDailyVolume30Day","averageVolume10days",
        "shortPercentOfFloat","shortRatio","sharesShort","heldPercentInsiders","heldPercentInstitutions",
        "trailingPE","forwardPE","beta","dividendYield","trailingEps","forwardEps",
        "targetMeanPrice","targetHighPrice","targetLowPrice","recommendationMean","recommendationKey","numberOfAnalystOpinions",
        "totalDebt","totalCash","totalCashPerShare","enterpriseToRevenue","enterpriseToEbitda",
        "totalRevenue","grossMargins","operatingMargins","profitMargins","ebitda","revenuePerShare",
        "bookValue","priceToBook","sector","industry","fullTimeEmployees","country"]
for k in keys:
    print(f"{k:28s}: {info.get(k)}")

print("\n" + "="*80); print("ANNUAL INCOME STMT"); print("="*80)
try: print(t.income_stmt.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("ANNUAL CASHFLOW"); print("="*80)
try: print(t.cashflow.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("ANNUAL BALANCE SHEET"); print("="*80)
try: print(t.balance_sheet.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("QUARTERLY INCOME STMT"); print("="*80)
try: print(t.quarterly_income_stmt.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("QUARTERLY CASHFLOW"); print("="*80)
try: print(t.quarterly_cashflow.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("PRICE HISTORY ANALYSIS"); print("="*80)
try:
    h = t.history(period="1y", auto_adjust=True)
    px = h["Close"]
    last = px.iloc[-1]
    print("last close:", round(last,3), "date:", px.index[-1].date())
    print("1y ago close:", round(px.iloc[0],3), "date:", px.index[0].date())
    print("1Y return %:", round((last/px.iloc[0]-1)*100,2))
    # YTD
    ytd = px[px.index >= "2026-01-01"]
    if len(ytd)>0:
        print("YTD start:", round(ytd.iloc[0],3), ytd.index[0].date(), "YTD return %:", round((last/ytd.iloc[0]-1)*100,2))
    # 30d realized vol
    ret = np.log(px/px.shift(1)).dropna()
    rv30 = ret.tail(30).std()*math.sqrt(252)
    print("30d realized vol annualized %:", round(rv30*100,2))
    # ADTV 30d $
    adtv = (h["Close"]*h["Volume"]).tail(30).mean()
    print("ADTV 30d $:", round(adtv,0))
    print("avg vol 30d shares:", round(h["Volume"].tail(30).mean(),0))
    print("52w high(hist):", round(px.max(),3), "52w low(hist):", round(px.min(),3))
except Exception as e: print(e)

print("\n" + "="*80); print("INSIDER TRANSACTIONS"); print("="*80)
try: print(t.insider_transactions.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("INSTITUTIONAL HOLDERS"); print("="*80)
try: print(t.institutional_holders.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("MAJOR HOLDERS"); print("="*80)
try: print(t.major_holders.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("EARNINGS HISTORY"); print("="*80)
try: print(t.earnings_history.to_string())
except Exception as e: print(e)

print("\n" + "="*80); print("ANALYST PRICE TARGETS"); print("="*80)
try: print(t.analyst_price_targets)
except Exception as e: print(e)
