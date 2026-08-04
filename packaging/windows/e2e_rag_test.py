from __future__ import annotations

import argparse
import os
import shutil
import tempfile
from pathlib import Path

from dotenv import dotenv_values, load_dotenv

from src.pipeline.rag_pipeline import RAGPipeline


QUESTION = "سواد مالی یعنی چه؟"
COLLECTION_NAME = "financial_knowledge_base"
REQUIRED_KEYS = {
    "ARVAN_AI_API_KEY",
    "ARVAN_EMBEDDING_URL",
    "ARVAN_CHAT_URL",
}
FORBIDDEN_KEYS = {
    "GITHUB_TOKEN",
    "GH_TOKEN",
    "ACTIONS_RUNTIME_TOKEN",
    "ACTIONS_ID_TOKEN_REQUEST_TOKEN",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distribution-root", required=True)
    args = parser.parse_args()

    distribution_root = Path(args.distribution_root).resolve()
    env_file = distribution_root / ".env"
    seed = distribution_root / "_internal" / "resources" / "qdrant_local"

    values = dotenv_values(env_file)
    missing = sorted(name for name in REQUIRED_KEYS if not values.get(name))
    if missing:
        raise SystemExit("Runtime config is missing required key names: " + ", ".join(missing))
    if not (values.get("ARVAN_CHAT_API_KEY") or values.get("ARVAN_AI_API_KEY")):
        raise SystemExit("Runtime config has no chat API credential.")
    leaked = sorted(FORBIDDEN_KEYS.intersection(values))
    if leaked:
        raise SystemExit("Forbidden CI credential key found in runtime config: " + ", ".join(leaked))

    load_dotenv(env_file, override=True)
    print("Runtime config: PASS")

    temp_root = Path(tempfile.mkdtemp(prefix="rag-finance-e2e-"))
    pipeline = None
    stage = "seed preparation"
    try:
        vectorstore = temp_root / "qdrant_local"
        shutil.copytree(seed, vectorstore)

        stage = "pipeline initialization"
        pipeline = RAGPipeline(
            vectorstore_path=vectorstore,
            collection_name=COLLECTION_NAME,
            cache_file=None,
            use_cache=False,
        )

        stage = "real RAG query"
        result = pipeline.ask(question=QUESTION, top_k=5)

        chunks = result.get("retrieved_chunks") or []
        if not chunks:
            raise RuntimeError("retrieval returned no chunks")
        if not any((item.get("text") or "").strip() for item in chunks):
            raise RuntimeError("retrieval returned no useful text")

        answer = (result.get("answer") or "").strip()
        if not answer:
            raise RuntimeError("generation returned an empty answer")

        print("Embedding request: PASS")
        print("Retrieval: PASS")
        print(f"Retrieved chunks: {len(chunks)}")
        print("Generation request: PASS")
        print(f"Answer length: {len(answer)}")
        print("End-to-end RAG: PASS")
        return 0
    except Exception as exc:
        raise SystemExit(f"End-to-end RAG failed during {stage}: {type(exc).__name__}") from None
    finally:
        if pipeline is not None:
            pipeline.close()
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
