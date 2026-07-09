
import json
import hashlib
from pathlib import Path
from datetime import datetime


class RAGCache:
    def __init__(self, cache_file: str | Path):
        self.cache_file = Path(cache_file)
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.cache_file.exists():
            self.save_cache({})

    def normalize_question(self, question: str) -> str:
        return " ".join(question.strip().lower().split())

    def make_question_hash(self, question: str) -> str:
        normalized = self.normalize_question(question)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def load_cache(self) -> dict:
        with open(self.cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_cache(self, cache: dict):
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

    def get(self, question: str):
        question_hash = self.make_question_hash(question)
        cache = self.load_cache()
        return cache.get(question_hash)

    def set(
        self,
        question: str,
        answer: str,
        sources: list,
        retrieved_chunks: list,
        top_k: int,
        embedding_model: str,
        generation_model: str
    ):
        question_hash = self.make_question_hash(question)
        cache = self.load_cache()

        cache[question_hash] = {
            "question": question,
            "question_hash": question_hash,
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": retrieved_chunks,
            "top_k": top_k,
            "embedding_model": embedding_model,
            "generation_model": generation_model,
            "created_at": datetime.now().isoformat()
        }

        self.save_cache(cache)

        return cache[question_hash]
