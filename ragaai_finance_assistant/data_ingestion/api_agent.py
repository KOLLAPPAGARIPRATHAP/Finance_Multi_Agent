import yfinance as yf

def get_stock_price(ticker: str, period: str = "2d"):
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period=period)
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
        print(f"Error fetching stock data for {ticker}: {e}")
        return None

if __name__ == "__main__":
    print(get_stock_price("TSM"))



