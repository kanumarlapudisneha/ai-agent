from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from ai_agent.config import settings

model = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's question prescisely and concisely."),
    ("user", "{message}"),
])

chain = prompt | model


async def ask(message: str) -> str:
    result = await chain.ainvoke({"message": message})
    print(f"Result: {result}")
    return result.content