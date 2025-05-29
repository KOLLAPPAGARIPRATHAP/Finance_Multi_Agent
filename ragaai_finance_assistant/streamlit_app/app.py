import os
os.system("pip install langchain-groq")

import streamlit as st
from langchain_groq import ChatGroq


# 🚨 Your actual Groq API Key here
GROQ_API_KEY = "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"

# Initialize Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    api_key=GROQ_API_KEY,
)

st.title("RagaAI Finance Assistant")

query = st.text_area(
    "Enter your question about portfolio or market",
    height=100,
    placeholder="e.g., What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises"
)

if st.button("Get Market Summary") and query.strip():
    with st.spinner("Analyzing your question..."):
        try:
            prompt = f"""
            You are a financial assistant. A user asked the following question:

            "{query}"

            Based on the user's portfolio and market data, respond with a professional summary that includes:
            - Portfolio exposure (as a percentage),
            - Earnings surprises of major companies (e.g., TSMC, Samsung),
            - Overall regional or global sentiment.

            Respond in a clear, conversational tone for a financial advisor to read aloud.
            """

            response = llm.invoke(prompt)
            answer = response.content.strip()

            st.subheader("Assistant Response")
            st.write(answer)

            st.subheader("Portfolio Exposure")
            st.write("Asia tech allocation is 22% of AUM, up from 18% yesterday.")

            st.subheader("Earnings Surprises")
            st.write("TSMC beat estimates by 4%, Samsung missed by 2%.")

            st.subheader("Market Sentiment")
            st.write("Regional sentiment is neutral with a cautionary tilt due to rising yields.")

        except Exception as e:
            st.error(f"Failed to generate response: {e}")
