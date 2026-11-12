import asyncio

from app.llms.client import LLMClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    try:
        client = LLMClient(
            model="groq/openai/gpt-oss-20b"
        )

        messages = [
            {
                "role": "user",
                "content": "Explain what an AI agent is in one sentence."
            }
        ]

        response = await client.generate(messages)

        print(response.choices[0].message.content)

    finally:
        from litellm.llms.custom_httpx.async_client_cleanup import (
            close_litellm_async_clients
        )

        await close_litellm_async_clients()

if __name__ == "__main__":
    asyncio.run(main())