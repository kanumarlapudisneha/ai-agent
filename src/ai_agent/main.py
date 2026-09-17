from fastapi import FastAPI
from ai_agent.schemas.chat import ChatRequest, ChatResponse

app = FastAPI(title="AI Agent")


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/echo/{count}")
async def echo_count(count: int):
    return {"count": 2*count}

@app.post("/chat", response_model = ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint to handle chat requests.
    """
    reply_message = f"Received your message: {request.message}"
    return ChatResponse(session_id=request.session_id, reply=reply_message)