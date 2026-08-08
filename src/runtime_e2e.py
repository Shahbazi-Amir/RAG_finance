from __future__ import annotations

import json
import os
import shutil
from pathlib import Path


QUESTION = "سواد مالی یعنی چه؟"
COLLECTION_NAME = "financial_knowledge_base"


def run_runtime_e2e(result_file: Path, data_root: Path) -> None:
    """Run a real packaged RAG request and persist it through the production DB."""
    from src.database.database import initialize_database, save_conversation
    from src.pipeline.rag_pipeline import RAGPipeline

    source = Path(os.environ["RAG_FINANCE_RESOURCE_ROOT"]) / "resources" / "qdrant_local"
    test_root = data_root / "runtime-e2e"
    vectorstore = test_root / "qdrant_local"
    shutil.rmtree(test_root, ignore_errors=True)
    shutil.copytree(source, vectorstore)

    pipeline = None
    try:
        pipeline = RAGPipeline(
            vectorstore_path=vectorstore,
            collection_name=COLLECTION_NAME,
            cache_file=None,
            use_cache=False,
        )
        result = pipeline.ask(question=QUESTION, top_k=5)
        chunks = result.get("retrieved_chunks") or []
        answer = (result.get("answer") or "").strip()
        if not chunks or not answer:
            raise RuntimeError("real RAG result was incomplete")

        initialize_database()
        row_id = save_conversation(
            session_id="windows-ci-e2e",
            question=QUESTION,
            rewritten_question=None,
            answer=answer,
            sources=result.get("sources") or [],
            from_cache=False,
            model_name=result.get("generation_model"),
            response_time_ms=None,
        )
        payload = {
            "embedding": "PASS",
            "retrieval": "PASS",
            "retrieved_chunks": len(chunks),
            "generation": "PASS",
            "answer_non_empty": True,
            "history_row_id": row_id,
        }
    except Exception as exc:
        payload = {"error_type": type(exc).__name__, "status": "FAIL"}
    finally:
        if pipeline is not None:
            pipeline.close()
        shutil.rmtree(test_root, ignore_errors=True)

    result_file.parent.mkdir(parents=True, exist_ok=True)
    result_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
