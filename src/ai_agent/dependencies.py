from ai_agent.services.chat_service import ChatService
from ai_agent.services.session_store import SessionStore

_session_store = SessionStore()
_chat_service = ChatService(session_store=_session_store)


def get_chat_service() -> ChatService:
    return _chat_service