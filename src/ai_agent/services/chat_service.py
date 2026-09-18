from ai_agent.schemas.chat import ChatRequest, ChatResponse

class ChatService:
    async def handle_chat(self, request: ChatRequest) -> ChatResponse:
        """
        Endpoint to handle chat requests.
        """
        reply_message = f"Received your message: {request.message}"
        return ChatResponse(session_id=request.session_id, reply=reply_message)