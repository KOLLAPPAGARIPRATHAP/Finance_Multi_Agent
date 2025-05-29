from langchain_groq.chat_models import ChatGroq

#GROQ_API_KEY = "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"
GROQ_API_KEY = "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"

# Initialize Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    api_key=GROQ_API_KEY,
)
# Example extra configs
ALPHAVANTAGE_API_KEY = "1OJC255JNF95JG7W"

# Threshold for risk classification in analysis_agent
RISK_THRESHOLD_HIGH = 0.7
RISK_THRESHOLD_MEDIUM = 0.4

# URLs for third-party APIs
SCRAPING_API_ENDPOINT = "https://api.scrapingservice.com"

# Other constants
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 512
