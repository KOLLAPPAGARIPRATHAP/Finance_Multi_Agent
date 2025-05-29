from fastapi import APIRouter, Query
from langchain_groq.chat_models import ChatGroq
from pydantic import BaseModel

router = APIRouter()

# Initialize LLM once with your API key and model
GROQ_API_KEY = "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"

# Initialize Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    api_key=GROQ_API_KEY,
)

class MarketSummaryResponse(BaseModel):
    market_brief: str
    portfolio_exposure: str = None
    earnings_surprises: str = None
    sentiment: str = None

@router.get("/market-summary/", response_model=MarketSummaryResponse)
async def get_market_summary_from_query(query: str = Query(..., description="Natural language question")):
    """
    Process a natural language query and generate a detailed market summary,
    including portfolio exposure, earnings surprises, and market sentiment.
    """
    prompt = f"""
You are a professional financial assistant. A user asked the following question:

"{query}"

Based on the following data, generate a detailed, conversational summary suitable for verbal response:

- Portfolio exposure: Asia tech allocation is 22% of AUM, up from 18% yesterday.
- Earnings surprises: TSMC beat estimates by 4%, Samsung missed by 2%.
- Market sentiment: Regional sentiment is neutral with a cautionary tilt due to rising yields.

Make the summary clear, friendly, and informative, as if explaining to a client.
End with an offer to provide more information or answer further questions.
"""

    try:
        response = llm.invoke(prompt)
        answer = response.content.strip()

        return MarketSummaryResponse(
            market_brief=answer,
            portfolio_exposure="Asia tech allocation is 22% of AUM, up from 18% yesterday.",
            earnings_surprises="TSMC beat estimates by 4%, Samsung missed by 2%.",
            sentiment="Regional sentiment is neutral with a cautionary tilt due to rising yields."
        )

    except Exception as e:
        return MarketSummaryResponse(market_brief=f"Failed to generate response: {str(e)}")
