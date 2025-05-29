from langchain_groq.chat_models import ChatGroq

# Initialize the GROQ LLM (replace with your API key)
GROQ_API_KEY = "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"

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    api_key=GROQ_API_KEY,
)

def generate_market_brief(portfolio_exposure, earnings_surprises, sentiment):
    prompt = f"""
You are a helpful and professional finance assistant.

Given the following data, generate a conversational summary answering the user's question:

Portfolio Exposure:
{portfolio_exposure}

Earnings Surprises:
{earnings_surprises}

Market Sentiment:
{sentiment}

Write a detailed, friendly report summarizing these points, including context and implications.
End with an offer to provide more info or answer questions.
"""
    # call your LLM here, e.g. llm.chat or llm.generate with prompt
    llm_response = llm.chat([{"role": "user", "content": prompt}])
    return llm_response.content.strip()


if __name__ == "__main__":
    sample_summary = (
        "Today, your Asia tech allocation is 22 % of AUM, up from 18 % yesterday. "
        "TSMC beat estimates by 4 %, Samsung missed by 2 %. "
        "Regional sentiment is neutral with a cautionary tilt due to rising yields."
    )
    print(generate_market_brief(sample_summary))
