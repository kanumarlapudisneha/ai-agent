from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from ai_agent.config import settings

model = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's question prescisely and concisely."),
    MessagesPlaceholder("history"),
    ("user", "{message}"),
])

chain = prompt | model


async def ask(message: str, history: list) -> str:
    print(f"History going in ({len(history)} messages): {history}")
    result = await chain.ainvoke({"message": message, "history": history})
    print(f"Tokens used: {result.usage_metadata}")
    return result.content