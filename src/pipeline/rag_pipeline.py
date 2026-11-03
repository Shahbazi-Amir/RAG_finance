
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

        insufficient_message = "در منابع موجود پاسخ کافی پیدا نشد."

        if answer.strip() == insufficient_message:
            sources = []
            retrieved_chunks_for_output = []
        else:
            sources = self.format_sources(retrieved_chunks)
            retrieved_chunks_for_output = retrieved_chunks

        result = {
            "question": question,
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": retrieved_chunks_for_output,
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


    def ask_with_char_rrf(
        self, question, *, candidate_id, rank_sources, write_receipt, top_k=10
    ):
        """Run an explicitly supplied char_rrf route and persist its input receipt."""
        import hashlib

        def text_sha(text):
            return hashlib.sha256(text.encode("utf-8")).hexdigest()

        if not isinstance(question, str) or not question.strip():
            raise ValueError("CHAR_RRF_QUESTION_REQUIRED")
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            raise ValueError("CHAR_RRF_CANDIDATE_ID_REQUIRED")
        if type(top_k) is not int or top_k < 1:
            raise ValueError("CHAR_RRF_INVALID_TOP_K")

        ranked = rank_sources(question=question, candidate_id=candidate_id, top_k=top_k)
        if (
            ranked["selected_variant"] != "char_rrf"
            or ranked["candidate_id"] != candidate_id
            or ranked["question_sha256"] != text_sha(question)
            or not isinstance(ranked["runtime_identity"], dict)
            or not ranked["runtime_identity"]
        ):
            raise ValueError("CHAR_RRF_RANK_RECEIPT_IDENTITY_MISMATCH")

        chunks = ranked["ordered_chunks"]
        if not isinstance(chunks, list) or not 0 < len(chunks) <= top_k:
            raise ValueError("CHAR_RRF_INVALID_CHUNK_COUNT")
        ids = [chunk["chunk_id"] for chunk in chunks]
        if any(not isinstance(value, str) or not value for value in ids):
            raise ValueError("CHAR_RRF_INVALID_CHUNK_ID")
        if len(set(ids)) != len(ids):
            raise ValueError("CHAR_RRF_DUPLICATE_CHUNK_ID")

        context = self.build_context(chunks)
        input_receipt = {
            "candidate_id": candidate_id,
            "question_sha256": text_sha(question),
            "selected_variant": "char_rrf",
            "runtime_identity": ranked["runtime_identity"],
            "ordered_chunk_ids": ids,
            "ordered_chunk_text_sha256": [text_sha(chunk["text"]) for chunk in chunks],
            "rendered_context_sha256": text_sha(context),
        }
        input_sha = write_receipt("input", input_receipt)
        if (
            not isinstance(input_sha, str)
            or len(input_sha) != 64
            or any(char not in "0123456789abcdef" for char in input_sha)
        ):
            raise ValueError("CHAR_RRF_INPUT_RECEIPT_HASH_REQUIRED")

        answer = self.generator.generate_answer(question=question, context=context)
        output_sha = write_receipt("output", {
            "input_receipt_file_bytes_sha256": input_sha,
            "answer_text_utf8_sha256": text_sha(answer),
        })
        return {
            "question": question,
            "answer": answer,
            "sources": [] if answer.strip() == "در منابع موجود پاسخ کافی پیدا نشد."
                       else self.format_sources(chunks),
            "selected_variant": "char_rrf",
            "input_receipt_file_bytes_sha256": input_sha,
            "output_receipt_file_bytes_sha256": output_sha,
            "from_cache": False,
        }

    def close(self):
        try:
            self.retriever.client.close()
        except Exception:
            pass
