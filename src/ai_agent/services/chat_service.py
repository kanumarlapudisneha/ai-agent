from ai_agent.schemas.chat import ChatRequest, ChatResponse
from ai_agent.llm.client import ask

class ChatService:
    async def handle_chat(self, request: ChatRequest) -> ChatResponse:
        """
        Endpoint to handle chat requests.
        """
        reply_message = await ask(request.message)
        return ChatResponse(session_id=request.session_id, reply=reply_message)