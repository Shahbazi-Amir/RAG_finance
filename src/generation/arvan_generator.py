
import os
from openai import OpenAI


class ArvanGenerator:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        temperature: float = 0.2
    ):
        self.api_key = api_key or os.getenv("ARVAN_CHAT_API_KEY") or os.getenv("ARVAN_AI_API_KEY")
        self.base_url = base_url or os.getenv("ARVAN_CHAT_URL")
        self.model = model or os.getenv("ARVAN_CHAT_MODEL") or "Qwen3-30B-A3B"
        self.temperature = temperature

        if not self.api_key:
            raise ValueError("ARVAN_CHAT_API_KEY or ARVAN_AI_API_KEY is not set")

        if not self.base_url:
            raise ValueError("ARVAN_CHAT_URL is not set")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def generate_answer(self, question: str, context: str) -> str:
        system_prompt = """
تو یک دستیار مالی فارسی هستی.
فقط بر اساس منابع داده‌شده پاسخ بده.
اگر پاسخ در منابع نبود، دقیقاً بگو: «در منابع موجود پاسخ کافی پیدا نشد.»
پاسخ را کوتاه، دقیق و روان بنویس.
"""

        user_prompt = f"""
سؤال:
{question}

منابع:
{context}

پاسخ:
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": user_prompt.strip()}
            ],
            temperature=self.temperature
        )

        return response.choices[0].message.content.strip()
