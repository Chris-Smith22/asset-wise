import yfinance as yf

spy = yf.Ticker("SPY")
spy_historical = spy.history(interval="1d", start="2023-05-01", end="2023-12-31")

mkt_prices = spy_historical["Close"]

'''
print(mkt_prices)
print(mkt_prices.iloc[-1])
'''

cap_gains = round(mkt_prices.iloc[-1] - mkt_prices.iloc[0],2)
cg_rate = round(cap_gains/mkt_prices.iloc[0],4)*100
print(f"Capital Gains: ${cap_gains}, Change: {cg_rate}%")