# Extracted tested route: no import-time execution.
from pathlib import Path
import ast
import hashlib
import importlib
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dotenv import dotenv_values

def require(ok, code):
    if not ok:
        raise ValueError(code)

def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def text_sha(value):
    return sha(value.encode("utf-8"))

def run_v3_c199():
    def require(ok, code):
        if not ok:
            raise ValueError(code)

    def encode(value):
        return json.dumps(
            value, ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")

    def sha(raw):
        return hashlib.sha256(raw).hexdigest()

    def text_sha(text):
        return sha(text.encode("utf-8"))

    reports = Path("reports/phase2/quality_improvement/NB22E.lab.v3")
    cwd = Path.cwd()
    root = next(
        (p.resolve() for p in (cwd, *cwd.parents) if (p / reports).is_dir()),
        None,
    )
    require(root is not None, "C199_PROJECT_ROOT_NOT_FOUND")

    def project_path(relative):
        path = (root / relative).resolve()
        require(path.is_relative_to(root), "C199_PATH_OUTSIDE_PROJECT")
        return path

    def load(relative, digest):
        raw = project_path(relative).read_bytes()
        require(sha(raw) == digest, f"C199_HASH_MISMATCH:{relative}")
        return json.loads(raw)

    def load_ref(pin):
        return load(pin["path"], pin["file_bytes_sha256"])

    def report(stem, digest):
        return load(reports / f"{stem}.{digest}.json", digest)

    def atomic_create(path, raw):
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(
            prefix=".C199-", dir=str(path.parent),
        )
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                os.link(temporary, path)
            except FileExistsError:
                pass
            require(path.read_bytes() == raw, "C199_EXISTING_OUTPUT_DIFFERS")
        finally:
            Path(temporary).unlink(missing_ok=True)

    def save(stem, value):
        raw = encode(value)
        digest = sha(raw)
        relative = reports / f"{stem}.{digest}.json"
        atomic_create(project_path(relative), raw)
        return {
            "path": relative.as_posix(),
            "file_bytes_sha256": digest,
            "reload_validation": "PASS",
        }

    c198_sha = "e9c605ecf404f084c0953b00f01e5d8dcb7752885aa720ffa83bf19c7789e6a3"
    c193_sha = "2f0c1535a4b0f5bd264d3ceddddc8a0ae235902c1deba5978fbe7479e8b4eeff"
    plan_sha = "a1a590e38c04ac9f0a7431bd5aac9c972f77c97f86b0e3d318c81d17d9e87876"
    ledger = report("C198.R11_selected_citation_witness_disposition", c198_sha)
    diagnosis = report("C193.R11_batch_response_diagnosis", c193_sha)
    plan = report("C191.R11_deepseek_batch_plan", plan_sha)

    target_ids = {
        "golden_v2_candidate_b8756d70dae44e64533a6691",
        "golden_v2_candidate_e5ea19069f2d84ca861c2847",
    }
    diagnosed = {
        row["candidate_id"]: row
        for row in diagnosis["blocked_response_diagnoses"]
    }
    require(
        set(diagnosed) == target_ids
        and ledger["open_item_ids"] == [9, 10, 12],
        "C199_TARGET_OR_LEDGER_MISMATCH",
    )

    jobs = []
    new_estimate_units = 0
    for summary in plan["jobs"]:
        candidate = summary["candidate_id"]
        if candidate not in target_ids:
            continue
        old_job = load_ref(summary["job_receipt"])
        old_response = load_ref(diagnosed[candidate]["response_receipt"])
        old_envelope = json.loads(old_response["response_body"])
        old_choice = old_envelope["choices"][0]
        old_request = old_job["request"]
        require(
            old_response["http_status"] == 200
            and old_response["request_payload_sha256"]
            == sha(encode(old_request)) == summary["request_payload_sha256"]
            and text_sha(old_response["response_body"])
            == old_response["response_body_sha256"]
            and old_choice["finish_reason"] == "length"
            and old_choice["message"]["content"] is None
            and old_request["max_tokens"] == 600,
            "C199_ORIGINAL_INCOMPLETE_RESPONSE_MISMATCH",
        )

        prepared = load_ref(old_job["prepared_context_receipt"])
        rank = load_ref(old_job["rank_receipt"])
        request = {**old_request, "max_tokens": 2400}
        body = encode(request)
        require(
            prepared["candidate_id"] == rank["candidate_id"] == candidate
            and {k: v for k, v in request.items() if k != "max_tokens"}
            == {k: v for k, v in old_request.items() if k != "max_tokens"}
            and request["model"] == "DeepSeek-V4-Flash",
            "C199_PROFILE_CHANGE_MISMATCH",
        )
        cost_units = (
            (len(body) + 1024) * plan["input_toman_per_million"]
            + 2400 * plan["output_toman_per_million"]
        )
        new_estimate_units += cost_units
        job = {
            **old_job,
            "request": request,
            "request_payload_sha256": sha(body),
            "request_bytes": len(body),
            "original_job_receipt": summary["job_receipt"],
            "original_response_receipt": diagnosed[candidate]["response_receipt"],
            "original_request_payload_sha256": summary["request_payload_sha256"],
            "profile_change": {"max_tokens": {"before": 600, "after": 2400}},
            "historical_estimated_cost_toman": cost_units / 1_000_000,
            "dispatch_performed": False,
        }
        pin = save("C199.R11_output_cap_probe_job", job)
        jobs.append((job, pin, prepared, rank))

    require(len(jobs) == 2, "C199_EXPECTED_TWO_JOBS")
    combined_estimate = (
        plan["historical_total_estimate_toman"] + new_estimate_units / 1_000_000
    )
    require(combined_estimate < 100_000, "C199_COMBINED_ESTIMATE_REACHES_BUDGET")

    batch_plan = {
        "C191": plan_sha,
        "C198": c198_sha,
        "jobs": [pin for _, pin, _, _ in jobs],
        "historical_new_estimate_toman": new_estimate_units / 1_000_000,
        "historical_combined_estimate_toman": combined_estimate,
        "current_rate_verified": False,
        "budget_toman": 100_000,
    }
    probe_plan_pin = save("C199.R11_output_cap_probe_plan", batch_plan)
    folder = (
        root / reports / "C199.R11_output_cap_receipts"
        / probe_plan_pin["file_bytes_sha256"]
    )
    folder.mkdir(parents=True, exist_ok=True)

    c186_sha = plan["input_file_hashes"]["C186"]
    inputs = report("C186.R11_remaining_scenario_input_preflight", c186_sha)
    corpus_relative = (
        "data/phase2/chunks/nb11_benchmark_v1/baseline_phase1_char_safe_v1.jsonl"
    )
    corpus_raw = project_path(corpus_relative).read_bytes()
    require(
        sha(corpus_raw) == inputs["input_file_hashes"]["chunks"],
        "C199_CORPUS_HASH_MISMATCH",
    )
    corpus = {}
    for line in corpus_raw.splitlines():
        if line.strip():
            row = json.loads(line)
            require(row["chunk_id"] not in corpus, "C199_DUPLICATE_CHUNK")
            corpus[row["chunk_id"]] = row

    pipeline_relative = "src/pipeline/rag_pipeline.py"
    pipeline_sha = "99ee048d00a7ad1884540fa297eb41df86ad4e54f6c49f26385ebb6b2ed504f6"
    pipeline_raw = project_path(pipeline_relative).read_bytes()
    require(sha(pipeline_raw) == pipeline_sha, "C199_PIPELINE_HASH_MISMATCH")
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    module = importlib.import_module("src.pipeline.rag_pipeline")
    require(
        Path(module.__file__).resolve() == project_path(pipeline_relative),
        "C199_PRODUCT_MODULE_PATH_MISMATCH",
    )
    pipeline_class = module.RAGPipeline

    code_type = type(run_v3_c199.__code__)
    compiled = compile(pipeline_raw, pipeline_relative, "exec", dont_inherit=True)
    class_code = next(
        value for value in compiled.co_consts
        if isinstance(value, code_type) and value.co_name == "RAGPipeline"
    )
    method_codes = {
        value.co_name: value for value in class_code.co_consts
        if isinstance(value, code_type)
    }

    def signature(code):
        return (
            code.co_code,
            tuple(
                signature(value) if isinstance(value, code_type) else value
                for value in code.co_consts
            ),
            code.co_names, code.co_varnames, code.co_freevars, code.co_cellvars,
            code.co_flags, code.co_argcount, code.co_posonlyargcount,
            code.co_kwonlyargcount, code.co_exceptiontable,
        )

    for name in ("__init__", "ask_with_char_rrf", "build_context", "close"):
        require(
            signature(getattr(pipeline_class, name).__code__)
            == signature(method_codes[name]),
            f"C199_LOADED_METHOD_MISMATCH:{name}",
        )

    parser = globals().get("dotenv_values")
    url_module = globals().get("urllib")
    require(
        callable(parser) and url_module is not None,
        "C199_C001_TRANSPORT_BINDINGS_REQUIRED",
    )
    config = parser(root / ".env", interpolate=False)
    base = str(os.environ.get("ARVAN_GATEWAY_URL") or config.get("ARVAN_GATEWAY_URL") or "").strip()
    key = str(os.environ.get("ARVAN_GATEWAY_API_KEY") or config.get("ARVAN_GATEWAY_API_KEY") or "").strip()
    url = url_module.parse.urlsplit(base)
    require(
        url.scheme == "https" and bool(url.hostname) and bool(key)
        and url.username is None and url.password is None
        and not url.query and not url.fragment,
        "C199_GATEWAY_CONFIGURATION_INVALID",
    )
    route = url.path.rstrip("/") or "/v1"
    if not route.endswith("/chat/completions"):
        route += "/chat/completions"
    endpoint = url._replace(path=route).geturl()

    class NoRedirect(url_module.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = url_module.request.build_opener(NoRedirect())
    c148_sha = "8352cfa49bedc99c50335f57a66051a3613bdb1cf3618200dff771a8c1d654f4"
    dense = report("C148.R11_target_test_hybrid100_probe", c148_sha)

    results = []
    blockers = []
    new_calls = 0
    pipeline = pipeline_class(
        vectorstore_path=project_path(dense["dense_storage_path"]),
        collection_name=dense["dense_collection"],
        use_cache=False,
    )

    try:
        for job, job_pin, prepared, rank in jobs:
            candidate = job["candidate_id"]
            request_sha = job["request_payload_sha256"]
            completed_path = folder / f"{request_sha}.completed.json"
            started_path = folder / f"{request_sha}.started.json"
            response_path = folder / f"{request_sha}.response.json"
            input_ref = None
            output_ref = None
            answer_state = {}

            try:
                if completed_path.exists():
                    saved = json.loads(completed_path.read_bytes())
                    require(
                        saved["job_receipt"] == job_pin
                        and saved["candidate_id"] == candidate,
                        "C199_COMPLETED_JOB_MISMATCH",
                    )
                    recorded_input = load_ref(saved["input_receipt"])
                    recorded_output = load_ref(saved["output_receipt"])
                    recorded_response = load_ref(saved["response_receipt"])
                    require(
                        recorded_input["runtime_identity"]["invocation_id"]
                        == saved["invocation_id"]
                        and recorded_output["input_receipt_file_bytes_sha256"]
                        == saved["input_receipt"]["file_bytes_sha256"]
                        and recorded_output["answer_text_utf8_sha256"]
                        == text_sha(saved["answer"])
                        and recorded_response["request_payload_sha256"] == request_sha
                        and text_sha(recorded_response["response_body"])
                        == recorded_response["response_body_sha256"]
                        and json.loads(recorded_response["response_body"])[
                            "choices"
                        ][0]["message"]["content"] == saved["answer"],
                        "C199_COMPLETED_RECEIPT_MISMATCH",
                    )
                    results.append(saved)
                    continue

                require(
                    not started_path.exists() and not response_path.exists(),
                    "C199_PREVIOUS_ATTEMPT_REQUIRES_RECOVERY_NO_RESEND",
                )
                invocation = sha(
                    f"C199:{candidate}:{time.time_ns()}:{os.getpid()}".encode("utf-8")
                )
                chunks = [
                    {
                        "chunk_id": cid,
                        "text": corpus[cid]["content"],
                        "title": corpus[cid].get("title"),
                        "url": corpus[cid].get("url"),
                    }
                    for cid in rank["char_rrf_top10"]
                ]
                require(
                    [text_sha(chunk["text"]) for chunk in chunks]
                    == rank["char_rrf_top10_text_sha256"],
                    "C199_CHUNK_TEXT_MISMATCH",
                )
                runtime_identity = {
                    "scope": "OUTPUT_CAP_2400_PROFILE_PROBE",
                    "invocation_id": invocation,
                    "pipeline_source_sha256": pipeline_sha,
                    "rank_receipt_sha256": job["rank_receipt"]["file_bytes_sha256"],
                    "job_receipt_sha256": job_pin["file_bytes_sha256"],
                }

                def rank_sources(*, question, candidate_id, top_k):
                    require(
                        candidate_id == candidate and top_k == 10
                        and text_sha(question) == job["question_sha256"],
                        "C199_RUNTIME_QUERY_MISMATCH",
                    )
                    return {
                        "candidate_id": candidate,
                        "question_sha256": job["question_sha256"],
                        "selected_variant": "char_rrf",
                        "runtime_identity": runtime_identity,
                        "ordered_chunks": chunks,
                    }

                def write_receipt(role, payload):
                    nonlocal input_ref, output_ref
                    if role == "input":
                        require(input_ref is None, "C199_DUPLICATE_INPUT")
                        input_ref = save("C199.R11_product_input", payload)
                        return input_ref["file_bytes_sha256"]
                    require(
                        role == "output" and input_ref is not None and output_ref is None
                        and payload["input_receipt_file_bytes_sha256"]
                        == input_ref["file_bytes_sha256"]
                        and payload["answer_text_utf8_sha256"] == answer_state["answer_sha"],
                        "C199_OUTPUT_BINDING_MISMATCH",
                    )
                    output_ref = save("C199.R11_product_output", payload)
                    return output_ref["file_bytes_sha256"]

                class Generator:
                    def generate_answer(self, *, question, context):
                        nonlocal new_calls
                        require(input_ref is not None, "C199_INPUT_RECEIPT_REQUIRED")
                        recorded = load_ref(input_ref)
                        require(
                            question == prepared["question"]
                            and context == prepared["rendered_context"]
                            and recorded["candidate_id"] == candidate
                            and recorded["runtime_identity"] == runtime_identity
                            and recorded["question_sha256"] == job["question_sha256"]
                            and recorded["ordered_chunk_ids"] == rank["char_rrf_top10"]
                            and recorded["ordered_chunk_text_sha256"]
                            == rank["char_rrf_top10_text_sha256"]
                            and recorded["rendered_context_sha256"]
                            == text_sha(context) == job["rendered_context_sha256"],
                            "C199_PRE_GENERATION_BINDING_MISMATCH",
                        )
                        started = {
                            "candidate_id": candidate,
                            "invocation_id": invocation,
                            "request_payload_sha256": request_sha,
                            "job_receipt": job_pin,
                            "input_receipt": input_ref,
                        }
                        with started_path.open("xb") as stream:
                            stream.write(encode(started))
                            stream.flush()
                            os.fsync(stream.fileno())

                        outgoing = url_module.request.Request(
                            endpoint,
                            data=encode(job["request"]),
                            method="POST",
                            headers={
                                "Authorization": f"apikey {key}",
                                "Content-Type": "application/json",
                            },
                        )
                        new_calls += 1
                        try:
                            with opener.open(outgoing, timeout=180) as response:
                                status = response.status
                                body = response.read().decode("utf-8")
                        except url_module.error.HTTPError as error:
                            with error:
                                status = error.code
                                body = error.read().decode("utf-8")
                        except (OSError, ValueError):
                            raise ValueError("C199_UNKNOWN_DISPATCH_OUTCOME_NO_RESEND") from None

                        response_record = {
                            "candidate_id": candidate,
                            "invocation_id": invocation,
                            "request_payload_sha256": request_sha,
                            "input_receipt_file_bytes_sha256": input_ref["file_bytes_sha256"],
                            "started_receipt_sha256": sha(started_path.read_bytes()),
                            "http_status": status,
                            "response_body": body,
                            "response_body_sha256": text_sha(body),
                        }
                        atomic_create(response_path, encode(response_record))
                        require(status == 200, "C199_NON200_RESPONSE_PRESERVED")
                        envelope = json.loads(body)
                        choices = envelope.get("choices", [])
                        require(len(choices) == 1, "C199_EXPECTED_ONE_CHOICE")
                        choice = choices[0]
                        answer = choice.get("message", {}).get("content")
                        require(
                            envelope["model"].strip().rsplit("/", 1)[-1].lower()
                            in {"deepseek-v4-flash", "deepseek-v4-flash-0731"}
                            and choice.get("finish_reason") == "stop"
                            and isinstance(answer, str) and bool(answer.strip()),
                            "C199_RESPONSE_INCOMPLETE_OR_WRONG_MODEL",
                        )
                        answer_state.update(
                            answer_sha=text_sha(answer),
                            finish_reason=choice["finish_reason"],
                            usage_as_reported=envelope.get("usage"),
                            response_receipt={
                                "path": response_path.relative_to(root).as_posix(),
                                "file_bytes_sha256": sha(response_path.read_bytes()),
                            },
                        )
                        return answer

                pipeline.generator = Generator()
                returned = pipeline.ask_with_char_rrf(
                    prepared["question"],
                    candidate_id=candidate,
                    rank_sources=rank_sources,
                    write_receipt=write_receipt,
                    top_k=10,
                )
                require(
                    returned["from_cache"] is False
                    and output_ref is not None
                    and returned["input_receipt_file_bytes_sha256"]
                    == input_ref["file_bytes_sha256"]
                    and returned["output_receipt_file_bytes_sha256"]
                    == output_ref["file_bytes_sha256"],
                    "C199_PRODUCT_RETURN_MISMATCH",
                )
                saved = {
                    "candidate_id": candidate,
                    "scenario_ids": [
                        spec["regression_spec_id"] for spec in job["scenario_specs"]
                    ],
                    "invocation_id": invocation,
                    "job_receipt": job_pin,
                    "request_payload_sha256": request_sha,
                    "input_receipt": input_ref,
                    "output_receipt": output_ref,
                    "answer": returned["answer"],
                    **answer_state,
                    "semantic_verdict": None,
                }
                atomic_create(completed_path, encode(saved))
                results.append(saved)

            except Exception as error:
                blockers.append({
                    "candidate_id": candidate,
                    "type": type(error).__name__,
                    "detail": str(error),
                    "input_receipt": input_ref,
                    "response_path": (
                        response_path.relative_to(root).as_posix()
                        if response_path.exists() else None
                    ),
                })
    finally:
        pipeline.close()

    result = {
        "cell": "C199",
        "roadmap_subtask": "R11.3",
        "checklist_item": 12,
        "status": (
            "TWO_PROFILE_PROBE_RESPONSES_BOUND"
            if len(results) == 2 and not blockers else "OUTPUT_CAP_PROBE_PARTIAL"
        ),
        "input_file_hashes": {"C198": c198_sha, "C193": c193_sha, "C191": plan_sha},
        "probe_plan": probe_plan_pin,
        "profile_change": {"max_tokens": {"before": 600, "after": 2400}},
        "completed_candidate_count": len(results),
        "candidate_results": results,
        "blocked_candidates": blockers,
        "new_api_calls": new_calls,
        "current_rate_verified": False,
        "historical_new_estimate_toman": new_estimate_units / 1_000_000,
        "historical_combined_estimate_toman": combined_estimate,
        "original_600_token_results_preserved": True,
        "new_semantic_verdicts": 0,
        "done_item_count": 9,
        "open_item_count": 3,
        "open_item_ids": [9, 10, 12],
        "selected_version_gate": "BLOCKED",
    }
    result["output"] = save("C199.R11_output_cap_probe_result", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def run_fixed_input(pipeline, *, root, bundle, receipt_directory, generator):
    root = Path(root).resolve()
    receipt_directory = Path(receipt_directory).resolve()
    require(receipt_directory.is_relative_to(root), "OFFLINE_PATH_OUTSIDE_PROJECT")
    receipt_directory.mkdir(parents=True, exist_ok=True)
    job = bundle["job"]
    prepared = bundle["prepared"]
    rank = bundle["rank"]
    chunks = bundle["chunks"]
    candidate = job["candidate_id"]
    runtime_identity = dict(bundle["historical_input"]["runtime_identity"])
    runtime_identity["invocation_id"] = "C212_OFFLINE_" + sha(encode(job))
    runtime_identity["control_mode"] = "OFFLINE_STUB_NO_DISPATCH"
    input_ref = None
    output_ref = None
    answer_state = {}
    events = []

    def load_ref(pin):
        path = (root / pin["path"]).resolve()
        require(path.is_relative_to(root), "OFFLINE_READ_OUTSIDE_PROJECT")
        raw = path.read_bytes()
        require(sha(raw) == pin["file_bytes_sha256"], "OFFLINE_RECEIPT_HASH")
        return json.loads(raw)

    def save(stem, payload):
        raw = encode(payload)
        digest = sha(raw)
        path = receipt_directory / (stem + "." + digest + ".json")
        if path.exists():
            require(path.read_bytes() == raw, "OFFLINE_RECEIPT_CONFLICT")
        else:
            with path.open("xb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
        require(path.read_bytes() == raw, "OFFLINE_RECEIPT_RELOAD")
        events.append("input_persisted" if input_ref is None else "output_persisted")
        return {"path": path.relative_to(root).as_posix(),
                "file_bytes_sha256": digest}

    def rank_sources(*, question, candidate_id, top_k):
        require(candidate_id == candidate and top_k == 10 and (text_sha(question) == job['question_sha256']), 'C199_RUNTIME_QUERY_MISMATCH')
        return {'candidate_id': candidate, 'question_sha256': job['question_sha256'], 'selected_variant': 'char_rrf', 'runtime_identity': runtime_identity, 'ordered_chunks': chunks}

    def write_receipt(role, payload):
        nonlocal input_ref, output_ref
        if role == 'input':
            require(input_ref is None, 'C199_DUPLICATE_INPUT')
            input_ref = save('C199.R11_product_input', payload)
            return input_ref['file_bytes_sha256']
        require(role == 'output' and input_ref is not None and (output_ref is None) and (payload['input_receipt_file_bytes_sha256'] == input_ref['file_bytes_sha256']) and (payload['answer_text_utf8_sha256'] == answer_state['answer_sha']), 'C199_OUTPUT_BINDING_MISMATCH')
        output_ref = save('C199.R11_product_output', payload)
        return output_ref['file_bytes_sha256']

    class Generator:
        def generate_answer(self, *, question, context):
            require(input_ref is not None, 'C199_INPUT_RECEIPT_REQUIRED')
            recorded = load_ref(input_ref)
            require(question == prepared['question'] and context == prepared['rendered_context'] and (recorded['candidate_id'] == candidate) and (recorded['runtime_identity'] == runtime_identity) and (recorded['question_sha256'] == job['question_sha256']) and (recorded['ordered_chunk_ids'] == rank['char_rrf_top10']) and (recorded['ordered_chunk_text_sha256'] == rank['char_rrf_top10_text_sha256']) and (recorded['rendered_context_sha256'] == text_sha(context) == job['rendered_context_sha256']), 'C199_PRE_GENERATION_BINDING_MISMATCH')
            events.append("persisted_input_verified")
            answer = generator.generate_answer(question=question, context=context)
            require(isinstance(answer, str), "OFFLINE_STUB_TEXT_REQUIRED")
            answer_state["answer_sha"] = text_sha(answer)
            events.append("stub_returned")
            return answer

    pipeline.generator = Generator()
    returned = pipeline.ask_with_char_rrf(
        prepared["question"], candidate_id=candidate,
        rank_sources=rank_sources, write_receipt=write_receipt, top_k=10,
    )
    require(input_ref is not None and output_ref is not None,
            "OFFLINE_RECEIPT_CHAIN_INCOMPLETE")
    require(returned["input_receipt_file_bytes_sha256"]
            == input_ref["file_bytes_sha256"]
            and returned["output_receipt_file_bytes_sha256"]
            == output_ref["file_bytes_sha256"], "OFFLINE_RETURN_BINDING")
    return {"input_receipt": input_ref, "output_receipt": output_ref,
            "events": events, "returned": returned}


def offline_control(root, fixture_path, fixture_sha, output_directory):
    root = Path(root).resolve()
    fixture_path = Path(fixture_path).resolve()
    require(fixture_path.is_relative_to(root), "FIXTURE_OUTSIDE_PROJECT")
    raw = fixture_path.read_bytes()
    require(sha(raw) == fixture_sha, "FIXTURE_HASH_MISMATCH")
    bundle = json.loads(raw)
    def audit(event, args):
        if event in {"socket.connect", "socket.connect_ex",
                     "socket.getaddrinfo", "socket.bind"}:
            raise RuntimeError("C212_NETWORK_FORBIDDEN")
    sys.addaudithook(audit)

    product_path = root / "src/pipeline/rag_pipeline.py"
    require(sha(product_path.read_bytes()) == bundle["pipeline_source_sha256"],
            "PRODUCT_SOURCE_HASH_MISMATCH")
    sys.path.insert(0, str(root))
    product = importlib.import_module("src.pipeline.rag_pipeline")
    require(Path(product.__file__).resolve() == product_path.resolve(),
            "PRODUCT_IMPORT_PATH_MISMATCH")

    class Stub:
        def __init__(self):
            self.calls = 0
        def generate_answer(self, *, question, context):
            self.calls += 1
            require(question == bundle["prepared"]["question"],
                    "STUB_QUESTION_MISMATCH")
            require(context == bundle["prepared"]["rendered_context"],
                    "STUB_CONTEXT_MISMATCH")
            return "C212_OFFLINE_TRANSPORT_CONTROL"

    # Only the tested product boundary is exercised. No constructor,
    # retriever, embedder or generator client is initialized.
    pipeline = object.__new__(product.RAGPipeline)
    stub = Stub()
    positive = run_fixed_input(
        pipeline, root=root, bundle=bundle,
        receipt_directory=Path(output_directory) / "positive",
        generator=stub,
    )
    input_path = root / positive["input_receipt"]["path"]
    recorded = json.loads(input_path.read_bytes())
    expected = bundle["historical_input"]
    for key in ("candidate_id", "question_sha256", "selected_variant",
                "ordered_chunk_ids", "ordered_chunk_text_sha256",
                "rendered_context_sha256"):
        require(recorded[key] == expected[key], "HISTORICAL_INPUT_DIFF:" + key)
    require(positive["events"] == [
        "input_persisted", "persisted_input_verified",
        "stub_returned", "output_persisted",
    ], "OFFLINE_EVENT_ORDER_MISMATCH")
    require(stub.calls == 1, "OFFLINE_STUB_CALL_COUNT")

    bad = json.loads(json.dumps(bundle))
    bad["chunks"] = list(reversed(bad["chunks"]))
    negative_stub = Stub()
    rejected = None
    try:
        run_fixed_input(
            object.__new__(product.RAGPipeline),
            root=root, bundle=bad,
            receipt_directory=Path(output_directory) / "negative",
            generator=negative_stub,
        )
    except ValueError as error:
        rejected = str(error)
    require(rejected == "C199_PRE_GENERATION_BINDING_MISMATCH"
            and negative_stub.calls == 0, "NEGATIVE_ORDER_CONTROL_FAILED")

    return {
        "status": "FRESH_PROCESS_FIXED_INPUT_BOUNDARY_PASSED",
        "same_order_and_text_hashes": True,
        "exact_context_text_match": True,
        "rendered_context_sha256": recorded["rendered_context_sha256"],
        "events": positive["events"],
        "input_receipt": positive["input_receipt"],
        "output_receipt": positive["output_receipt"],
        "negative_order_control": "REJECTED_BEFORE_STUB",
        "product_constructor_executed": False,
        "live_dispatch_performed": False,
        "new_api_calls": 0,
        "new_model_runs": 0,
        "kernel_history_required": False,
    }

if __name__ == "__main__":
    require(len(sys.argv) == 5, "EXPECTED_ROOT_FIXTURE_HASH_OUTPUT")
    print(json.dumps(offline_control(*sys.argv[1:]),
                     ensure_ascii=False, sort_keys=True))
