import yfinance as yf

spy = yf.Ticker("SPY")
spy_historical = spy.history(period="1d", interval="1d")



print(spy_historical)


