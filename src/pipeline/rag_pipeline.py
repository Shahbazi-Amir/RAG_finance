
from pathlib import Path

from src.embeddings.arvan_embedder import ArvanEmbedder
from src.retrieval.qdrant_retriever import QdrantRetriever
from src.generation.arvan_generator import ArvanGenerator
from src.cache.rag_cache import RAGCache


class RAGPipeline:
    def __init__(
        self,
        vectorstore_path: str | Path,
        collection_name: str,
        cache_file: str | Path | None = None,
        embedding_model: str = "text-embedding-3-large",
        generation_model: str = "Qwen3-30B-A3B",
        use_cache: bool = True
    ):
        self.embedding_model = embedding_model
        self.generation_model = generation_model
        self.use_cache = use_cache

        self.embedder = ArvanEmbedder(
            model=self.embedding_model
        )

        self.retriever = QdrantRetriever(
            vectorstore_path=vectorstore_path,
            collection_name=collection_name
        )

        self.generator = ArvanGenerator(
            model=self.generation_model
        )

        self.cache = RAGCache(cache_file) if cache_file else None

    def build_context(self, retrieved_chunks: list[dict]) -> str:
        context_parts = []

        for i, item in enumerate(retrieved_chunks, start=1):
            part = f"""
[منبع {i}]
عنوان: {item["title"]}
آدرس: {item["url"]}
شناسه چانک: {item["chunk_id"]}

متن:
{item["text"]}
"""
            context_parts.append(part.strip())

        separator = "\n\n" + ("-" * 80) + "\n\n"
        return separator.join(context_parts)

    def format_sources(self, retrieved_chunks: list[dict]) -> list[dict]:
        sources = []
        seen = set()

        for item in retrieved_chunks:
            key = item.get("url") or item.get("title")

            if key in seen:
                continue

            seen.add(key)

            sources.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "chunk_id": item.get("chunk_id"),
                "score": item.get("score")
            })

        return sources

    def ask(self, question: str, top_k: int = 5) -> dict:
        if self.use_cache and self.cache:
            cached_item = self.cache.get(question)

            if cached_item:
                cached_item["from_cache"] = True
                return cached_item

        query_vector = self.embedder.embed_query(question)

        retrieved_chunks = self.retriever.search(
            query_vector=query_vector,
            top_k=top_k
        )

        context = self.build_context(retrieved_chunks)

        answer = self.generator.generate_answer(
            question=question,
            context=context
        )

        sources = self.format_sources(retrieved_chunks)

        result = {
            "question": question,
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": retrieved_chunks,
            "top_k": top_k,
            "embedding_model": self.embedding_model,
            "generation_model": self.generation_model,
            "from_cache": False
        }

        if self.use_cache and self.cache:
            result = self.cache.set(
                question=question,
                answer=answer,
                sources=sources,
                retrieved_chunks=retrieved_chunks,
                top_k=top_k,
                embedding_model=self.embedding_model,
                generation_model=self.generation_model
            )
            result["from_cache"] = False

        return result

    def close(self):
        try:
            self.retriever.client.close()
        except Exception:
            pass
