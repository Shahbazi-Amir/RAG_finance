
import os
from openai import OpenAI


class ArvanEmbedder:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "text-embedding-3-large"
    ):
        self.api_key = api_key or os.getenv("ARVAN_AI_API_KEY")
        self.base_url = base_url or os.getenv("ARVAN_EMBEDDING_URL")
        self.model = model

        if not self.api_key:
            raise ValueError("ARVAN_AI_API_KEY is not set")

        if not self.base_url:
            raise ValueError("ARVAN_EMBEDDING_URL is not set")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def embed_text(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding

    def embed_query(self, query: str) -> list[float]:
        return self.embed_text(query)
