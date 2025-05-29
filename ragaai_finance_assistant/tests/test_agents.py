
import pytest
from agents import api_agent, analysis_agent

def test_fetch_market_data():
    result = api_agent.fetch_market_data("TSM")
    assert result is not None
    assert "latest_close" in result

def test_risk_analysis():
    portfolio = {"Asia Tech": 22, "US Banks": 18}
    report = analysis_agent.analyze_risk_exposure(portfolio)
    assert "Asia Tech" in report
