from fastapi import FastAPI
from ai_agent.api.chat import router as chat_router

app = FastAPI(title="AI Agent")


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/echo/{count}")
async def echo_count(count: int):
    return {"count": 2*count}

app.include_router(chat_router, tags=["chat"])