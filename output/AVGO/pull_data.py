import yfinance as yf
import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

t = yf.Ticker("AVGO")

def section(name):
    print("\n" + "="*80)
    print(name)
    print("="*80)

# ---- INFO ----
section("INFO FIELDS")
info = t.info
keys = ["currentPrice","marketCap","enterpriseValue","floatShares","sharesOutstanding",
        "fiftyTwoWeekHigh","fiftyTwoWeekLow","shortPercentOfFloat","shortRatio",
        "heldPercentInsiders","heldPercentInstitutions","averageDailyVolume30Day",
        "averageDailyVolume10Day","beta","dividendYield","dividendRate","trailingPE","forwardPE",
        "enterpriseToRevenue","enterpriseToEbitda","totalDebt","totalCash",
        "trailingEps","forwardEps","priceToBook","profitMargins","grossMargins",
        "operatingMargins","ebitdaMargins","revenueGrowth","earningsGrowth",
        "recommendationMean","recommendationKey","numberOfAnalystOpinions",
        "targetMeanPrice","targetHighPrice","targetLowPrice","targetMedianPrice",
        "totalRevenue","ebitda","freeCashflow","operatingCashflow","sector","industry",
        "fullTimeEmployees","longName","totalDebt"]
for k in keys:
    print(f"{k}: {info.get(k)}")

# ---- PRICE HISTORY ----
section("PRICE HISTORY (1y)")
hist = t.history(period="1y", auto_adjust=True)
print("First date:", hist.index[0], "Close:", round(hist['Close'].iloc[0],2))
print("Last date:", hist.index[-1], "Close:", round(hist['Close'].iloc[-1],2))
print("1y ago close:", round(hist['Close'].iloc[0],2))
print("Current close:", round(hist['Close'].iloc[-1],2))
print("1y return %:", round((hist['Close'].iloc[-1]/hist['Close'].iloc[0]-1)*100,2))

# YTD
ytd = t.history(start="2026-01-02", auto_adjust=True)
print("YTD start close (2026-01-02ish):", round(ytd['Close'].iloc[0],2))
print("YTD return %:", round((ytd['Close'].iloc[-1]/ytd['Close'].iloc[0]-1)*100,2))

# 30d realized vol annualized
logret = np.log(hist['Close']/hist['Close'].shift(1)).dropna()
vol30 = logret.tail(30).std()*np.sqrt(252)
print("30d realized vol (annualized) %:", round(vol30*100,2))

# ADTV 30d in $
adtv_sh = hist['Volume'].tail(30).mean()
adtv_usd = adtv_sh * hist['Close'].tail(30).mean()
print("ADTV 30d shares:", round(adtv_sh))
print("ADTV 30d $ (B):", round(adtv_usd/1e9,3))

# drawdown from 52wk high
print("Drawdown from 52wk high %:", round((info.get('currentPrice',hist['Close'].iloc[-1])/info.get('fiftyTwoWeekHigh')-1)*100,2))

# ---- INCOME STATEMENT ----
section("ANNUAL INCOME STATEMENT")
inc = t.income_stmt
print(inc.to_string())

# ---- BALANCE SHEET ----
section("ANNUAL BALANCE SHEET")
bs = t.balance_sheet
print(bs.to_string())

# ---- CASH FLOW ----
section("ANNUAL CASH FLOW")
cf = t.cashflow
print(cf.to_string())

# ---- ANALYST TARGETS ----
section("ANALYST PRICE TARGETS")
try:
    print(t.analyst_price_targets)
except Exception as e:
    print("err", e)

# ---- RECOMMENDATIONS ----
section("RECOMMENDATIONS")
try:
    print(t.recommendations.to_string())
except Exception as e:
    print("err", e)

# ---- INSIDER ----
section("INSIDER TRANSACTIONS")
try:
    it = t.insider_transactions
    print(it.head(15).to_string() if it is not None else "None")
except Exception as e:
    print("err", e)

# ---- INSTITUTIONAL ----
section("INSTITUTIONAL HOLDERS")
try:
    ih = t.institutional_holders
    print(ih.to_string() if ih is not None else "None")
except Exception as e:
    print("err", e)

# ---- EARNINGS HISTORY ----
section("EARNINGS HISTORY")
try:
    print(t.earnings_history.to_string())
except Exception as e:
    print("err", e)
