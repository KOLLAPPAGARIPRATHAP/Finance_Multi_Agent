import yfinance as yf

def fetch_market_data(ticker: str, period: str = "5d"):
    """
    Fetches recent market data for given ticker using yfinance.
    """
    try:
        ticker_obj = yf.Ticker(ticker)
        hist = ticker_obj.history(period=period)
        if hist.empty:
            return None
        latest_close = hist['Close'].iloc[-1]
        prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else latest_close
        return {
            "ticker": ticker,
            "latest_close": latest_close,
            "prev_close": prev_close,
            "change_pct": ((latest_close - prev_close) / prev_close) * 100 if prev_close else 0,
            "date": hist.index[-1].strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"API Agent error: {e}")
        return None

if __name__ == "__main__":
    print(fetch_market_data("TSM"))
