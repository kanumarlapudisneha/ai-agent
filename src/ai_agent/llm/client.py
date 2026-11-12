from openai import AsyncOpenAI
from ai_agent.config import settings

client = AsyncOpenAI(api_key=settings.openai_api_key)


async def ask(message: str) -> str:
    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=[{"role": "user", "content": message}],
    )
    print(f"response:: {response}")
    return response.choices[0].message.content