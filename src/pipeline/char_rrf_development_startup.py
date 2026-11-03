"""Offline opt-in startup for one pinned Development question."""

import hashlib
import json
import os
from pathlib import Path

from .char_rrf_route import ask_product_char_rrf
from .rag_pipeline import RAGPipeline


REPORTS = Path("reports/phase2/quality_improvement/NB22E.lab.v3")
C138 = "1df8a9e4c0fcc6a4bfcce4edb4356f2557f71e312aed48f501b89a8c5464e910"
C139 = "3b5a43d5476dc28de79eed5fc35adc6e2a6834bbd9c6a341c8efa93b18669634"


def require(ok, code):
    if not ok:
        raise ValueError(code)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def text_sha(text):
    return sha(text.encode("utf-8"))


def run_offline(root):
    root = Path(root).resolve()

    def project_path(relative):
        relative = Path(relative)
        path = (root / relative).resolve()
        require(not relative.is_absolute() and path.is_relative_to(root),
                "C140_PATH_OUTSIDE_PROJECT")
        return path

    def read(relative, digest):
        raw = project_path(relative).read_bytes()
        require(sha(raw) == digest, f"C140_HASH_CONFLICT:{relative}")
        return raw

    def load(receipt):
        return json.loads(read(receipt["path"], receipt["file_bytes_sha256"]))

    def report(stem, digest):
        return json.loads(read(REPORTS / f"{stem}.{digest}.json", digest))

    def save(stem, value):
        raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                         indent=2, allow_nan=False).encode("utf-8")
        digest = sha(raw)
        relative = REPORTS / f"{stem}.{digest}.json"
        path = project_path(relative)
        try:
            with path.open("xb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
        except FileExistsError:
            pass
        require(path.read_bytes() == raw, "C140_RECEIPT_RELOAD_CONFLICT")
        return {"path": relative.as_posix(), "file_bytes_sha256": digest,
                "reload_validation": "PASS"}

    route = report("C139.R11_persisted_opt_in_caller", C139)
    prior = report("C138.R11_constructed_product_instance_local_rank_chain", C138)
    require(
        route["status"] == "OPT_IN_CALLER_PERSISTED_IN_PRODUCT_SOURCE"
        and route["input_file_hashes"]["C138"] == C138
        and prior["status"] == "CONSTRUCTED_PRODUCT_INSTANCE_LOCAL_RANK_CHAIN_PASSED",
        "C140_PRIOR_EVIDENCE_CONFLICT",
    )
    route_file = route["module"]
    read(route_file["path"], route_file["file_bytes_sha256"])
    pipeline_sha = prior["input_file_hashes"]["pipeline_source"]
    require(pipeline_sha == route["input_file_hashes"]["pipeline_source"],
            "C140_PIPELINE_PIN_CONFLICT")
    read("src/pipeline/rag_pipeline.py", pipeline_sha)

    candidate = prior["candidate_id"]
    question_sha = prior["question_sha256"]
    reference = load(prior["receipts"]["input"])
    hybrid_ref = prior["hybrid100_probe_receipt"]
    hybrid = load(hybrid_ref)
    pool_report = report("C135.R11_versioned_pool50_provider",
                         prior["input_file_hashes"]["C135"])
    pool_ref = pool_report["provider_receipt"]
    pool = load(pool_ref)

    for record in (reference, hybrid, pool_report, pool):
        require((record["candidate_id"], record["question_sha256"])
                == (candidate, question_sha), "C140_QUERY_BINDING_CONFLICT")

    hybrid_ids = hybrid["observed_hybrid100_order"]
    pool_ids = pool["ordered_chunk_ids"]
    pool_scores = pool["scores_by_chunk_id"]
    top10 = reference["ordered_chunk_ids"]
    require(
        hybrid["full_hybrid100_order_matches"] is True
        and len(hybrid_ids) == len(set(hybrid_ids)) == 100
        and hybrid_ids == pool["hybrid100_order"]
        and len(pool_ids) == len(set(pool_ids)) == 50
        and set(pool_ids) == set(hybrid_ids[:50]) == set(pool_scores)
        and len(top10) == len(set(top10)) == 10
        and reference["selected_variant"] == "char_rrf",
        "C140_RANK_INPUT_CONFLICT",
    )

    c129 = report("C129.R11_local_hybrid100_opt_in_integration",
                  prior["input_file_hashes"]["C129"])

    def select_rows(path, digest, key, wanted):
        selected = {}
        for line in read(path, digest).splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            identity = row[key]
            if identity in wanted:
                require(identity not in selected, f"C140_DUPLICATE_ROW:{key}")
                selected[identity] = row
        require(set(selected) == wanted, f"C140_ROW_MISSING:{key}")
        return selected

    question_row = select_rows(
        "artifacts/phase2/golden_dataset_v2/golden_dataset_v2.jsonl",
        c129["input_file_hashes"]["golden"], "candidate_id", {candidate},
    )[candidate]
    question = question_row["evaluation_content"]["question"].strip()
    require(text_sha(question) == question_sha, "C140_QUESTION_HASH_CONFLICT")

    corpus = select_rows(
        "data/phase2/chunks/nb11_benchmark_v1/baseline_phase1_char_safe_v1.jsonl",
        c129["input_file_hashes"]["chunks"], "chunk_id", set(top10),
    )
    chunks = [
        {"chunk_id": cid, "text": corpus[cid]["content"],
         "title": corpus[cid].get("title"), "url": corpus[cid].get("url")}
        for cid in top10
    ]
    require([text_sha(chunk["text"]) for chunk in chunks]
            == reference["ordered_chunk_text_sha256"], "C140_CHUNK_TEXT_CONFLICT")

    events = []
    receipts = {}

    def query_check(question, candidate_id):
        require((candidate_id, text_sha(question)) == (candidate, question_sha),
                "C140_PROVIDER_QUERY_CONFLICT")

    def hybrid_provider(*, question, candidate_id):
        query_check(question, candidate_id)
        events.append("hybrid100_receipt_supplied")
        return {"candidate_id": candidate, "question_sha256": question_sha,
                "ordered_chunk_ids": list(hybrid_ids),
                "receipt_sha256": hybrid_ref["file_bytes_sha256"]}

    def pool_provider(*, question, candidate_id, hybrid100):
        query_check(question, candidate_id)
        require(list(hybrid100) == hybrid_ids, "C140_POOL50_HYBRID_CONFLICT")
        events.append("pool50_receipt_supplied")
        return {"candidate_id": candidate, "question_sha256": question_sha,
                "ordered_chunk_ids": list(pool_ids), "scores_by_chunk_id": dict(pool_scores),
                "receipt_sha256": pool_ref["file_bytes_sha256"]}

    def rank_provider(*, question, candidate_id, top_k, hybrid100,
                      pool50_order, pool50_scores):
        query_check(question, candidate_id)
        require(top_k == 10 and list(hybrid100) == hybrid_ids
                and list(pool50_order) == pool_ids and pool50_scores == pool_scores,
                "C140_FINAL_RANK_INPUT_CONFLICT")
        events.append("fixed_final_order_supplied")
        return {
            "candidate_id": candidate,
            "question_sha256": question_sha,
            "selected_variant": "char_rrf",
            "runtime_identity": {
                "scope": "STANDALONE_DEVELOPMENT_FIXED_INPUT_STUB",
                "pipeline_source_sha256": pipeline_sha,
                "route_source_sha256": route_file["file_bytes_sha256"],
                "reference_run_sha256": C138,
            },
            "ordered_chunks": chunks,
        }

    def write_receipt(role, payload):
        require(role in {"input", "output"} and role not in receipts,
                "C140_RECEIPT_ROLE_CONFLICT")
        receipts[role] = save(f"C140.R11_startup_{role}_receipt", payload)
        events.append(f"{role}_receipt_written")
        return receipts[role]["file_bytes_sha256"]

    answer = "در منابع موجود پاسخ کافی پیدا نشد."

    class OfflineGenerator:
        def generate_answer(self, *, question, context):
            query_check(question, candidate)
            require("input" in receipts and "output" not in receipts,
                    "C140_PRE_GENERATION_RECEIPT_REQUIRED")
            recorded = load(receipts["input"])
            require(
                recorded["candidate_id"] == candidate
                and recorded["question_sha256"] == question_sha
                and recorded["ordered_chunk_ids"] == top10
                and recorded["ordered_chunk_text_sha256"]
                    == reference["ordered_chunk_text_sha256"]
                and recorded["rendered_context_sha256"] == text_sha(context)
                    == reference["rendered_context_sha256"]
                and recorded["runtime_identity"]["pool50_provider_receipt_sha256"]
                    == pool_ref["file_bytes_sha256"]
                and recorded["runtime_identity"]["hybrid100_provider_receipt_sha256"]
                    == hybrid_ref["file_bytes_sha256"],
                "C140_PRE_GENERATION_RECEIPT_CONFLICT",
            )
            events.append("stub_verified_persisted_input")
            return answer

    storage = project_path(prior["dense_storage_path"])
    require(storage.is_dir(), "C140_DENSE_STORAGE_REQUIRED")
    pipeline = RAGPipeline(
        vectorstore_path=storage,
        collection_name=prior["dense_collection"],
        use_cache=False,
    )
    try:
        pipeline.generator = OfflineGenerator()
        response = ask_product_char_rrf(
            pipeline, question=question, candidate_id=candidate,
            hybrid100_provider=hybrid_provider, pool50_provider=pool_provider,
            rank_provider=rank_provider, write_receipt=write_receipt, top_k=10,
        )
    finally:
        pipeline.close()

    input_sha = receipts["input"]["file_bytes_sha256"]
    output_sha = receipts["output"]["file_bytes_sha256"]
    output = load(receipts["output"])
    require(
        events == [
            "hybrid100_receipt_supplied", "pool50_receipt_supplied",
            "fixed_final_order_supplied", "input_receipt_written",
            "stub_verified_persisted_input", "output_receipt_written",
        ]
        and response["answer"] == answer and response["sources"] == []
        and response["from_cache"] is False
        and response["input_receipt_file_bytes_sha256"] == input_sha
        and response["output_receipt_file_bytes_sha256"] == output_sha
        and output["input_receipt_file_bytes_sha256"] == input_sha
        and output["answer_text_utf8_sha256"] == text_sha(answer),
        "C140_OUTPUT_OR_EVENT_ORDER_CONFLICT",
    )
    result = {
        "cell": "C140",
        "roadmap_action": "R11",
        "roadmap_subtask": "R11.3",
        "status": "STANDALONE_FIXED_INPUT_STARTUP_PASSED",
        "candidate_id": candidate,
        "question_sha256": question_sha,
        "input_file_hashes": {"C138": C138, "C139": C139},
        "startup_module_sha256": sha(Path(__file__).read_bytes()),
        "events": events,
        "receipts": receipts,
        "product_constructor_executed": True,
        "product_runtime_binding_verified": False,
        "product_regression_tests_executed": 0,
        "qdrant_queries_attempted": 0,
        "new_local_pairs_scored": 0,
        "new_api_calls": 0,
        "done_item_count": 7,
        "open_item_count": 5,
        "newly_completed_items_from_previous_open_set": [],
        "selected_version_gate": "BLOCKED",
        "next_product_dependency": "PERSIST_COMPUTATIONAL_RANK_PROVIDERS_FOR_STANDALONE_STARTUP",
    }
    result["output"] = save("C140.R11_standalone_fixed_input_startup", result)
    return result


if __name__ == "__main__":
    print(json.dumps(run_offline(Path.cwd()), ensure_ascii=False, indent=2))
