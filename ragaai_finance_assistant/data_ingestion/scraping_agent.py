import requests
from bs4 import BeautifulSoup

def get_earnings_surprises(ticker: str):
    url = f"https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch data for {ticker} - Status: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Dummy static return, replace with actual scraping logic when page structure is known
        return {
            "ticker": ticker,
            "earnings_surprise_pct": 4.0,
            "summary": f"{ticker} beat estimates by 4%"
        }

    except Exception as e:
        print(f"Error scraping earnings for {ticker}: {e}")
        return None

if __name__ == "__main__":
    print(get_earnings_surprises("TSM"))
