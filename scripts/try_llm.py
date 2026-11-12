import asyncio
from ai_agent.llm.client import ask


async def main():
    reply = await ask("Say hello in exactly five words.")
    print(reply)


asyncio.run(main())