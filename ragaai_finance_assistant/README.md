# RagaAI Finance Assistant 🧠💰

This AI-powered financial assistant provides:
- Real-time market summaries
- Portfolio risk insights
- Earnings surprise analysis
- Conversational & voice-based answers

## 🛠️ Tech Stack
- FastAPI (backend)
- Streamlit (frontend UI)
- LangChain + Groq LLaMA 3 (LLM)
- yFinance + Web Scraping (data sources)

## 🚀 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn orchestrator.main:app --reload

# Run Streamlit app
streamlit run streamlit_app/app.py
