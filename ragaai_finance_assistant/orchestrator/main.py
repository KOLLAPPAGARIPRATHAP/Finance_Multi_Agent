#orchestrator/main.py
from fastapi import FastAPI
from orchestrator.orchestrator import router

app = FastAPI(title="Finance Assistant Orchestrator")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
