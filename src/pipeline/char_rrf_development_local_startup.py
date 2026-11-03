"""Offline opt-in startup for one pinned Development question."""

import hashlib
import json
import os
from pathlib import Path

import ast
import collections
import copy
import dataclasses
import importlib.metadata
import math
import platform
import re
import statistics
import sys
import time
import unicodedata

import numpy as np
import onnxruntime as ort
import pandas as pd
import scipy
from qdrant_client import QdrantClient, models as qdrant_models
from transformers import AutoTokenizer

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


def run_v3_c120():
    def require(ok, code):
        if not ok:
            raise ValueError(code)

    def sha(raw):
        return hashlib.sha256(raw).hexdigest()

    reports = Path("reports/phase2/quality_improvement/NB22E.lab.v3")
    root = next(
        (p for p in (Path.cwd(), *Path.cwd().parents) if (p / reports).is_dir()),
        None,
    )
    require(root is not None, "C120_PROJECT_ROOT_NOT_FOUND")
    root = root.resolve()

    def read_bound(relative, digest, *, key=None):
        relative = Path(relative)
        path = (root / relative).resolve()
        require(
            not relative.is_absolute() and path.is_relative_to(root),
            "C120_PATH_OUTSIDE_PROJECT",
        )
        raw = path.read_bytes()
        require(sha(raw) == digest, f"C120_HASH_CONFLICT:{relative}")
        if key is None:
            return json.loads(raw)
        rows = {}
        for line in raw.splitlines():
            if line.strip():
                row = json.loads(line)
                identity = row[key]
                require(identity not in rows, f"C120_DUPLICATE_ID:{relative}:{identity}")
                rows[identity] = row
        return rows

    def ordered_ids(row, depth):
        candidates = row["candidates"]
        require(len(candidates) == depth, f"C120_DEPTH_CONFLICT:{depth}")
        require(
            [r["rank"] for r in candidates] == list(range(1, depth + 1)),
            f"C120_RANK_ORDER_CONFLICT:{depth}",
        )
        ids = [r["chunk_id"] for r in candidates]
        require(len(set(ids)) == depth, f"C120_DUPLICATE_CHUNK:{depth}")
        return ids

    c119_sha = "967178107d6a4fab03ecb5ffd74f79ceebfd716dc265d9726339164d06a3647b"
    prior = read_bound(
        reports / f"C119.R11_local100_four_pair_parity.{c119_sha}.json",
        c119_sha,
    )
    require(
        prior["score_parity_verified"] is True
        and prior["same_query_hybrid100_and_scored_pool50_bound"] is True,
        "C120_C119_PARITY_REQUIRED",
    )

    pins = prior["input_file_hashes"]
    candidate = prior["sample_candidate_id"]
    result = {
        "cell": "C120",
        "roadmap_action": "R11",
        "roadmap_subtask": "R11.3",
        "scope": "ONE_DEVELOPMENT_QUERY_PINNED_STORED_INPUTS",
        "candidate_id": candidate,
        "input_file_hashes": {"C119": c119_sha, **pins},
        "new_api_calls": 0,
        "model_inference_calls_attempted": 0,
        "new_local_pairs_scored": 0,
        "target_case_rankings_reconstructed": 0,
        "product_runtime_binding_verified": False,
        "product_regression_tests_executed": 0,
        "done_item_count": 7,
        "open_item_count": 5,
        "newly_completed_items_from_previous_open_set": [],
        "historical_gate": "FAIL",
        "selected_version_gate": "BLOCKED",
    }

    stage = "PINNED_INPUTS"
    try:
        c056_sha = pins["NB22_C056"]
        c056 = read_bound(
            Path("reports/phase2/release/NB22.C056.retrieval_verification")
            / f"C056.independent_retrieval_metric_verification.{c056_sha}.json",
            c056_sha,
        )
        inputs = {}
        for role, key in (
            ("golden", "candidate_id"),
            ("hybrid", "candidate_id"),
            ("reranker", "candidate_id"),
            ("chunks", "chunk_id"),
        ):
            receipt = c056["input_file_receipts"][role]
            require(receipt["file_bytes_sha256"] == pins[role], f"C120_PIN_CONFLICT:{role}")
            inputs[role] = read_bound(receipt["path"], pins[role], key=key)

        hrow = inputs["hybrid"][candidate]
        rrow = inputs["reranker"][candidate]
        require(hrow["split"] == "development", "C120_DEVELOPMENT_REQUIRED")
        hybrid_ids = ordered_ids(hrow, 100)
        pool_ids = ordered_ids(rrow, 50)
        require(set(hybrid_ids[:50]) == set(pool_ids), "C120_POOL50_MEMBERSHIP_CONFLICT")

        question = inputs["golden"][candidate]["evaluation_content"]["question"].strip()
        question_sha = sha(question.encode("utf-8"))
        require(question_sha == prior["question_sha256"], "C120_QUESTION_HASH_CONFLICT")
        require(hybrid_ids[:4] == prior["pair_chunk_ids"], "C120_PARITY_PAIR_ID_CONFLICT")

        contents = {cid: inputs["chunks"][cid]["content"] for cid in hybrid_ids}
        content_hashes = {cid: sha(value.encode("utf-8")) for cid, value in contents.items()}
        require(
            [content_hashes[cid] for cid in hybrid_ids[:4]] == prior["pair_content_sha256"],
            "C120_PARITY_PAIR_TEXT_CONFLICT",
        )
        scores = {
            row["chunk_id"]: float(row["reranker_score"]) for row in rrow["candidates"]
        }
        require(
            [scores[cid] for cid in hybrid_ids[:4]] == prior["reference_scores"],
            "C120_PARITY_REFERENCE_SCORE_CONFLICT",
        )
        require(bool(np.isfinite(list(scores.values())).all()), "C120_INVALID_POOL50_SCORE")

        stage = "PINNED_LOCAL_RUNTIME"
        c118_sha = pins["C118"]
        preflight = read_bound(
            reports / f"C118.R11_local100_model_preflight.{c118_sha}.json",
            c118_sha,
        )
        config = preflight["expected_runtime"]
        runtime = globals().get("ort") or globals().get("onnxruntime")
        require(runtime is not None, "C120_C001_ONNXRUNTIME_BINDING_MISSING")
        require(
            runtime.__version__ == config["onnxruntime_version"],
            "C120_ONNXRUNTIME_VERSION_CONFLICT",
        )
        require(
            (config["batch_size"], config["maximum_sequence_length"]) == (4, 512),
            "C120_INFERENCE_CONFIG_CONFLICT",
        )
        cache_root = Path(
            os.environ.get("HF_HUB_CACHE")
            or str(Path(os.environ.get("HF_HOME", str(Path.home() / ".cache/huggingface"))) / "hub")
        )
        snapshot = (
            cache_root / ("models--" + config["model_id"].replace("/", "--"))
            / "snapshots" / config["model_revision"]
        )
        model = snapshot / "onnx/model_quint8_avx2.onnx"
        require(sha(model.read_bytes()) == config["onnx_sha256"], "C120_MODEL_HASH_CONFLICT")
        tokenizer = AutoTokenizer.from_pretrained(
            str(snapshot), local_files_only=True, trust_remote_code=False
        )
        options = runtime.SessionOptions()
        options.intra_op_num_threads = 4
        options.inter_op_num_threads = 1
        options.execution_mode = runtime.ExecutionMode.ORT_SEQUENTIAL
        options.graph_optimization_level = runtime.GraphOptimizationLevel.ORT_ENABLE_ALL
        session = runtime.InferenceSession(
            str(model), sess_options=options, providers=["CPUExecutionProvider"]
        )
        names = {item.name for item in session.get_inputs()}
        require({"input_ids", "attention_mask"} <= names, "C120_ONNX_INPUT_CONTRACT")

        stage = "SCORE_MISSING_50"
        missing = [cid for cid in hybrid_ids if cid not in scores]
        require(len(missing) == 50, "C120_MISSING_PAIR_COUNT_CONFLICT")
        for start in range(0, len(missing), 4):
            batch = missing[start:start + 4]
            encoded = tokenizer(
                [question] * len(batch), [contents[cid] for cid in batch],
                padding=True, truncation=True, max_length=512, return_tensors="np",
            )
            require(names <= set(encoded), "C120_TOKENIZER_ONNX_INPUT_MISMATCH")
            feed = {name: np.asarray(encoded[name], dtype=np.int64) for name in names}
            result["model_inference_calls_attempted"] += 1
            values = np.asarray(session.run(None, feed)[0], dtype=np.float64).reshape(-1)
            require(
                values.shape == (len(batch),) and bool(np.isfinite(values).all()),
                "C120_INVALID_ONNX_SCORES",
            )
            scores.update({cid: float(value) for cid, value in zip(batch, values)})
            result["new_local_pairs_scored"] += len(batch)

        require(set(scores) == set(hybrid_ids), "C120_LOCAL100_CHUNK_SET_CONFLICT")
        local_ids = sorted(hybrid_ids, key=lambda cid: (-scores[cid], cid))
        result.update(
            status="ONE_DEVELOPMENT_LOCAL100_INPUT_BUILT",
            blocker=None,
            question_sha256=question_sha,
            hybrid100_order=hybrid_ids,
            scored_pool50_order=pool_ids,
            local100_order=local_ids,
            scores_by_chunk_id=scores,
            chunk_text_sha256_by_id=content_hashes,
            reused_pool50_score_count=50,
            local100_matches_saved_order_verified=False,
            next_product_dependency="COMPARE_WITH_SAVED_LOCAL100_AND_BIND_OPT_IN_PROVIDER",
        )
    except Exception as error:
        result.update(
            status="DEVELOPMENT_LOCAL100_INPUT_BLOCKED",
            blocker={"stage": stage, "type": type(error).__name__, "detail": str(error)},
        )

    raw = json.dumps(
        result, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False
    ).encode("utf-8")
    digest = sha(raw)
    relative = reports / f"C120.R11_development_local100_input.{digest}.json"
    path = root / relative
    try:
        with path.open("xb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        pass
    require(path.read_bytes() == raw, "C120_REPORT_RELOAD_CONFLICT")
    result["output"] = {
        "path": relative.as_posix(),
        "file_bytes_sha256": digest,
        "reload_validation": "PASS",
    }
    detail_fields = {
        "hybrid100_order", "scored_pool50_order", "local100_order",
        "scores_by_chunk_id", "chunk_text_sha256_by_id",
    }
    print(json.dumps(
        {key: value for key, value in result.items() if key not in detail_fields},
        ensure_ascii=False, indent=2,
    ))
    return result

def run_v3_c126():
    def require(ok, code):
        if not ok:
            raise ValueError(code)

    def sha(raw):
        return hashlib.sha256(raw).hexdigest()

    reports = Path("reports/phase2/quality_improvement/NB22E.lab.v3")
    root = next(
        (p for p in (Path.cwd(), *Path.cwd().parents) if (p / reports).is_dir()),
        None,
    )
    require(root is not None, "C126_PROJECT_ROOT_NOT_FOUND")
    root = root.resolve()

    def read_bound(relative, digest):
        path = (root / relative).resolve()
        require(path.is_relative_to(root), "C126_PATH_OUTSIDE_PROJECT")
        raw = path.read_bytes()
        require(sha(raw) == digest, f"C126_HASH_CONFLICT:{relative}")
        return raw

    nb_path = "notebooks/phase2/16_hybrid_retrieval.ipynb"
    nb_sha = "40699ca54c57fcef40472df6b6fc42a54f74dc2e9bdc9bb40e0ccc93bb7ad6a7"
    c120_sha = "33578338372385982a433939fbec3e140cac3495d0ef8228847cceb99ac05975"
    result = {
        "cell": "C126",
        "roadmap_action": "R11",
        "roadmap_subtask": "R11.3",
        "scope": "ONE_DEVELOPMENT_QUERY_LOCAL_NB16_ASSETS",
        "input_file_hashes": {"NB16": nb_sha, "C120": c120_sha},
        "full_hybrid100_order_matches": False,
        "product_runtime_binding_verified": False,
        "product_regression_tests_executed": 0,
        "new_api_calls": 0,
        "embedding_calls": 0,
        "qdrant_queries_attempted": 0,
        "target_case_rankings_reconstructed": 0,
        "rank_reconstruction_for_unverified_candidates": "DEFERRED",
        "done_item_count": 7,
        "open_item_count": 5,
        "newly_completed_items_from_previous_open_set": [],
        "historical_gate": "FAIL",
        "selected_version_gate": "BLOCKED",
    }

    # NB16 runs in an isolated namespace with dependencies from C001.
    scope = dict(globals())
    scope.pop("qdrant_client", None)
    scope.pop("development_cache_hit", None)
    stage = "VERIFY_PINNED_INPUTS"

    try:
        notebook = json.loads(read_bound(nb_path, nb_sha))
        prior = json.loads(read_bound(
            reports / f"C120.R11_development_local100_input.{c120_sha}.json",
            c120_sha,
        ))
        expected = prior["hybrid100_order"]
        candidate = prior["candidate_id"]
        require(
            prior["status"] == "ONE_DEVELOPMENT_LOCAL100_INPUT_BUILT"
            and len(expected) == len(set(expected)) == 100,
            "C126_INVALID_C120_REFERENCE",
        )
        result["candidate_id"] = candidate
        result["question_sha256"] = prior["question_sha256"]

        def parse_cell(index):
            cell = notebook["cells"][index]
            require(cell["cell_type"] == "code", f"C126_EXPECTED_CODE_CELL:{index}")
            return ast.parse("".join(cell["source"]), filename=f"{nb_path}:{index}")

        def execute_nodes(index, nodes):
            module = ast.Module(body=nodes, type_ignores=[])
            exec(compile(module, f"{nb_path}:{index}", "exec", optimize=0), scope)

        # Run the reviewed, read-only setup cells. Defer opening Qdrant
        # until the existing Development embedding cache has passed.
        for index in (3, 5, 7, 9, 11, 13):
            stage = f"NB16_SETUP_CELL_{index}"
            execute_nodes(index, parse_cell(index).body)

        require(
            Path(scope["PROJECT_ROOT"]).resolve() == root,
            "C126_NB16_PROJECT_ROOT_CONFLICT",
        )

        # The leading assignments in cell 15 define the dense contract.
        # The client creation and collection checks run later.
        stage = "READ_DENSE_RUNTIME_CONTRACT"
        dense_setup = parse_cell(15).body
        client_index = next(
            i for i, node in enumerate(dense_setup)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "qdrant_client"
                    for target in node.targets)
        )
        execute_nodes(15, dense_setup[:client_index])

        stage = "LOAD_EXISTING_DEVELOPMENT_CACHE"
        cache_nodes = parse_cell(17).body
        fallback = [
            i for i, node in enumerate(cache_nodes)
            if isinstance(node, ast.If)
            and isinstance(node.test, ast.UnaryOp)
            and isinstance(node.test.op, ast.Not)
            and isinstance(node.test.operand, ast.Name)
            and node.test.operand.id == "development_cache_hit"
        ]
        require(len(fallback) == 1, "C126_CACHE_FALLBACK_BOUNDARY_CONFLICT")
        # Execute only the source up to the branch that builds a new cache.
        execute_nodes(17, cache_nodes[:fallback[0]])
        require(
            scope["development_cache_hit"] is True,
            "C126_EXISTING_DEVELOPMENT_CACHE_REQUIRED",
        )

        ids = scope["development_candidate_ids_ordered"]
        require(len(ids) == len(set(ids)) == 2664 and candidate in ids,
                "C126_DEVELOPMENT_QUERY_POPULATION_CONFLICT")
        question = scope["development_query_by_candidate_id"][candidate]
        require(
            sha(question.strip().encode("utf-8")) == prior["question_sha256"],
            "C126_QUESTION_HASH_CONFLICT",
        )
        # NB16 originally embedded and analyzed the unstripped Golden text.
        row_index = ids.index(candidate)
        vectors = scope["development_query_embeddings"]
        np_local = scope["np"]
        require(vectors.shape == (len(ids), 384) and vectors.dtype == np_local.float32,
                "C126_CACHE_ARRAY_CONTRACT_CONFLICT")
        vector = vectors[row_index]
        require(bool(np_local.isfinite(vector).all())
                and bool(np_local.isclose(np_local.linalg.norm(vector), 1.0)),
                "C126_INVALID_QUERY_VECTOR")
        result.update(
            cache_row_index_zero_based=row_index,
            cache_key=scope["query_embedding_cache_key"],
            exact_nb16_question_sha256=sha(question.encode("utf-8")),
            query_vector_sha256=sha(vector.tobytes()),
        )
        for key in ("DEVELOPMENT_QUERY_EMBEDDINGS_PATH", "DEVELOPMENT_QUERY_METADATA_PATH"):
            path = Path(scope[key]).resolve()
            result["input_file_hashes"][key] = sha(path.read_bytes())

        stage = "OPEN_AND_VERIFY_LOCAL_QDRANT"
        dense_path = Path(scope["dense_storage_path"]).resolve()
        require(dense_path.is_relative_to(root) and dense_path.is_dir(),
                "C126_LOCAL_QDRANT_PATH_REQUIRED")
        execute_nodes(15, dense_setup[client_index:])
        result.update(
            dense_collection=scope["DENSE_COLLECTION_NAME"],
            dense_storage_path=dense_path.relative_to(root).as_posix(),
        )

        stage = "LOAD_PINNED_HYBRID_FUNCTIONS"
        names = {
            "frozen_bm25_scores", "frozen_sparse_retrieve", "frozen_dense_retrieve",
            "frozen_minmax_scores", "frozen_weighted_fusion",
        }
        definitions = [
            node for node in parse_cell(37).body
            if isinstance(node, ast.FunctionDef) and node.name in names
        ]
        require(len(definitions) == len(names), "C126_PINNED_DEFINITIONS_MISSING")
        scope.update(
            FROZEN_CANDIDATE_DEPTH=100,
            FROZEN_DENSE_WEIGHT=0.4,
            FROZEN_SPARSE_WEIGHT=0.6,
        )
        execute_nodes(37, definitions)

        stage = "RUN_AND_COMPARE_ONE_HYBRID_QUERY"
        sparse = scope["frozen_sparse_retrieve"](question, 100)
        result["qdrant_queries_attempted"] += 1
        dense = scope["frozen_dense_retrieve"](vector, 100)
        fused = scope["frozen_weighted_fusion"](
            dense["ranked_chunk_ids"], dense["ranked_scores"],
            sparse["ranked_chunk_ids"], sparse["ranked_scores"],
        )
        observed = fused["ranked_chunk_ids"][:100]
        differences = [
            {"rank": i + 1, "expected": cid,
             "observed": observed[i] if i < len(observed) else None}
            for i, cid in enumerate(expected)
            if i >= len(observed) or observed[i] != cid
        ]
        matched = observed == expected
        result.update(
            status="LOCAL_HYBRID100_ORDER_MATCHED" if matched
                   else "LOCAL_HYBRID100_ORDER_DIFFERS",
            full_hybrid100_order_matches=matched,
            observed_depth=len(observed),
            observed_hybrid100_order=observed,
            different_position_count=len(differences),
            first_difference=differences[0] if differences else None,
            blocker=None,
        )
    except Exception as error:
        result.update(
            status="LOCAL_HYBRID100_PROBE_BLOCKED",
            blocker={
                "stage": stage,
                "type": type(error).__name__,
                "detail": str(error),
                "missing_name": error.name if isinstance(error, NameError) else None,
            },
        )
    finally:
        client = scope.get("qdrant_client")
        if client is not None:
            try:
                client.close()
            except Exception as error:
                result["qdrant_close_error"] = {
                    "type": type(error).__name__, "detail": str(error),
                }

    raw = json.dumps(
        result, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False
    ).encode("utf-8")
    digest = sha(raw)
    relative = reports / f"C126.R11_local_hybrid100_probe.{digest}.json"
    path = root / relative
    try:
        with path.open("xb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        pass
    require(path.read_bytes() == raw, "C126_REPORT_RELOAD_CONFLICT")
    result["output"] = {
        "path": relative.as_posix(),
        "file_bytes_sha256": digest,
        "reload_validation": "PASS",
    }
    print(json.dumps(
        {k: v for k, v in result.items() if k != "observed_hybrid100_order"},
        ensure_ascii=False, indent=2,
    ))
    return result


def make_local_providers(root, startup, chain, bound):
    metrics = {"qdrant_queries_attempted": 0, "new_local_pairs_scored": 0, "char_channel_depth": 0}

    def quiet_run(name, **overrides):
        function = globals().get(name)
        require(callable(function), f"C138_FUNCTION_REQUIRED:{name}")
        scope = dict(function.__globals__)
        scope.update(overrides)
        scope["print"] = lambda *args, **kwargs: None
        return type(function)(function.__code__, scope)()

    def live_hybrid(pipeline, question, candidate_id, reference):
        require(metrics["qdrant_queries_attempted"] == 0, "C138_DUPLICATE_HYBRID_CALL")
        client = pipeline.retriever.client
        expected_path = (root / startup["dense_storage_path"]).resolve()

        class BorrowedClient:
            def __getattr__(self, name):
                return getattr(client, name)

            def close(self):
                # The constructed pipeline owns this client.
                pass

        def borrow(*, path):
            require(Path(path).resolve() == expected_path, "C138_DENSE_STORAGE_CONFLICT")
            return BorrowedClient()

        observed = quiet_run("run_v3_c126", QdrantClient=borrow)
        metrics["qdrant_queries_attempted"] = observed["qdrant_queries_attempted"]
        require(
            observed["status"] == "LOCAL_HYBRID100_ORDER_MATCHED"
            and observed["observed_hybrid100_order"] == reference
            and observed["candidate_id"] == candidate_id
            and observed["question_sha256"] == sha(question.encode("utf-8"))
            and observed["dense_collection"] == startup["dense_collection"]
            and observed["qdrant_queries_attempted"] == 1
            and observed["new_api_calls"] == 0,
            f"C138_HYBRID100_CONFLICT:{observed.get('blocker')}",
        )
        metrics["hybrid100_probe_receipt"] = observed["output"]
        return {
            "candidate_id": candidate_id,
            "question_sha256": observed["question_sha256"],
            "ordered_chunk_ids": observed["observed_hybrid100_order"],
            "receipt_sha256": observed["output"]["file_bytes_sha256"],
        }

    def live_rank(question, candidate_id, hybrid100, pool50_order, pool50_scores):
        require(metrics["new_local_pairs_scored"] == 0, "C138_DUPLICATE_LOCAL100_CALL")
        scored = quiet_run("run_v3_c120")
        metrics["new_local_pairs_scored"] = scored["new_local_pairs_scored"]
        require(
            scored["status"] == "ONE_DEVELOPMENT_LOCAL100_INPUT_BUILT"
            and scored["candidate_id"] == candidate_id
            and scored["question_sha256"] == sha(question.encode("utf-8"))
            and scored["hybrid100_order"] == list(hybrid100)
            and scored["scored_pool50_order"] == list(pool50_order)
            and all(scored["scores_by_chunk_id"][cid] == score
                    for cid, score in pool50_scores.items())
            and scored["new_local_pairs_scored"] == 50
            and scored["new_api_calls"] == 0,
            f"C138_LOCAL100_CONFLICT:{scored.get('blocker')}",
        )
        metrics["local100_probe_receipt"] = scored["output"]

        notebook_path = "notebooks/phase2/22d_full_corpus_retrieval_expansion.ipynb"
        notebook_sha = "fff5bd072a4977820882045451b61d66f8621ef9a4918775e4534800f0ae1480"
        notebook = json.loads(bound(notebook_path, notebook_sha))
        names = {
            "normalized_words", "char_tokens", "build_index", "lexical_search",
            "lexical_fusion",
        }
        nodes = [
            node for node in ast.parse("".join(notebook["cells"][12]["source"])).body
            if isinstance(node, ast.FunctionDef) and node.name in names
        ]
        require(len(nodes) == len(names) and {node.name for node in nodes} == names,
                "C138_NB22D_DEFINITIONS_REQUIRED")
        corpus_path = (
            "data/phase2/chunks/nb11_benchmark_v1/baseline_phase1_char_safe_v1.jsonl"
        )
        chunks = {}
        for line in bound(corpus_path, scored["input_file_hashes"]["chunks"]).splitlines():
            if line.strip():
                row = json.loads(line)
                cid = row["chunk_id"]
                require(cid not in chunks, "C138_DUPLICATE_CHUNK")
                chunks[cid] = row
        require(len(chunks) == 3488, "C138_CORPUS_COUNT_CONFLICT")
        scope = dict(globals())
        scope.update(require=require, CONFIG={
            "char_max_df_fraction": 0.30,
            "bm25": {"k1": 1.2, "b": 0.3},
            "rrf_k": 10,
            "incumbent_rank_weight": 0.75,
        })
        exec(compile(ast.Module(body=nodes, type_ignores=[]), notebook_path, "exec"), scope)
        index = scope["build_index"](chunks, "char")
        char_order = scope["lexical_search"](index, question, "char")
        channel_ref = chain["source_rows"]["NB22D_A03"]
        channel_sha = chain["input_file_hashes"]["NB22D_A03"]
        channel_row = json.loads(bound(
            channel_ref["path"], channel_sha,
        ).splitlines()[channel_ref["line_number"] - 1])
        require(channel_row["candidate_id"] == candidate_id
                and char_order == channel_row["channels"]["char"],
                "C138_CHAR_CHANNEL_ORDER_CONFLICT")
        metrics["char_channel_depth"] = len(char_order)

        hybrid_rank = {cid: i for i, cid in enumerate(hybrid100, 1)}
        local_rank = {cid: i for i, cid in enumerate(scored["local100_order"], 1)}
        require(set(hybrid_rank) == set(local_rank), "C138_LOCAL100_POOL_CONFLICT")
        ranked = sorted(hybrid100, key=lambda cid: (
            -(0.75 / (10 + local_rank[cid]) + 0.25 / (10 + hybrid_rank[cid])), cid,
        ))
        pool = set(pool50_order)
        top = []
        newcomer_used = False
        for cid in ranked:
            if cid not in pool:
                if newcomer_used:
                    continue
                newcomer_used = True
            top.append(cid)
            if len(top) == 10:
                break
        chosen = set(top)
        quota_order = top + [cid for cid in ranked if cid not in chosen]
        require(quota_order == chain["quota100_order"], "C138_QUOTA100_ORDER_CONFLICT")
        fused = scope["lexical_fusion"](
            quota_order, {"char": char_order}, {"channels": ["char"]},
        )
        require(fused == chain["char_rrf_order"], "C138_CHAR_RRF_ORDER_CONFLICT")
        return fused[:10]

    return live_hybrid, live_rank, metrics


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

    c122_sha = prior["input_file_hashes"]["C122"]
    chain = report("C122.R11_development_rank_chain", c122_sha)
    require(
        chain["status"] == "QUOTA100_AND_CHAR_RRF_FULL_ORDERS_MATCHED"
        and (chain["candidate_id"], chain["question_sha256"]) == (candidate, question_sha)
        and chain["char_rrf_top10"] == top10,
        "C141_RANK_CHAIN_REFERENCE_CONFLICT",
    )
    live_hybrid, live_rank, metrics = make_local_providers(root, prior, chain, read)
    events = []
    receipts = {}

    def query_check(question, candidate_id):
        require((candidate_id, text_sha(question)) == (candidate, question_sha),
                "C140_PROVIDER_QUERY_CONFLICT")

    def hybrid_provider(*, question, candidate_id):
        query_check(question, candidate_id)
        supplied = live_hybrid(pipeline, question, candidate_id, hybrid_ids)
        events.append("hybrid100_computed")
        return supplied

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
        fresh_top = live_rank(
            question, candidate_id, hybrid100, pool50_order, pool50_scores,
        )
        require(fresh_top == top10, "C141_FINAL_TOP10_CONFLICT")
        by_id = {chunk["chunk_id"]: chunk for chunk in chunks}
        events.append("final_order_computed")
        return {
            "candidate_id": candidate,
            "question_sha256": question_sha,
            "selected_variant": "char_rrf",
            "runtime_identity": {
                "scope": "STANDALONE_DEVELOPMENT_LOCAL_RANK_CHAIN_STUB",
                "pipeline_source_sha256": pipeline_sha,
                "route_source_sha256": route_file["file_bytes_sha256"],
                "reference_run_sha256": C138,
                "startup_module_sha256": sha(Path(__file__).read_bytes()),
                "local100_probe_receipt_sha256":
                    metrics["local100_probe_receipt"]["file_bytes_sha256"],
            },
            "ordered_chunks": [by_id[cid] for cid in fresh_top],
        }

    def write_receipt(role, payload):
        require(role in {"input", "output"} and role not in receipts,
                "C140_RECEIPT_ROLE_CONFLICT")
        receipts[role] = save(f"C141.R11_startup_{role}_receipt", payload)
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
                    == metrics["hybrid100_probe_receipt"]["file_bytes_sha256"]
                and recorded["runtime_identity"]["local100_probe_receipt_sha256"]
                    == metrics["local100_probe_receipt"]["file_bytes_sha256"],
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
            "hybrid100_computed", "pool50_receipt_supplied",
            "final_order_computed", "input_receipt_written",
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
    require(
        (metrics["qdrant_queries_attempted"], metrics["new_local_pairs_scored"],
         metrics["char_channel_depth"]) == (1, 50, 800),
        "C141_COMPUTATION_COUNTS_CONFLICT",
    )
    result = {
        "cell": "C141",
        "roadmap_action": "R11",
        "roadmap_subtask": "R11.3",
        "status": "STANDALONE_LOCAL_RANK_CHAIN_PASSED",
        "candidate_id": candidate,
        "question_sha256": question_sha,
        "input_file_hashes": {"C138": C138, "C139": C139, "C140": "8c26991d74a581ba7e80c2e4059ea5654fa4bdfb962b1aa0d10375502731e944", "C122": c122_sha},
        "startup_module_sha256": sha(Path(__file__).read_bytes()),
        "events": events,
        "receipts": receipts,
        "product_constructor_executed": True,
        "product_runtime_binding_verified": False,
        "product_regression_tests_executed": 0,
        **metrics,
        "rank_providers_executed_in_standalone_product_call": True,
        "new_api_calls": 0,
        "done_item_count": 7,
        "open_item_count": 5,
        "newly_completed_items_from_previous_open_set": [],
        "selected_version_gate": "BLOCKED",
        "next_product_dependency": "VERIFY_SELECTED_RUNTIME_REGRESSION_INPUTS",
    }
    result["output"] = save("C141.R11_standalone_local_rank_chain", result)
    return result


if __name__ == "__main__":
    print(json.dumps(run_offline(Path.cwd()), ensure_ascii=False, indent=2))
