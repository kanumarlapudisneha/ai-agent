from ai_agent.schemas.chat import ChatRequest, ChatResponse
from ai_agent.llm.client import ask

class ChatService:
    def __init__(self, session_store):
        self.session_store = session_store

    async def handle_chat(self, request: ChatRequest) -> ChatResponse:
        """
        Endpoint to handle chat requests.
        # 1. get this session's history from self.session_store
        # 2. call ask(), passing request.message AND the history
        # 3. record this turn (add_turn) so it's there for next time
        # 4. return the ChatResponse, same as before
        """
        history = self.session_store.get_history(request.session_id)
        reply_message = await ask(request.message, history = history)
        self.session_store.add_turn(request.session_id, request.message, reply_message)
        return ChatResponse(session_id=request.session_id, reply=reply_message)