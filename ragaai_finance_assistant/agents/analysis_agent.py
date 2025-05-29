def analyze_risk_exposure(portfolio_allocation: dict):
    """
    Analyzes risk exposure given portfolio allocation dict.
    Example input: {"Asia Tech": 22, "Europe Banks": 15, "US Healthcare": 30}
    """
    try:
        total = sum(portfolio_allocation.values())
        if total == 0:
            return "Portfolio allocation is empty."
        exposure_report = []
        for sector, pct in portfolio_allocation.items():
            exposure_report.append(f"{sector} allocation is {pct}% of total AUM.")
        return " ".join(exposure_report)
    except Exception as e:
        print(f"Analysis Agent error: {e}")
        return "Failed to analyze risk exposure."

if __name__ == "__main__":
    example_portfolio = {"Asia Tech": 22, "Europe Banks": 15, "US Healthcare": 30}
    print(analyze_risk_exposure(example_portfolio))
