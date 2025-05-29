# AI Tool Usage and Prompt Engineering Log

## Overview
This document tracks the usage of language models, financial agents, and prompt engineering strategies in the RagaAI Finance Assistant.

---

## Prompt Format (for Risk Exposure)
**System Prompt:**
> You are a finance assistant. Based on user queries, summarize:
> - Portfolio exposure (e.g., Asia tech allocation)
> - Earnings surprises (e.g., TSMC beat by 4%)
> - Regional market sentiment

**Example User Query:**
> What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?

**Expected Output:**
> Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields.

---

## LLM Parameters
- Model: `llama3-8b-8192` via Groq API
- Temperature: `0.7`
- Max Tokens: `512`

---

## Logging
- [x] Track LLM failure states
- [x] Tune for structured summaries
- [ ] Add voice feedback (TTS)
