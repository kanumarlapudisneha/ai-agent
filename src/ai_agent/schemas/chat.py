from pydantic import BaseModel

class ChatRequest(BaseModel):
    """
    Schema for a chat request.
    """
    session_id: str
    message: str

class ChatResponse(BaseModel):
    """
    Schema for a chat response.
    """
    session_id: str
    reply: str
