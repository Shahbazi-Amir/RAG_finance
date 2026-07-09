
from pathlib import Path
from qdrant_client import QdrantClient


class QdrantRetriever:
    def __init__(
        self,
        vectorstore_path: str | Path,
        collection_name: str
    ):
        self.vectorstore_path = Path(vectorstore_path)
        self.collection_name = collection_name

        if not self.vectorstore_path.exists():
            raise FileNotFoundError(f"Vectorstore path not found: {self.vectorstore_path}")

        self.client = QdrantClient(
            path=str(self.vectorstore_path)
        )

    def search(self, query_vector: list[float], top_k: int = 5) -> list[dict]:
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
            with_payload=True
        )

        retrieved_chunks = []

        for point in results.points:
            payload = point.payload or {}

            retrieved_chunks.append({
                "score": point.score,
                "chunk_id": payload.get("chunk_id"),
                "article_id": payload.get("article_id"),
                "chunk_index": payload.get("chunk_index"),
                "title": payload.get("title"),
                "url": payload.get("url"),
                "text": payload.get("text"),
                "char_count": payload.get("char_count")
            })

        return retrieved_chunks
