from fastapi import APIRouter, Depends
from ai_agent.dependencies import get_chat_service
from ai_agent.schemas.chat import ChatRequest, ChatResponse
from ai_agent.services.chat_service import ChatService

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, service: ChatService = Depends(get_chat_service)) -> ChatResponse:
    return await service.handle_chat(request)