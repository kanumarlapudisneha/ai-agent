from langchain_core.messages import BaseMessage, HumanMessage, AIMessage


class SessionStore:
    def __init__(self):
        self._sessions: dict[str, list[BaseMessage]] = {}

    def get_history(self, session_id: str) -> list[BaseMessage]:
        print(f"Getting history for session_id: {session_id}")
        return self._sessions.setdefault(session_id, [])

    def add_turn(self, session_id: str, user_message: str, ai_message: str) -> None:
        history = self.get_history(session_id)
        print(f"Adding turn to session_id: {session_id}, user_message: {user_message}, ai_message: {ai_message}")
        history.append(HumanMessage(content=user_message))
        history.append(AIMessage(content=ai_message))