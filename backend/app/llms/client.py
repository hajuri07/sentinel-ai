from litellm import acompletion


class LLMClient:

    def __init__(self, model: str, timeout: int = 30):
        self.model = model
        self.timeout = timeout

    async def generate(self, messages: list):
        try:
            response = await acompletion(
                model=self.model,
                messages=messages,
                timeout=self.timeout
            )
            return response
        except Exception as e:
            raise RuntimeError(f"Error generating response: {e}")   

        