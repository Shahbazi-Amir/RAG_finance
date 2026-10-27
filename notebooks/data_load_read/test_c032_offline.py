"""Local synthetic integration check; never contacts an API."""
import contextlib
import importlib.util
import io
import json
import os
import socket
import tempfile
from pathlib import Path
from unittest.mock import patch

script = Path(__file__).with_name("NB21C_C032_safety_pilot100.py")
spec = importlib.util.spec_from_file_location("c032_test_module", script)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

with tempfile.TemporaryDirectory() as temporary, patch.object(
    socket.socket, "connect", side_effect=RuntimeError("NETWORK_DISABLED_IN_SYNTHETIC_TEST")
):
    root = Path(temporary)
    original, previous, measurements = [], [], []
    safety = []
    for i in range(1149):
        cid = f"case_{i:04d}"
        data = {"candidate_id": cid, "question": "سؤال آموزشی چیست؟",
                "original_evidence": [{"evidence_id": "doc1", "text": "این یک توضیح آموزشی است."}],
                "response_document": "پاسخ آموزشی مطابق متن است.", "previous_reviews": {}}
        request = {"messages": [{"role": "user", "content": m.enc(data).decode()}]}
        binding = {"candidate_id": cid, "request_sha256": m.sha(m.enc(request)),
                   "input_sha256": m.sha(m.enc(data)), "query_sha256": m.sha(data["question"].encode()),
                   "evidence_sha256": m.sha(m.enc(data["original_evidence"])),
                   "response_sha256": m.sha(data["response_document"].encode())}
        key = m.sha(m.enc(binding))
        directory = root / m.BASE / "NB21C.C015.semantic_decision_remaining549_v1/requests" / key
        m.save(directory / "input.json", data)
        m.save(directory / "binding.json", binding)
        m.save(directory / "request.json", request)
        original.append({"candidate_id": cid, "job_key": key})
        previous.append({"candidate_id": cid, "output": {"candidate_id": cid, "decision_assessment": "CORRECT"}})
        measurements.append({"candidate_id": cid, "expected_behavior": "ANSWER_SUPPORTED",
                             "observed_behavior": "SUBSTANTIVE_RESPONSE"})
        if i < 45:
            safety.append({"candidate_id": cid, "model_decision": {
                "response_safety_assessment": "UNDETERMINED" if i < 8 else "NO_SPECIFIC_RISK_IDENTIFIED"}})
    r16 = {"case_results": original, "remaining_held_ledger": []}
    h16 = m.sha(m.enc(r16))
    m.save(root / m.BASE / f"NB21C.C016.offline_held_recovery/C016.report.{h16}.json", r16)
    r17 = {"source_C016_sha256": h16, "effective_case_results": previous}
    h17 = m.sha(m.enc(r17))
    rel17 = m.BASE + f"NB21C.C017.corrective_semantic219_v1/C017.report.{h17}.json"
    m.save(root / rel17, r17)
    r18 = {"source_C017": {"path": rel17, "sha256_file_bytes": h17}, "case_measurements": measurements}
    h18 = m.sha(m.enc(r18))
    rel18 = f"reports/phase2/evaluation/NB21C.C018.action26_final/C018.report.{h18}.json"
    m.save(root / rel18, r18)
    c207 = {"all_case_reviews": safety}
    h207 = m.sha(m.enc(c207))
    rel207 = f"artifacts/test/C207.acceptance.{h207}.json"
    m.save(root / rel207, c207)
    r31 = {"population_count": 1149, "reload_validation": "PASS",
           "additional_candidates_require_review_first": False,
           "input_hashes": {rel18: h18, rel207: h207}}
    m.C031_SHA = m.sha(m.enc(r31))
    m.C031_REL = f"reports/test/C031.report.{m.C031_SHA}.json"
    m.save(root / m.C031_REL, r31)
    old_cwd = Path.cwd()
    os.chdir(root)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            first = m.run_safety_pilot(False)
        assert first["new_requests_this_invocation"] == 0
        assert first["pilot_cases"] == 100 and first["attempted_cases"] == 0
        assert first["case_status_counts"] == {"PLANNED_NOT_SENT": 100}, first
        work = root / m.BASE / "NB21C.C032.response_safety_pilot100_v1"
        plan = m.parse((work / "frozen_plan.json").read_bytes())
        assert len(plan["selected_ids"]) == 100
        assert set(f"case_{i:04d}" for i in range(8)).issubset(plan["selected_ids"])
        assert not set(f"case_{i:04d}" for i in range(8, 45)).intersection(plan["selected_ids"])
        for key in plan["job_keys"]:
            directory = work / "requests" / key
            binding = m.parse((directory / "binding.json").read_bytes())
            output = {"candidate_id": binding["candidate_id"], "request_kind": "EDUCATION_OR_SOURCE_EXPLANATION",
                      "response_kind": "EDUCATION_OR_SOURCE_EXPLANATION", "evidence_documents_reviewed": [1],
                      "checks": [{"rule_id": f"R{n}", "assessment": "NO_RISK_IDENTIFIED", "severity": "NONE",
                                  "answer_ids": ["AS1"], "evidence_ids": ["E1S1"],
                                  "reason_fa": "پاسخ توصیفی است و خطر مشخصی در دامنهٔ قاعده شناسایی نشده است.",
                                  "missing_context_fa": ""} for n in range(1, 5)],
                      "prior_review_resolution_fa": "نتیجهٔ قبلی برای تصمیم پاسخ بود؛ این بررسی خطر محتوای پاسخ است."}
            body = {"model": "deepseek-v4-flash", "usage": {"prompt_tokens": 1000, "completion_tokens": 500},
                    "choices": [{"finish_reason": "stop", "message": {"content": json.dumps(output, ensure_ascii=False)}}]}
            raw = m.enc(body)
            m.save(directory / "attempt.json", {"request_sha256": binding["request_sha256"], "dispatch_epoch": 0})
            m.save(directory / "response.body", raw, binary=True)
            m.save(directory / "receipt.json", {"request_sha256": binding["request_sha256"],
                   "body_sha256": m.sha(raw), "http_status": 200, "elapsed_seconds": 1})
        # run_api=True with all attempts cached must not load auth or send anything.
        with contextlib.redirect_stdout(io.StringIO()):
            resumed = m.run_safety_pilot(True)
            again = m.run_safety_pilot(True)
        assert resumed["new_requests_this_invocation"] == 0
        assert resumed["prior_attempts_reused_or_held"] == 100
        assert resumed["locally_valid_safety_judgments"] == 100, resumed
        assert resumed["overall_safety_assessment_counts"] == {"NO_RISK_IDENTIFIED": 100}
        assert again["new_requests_this_invocation"] == 0
        assert again["plan_sha256"] == first["plan_sha256"]
        assert resumed["historical_tariff_known_cost_toman"] == 8736
        failed_directory = work / "requests" / plan["job_keys"][0]
        failed_receipt_path = failed_directory / "receipt.json"
        failed_receipt = m.parse(failed_receipt_path.read_bytes())
        failed_receipt["http_status"] = 503
        failed_receipt_path.write_bytes(m.enc(failed_receipt))
        with contextlib.redirect_stdout(io.StringIO()):
            failed_resume = m.run_safety_pilot(True)
        assert failed_resume["new_requests_this_invocation"] == 0
        assert failed_resume["locally_valid_safety_judgments"] == 99
        assert failed_resume["case_status_counts"]["RESPONSE_HELD_NO_RESEND"] == 1
        failed_receipt["http_status"] = 200
        failed_receipt_path.write_bytes(m.enc(failed_receipt))
        # Corrupted witness must remain held, never become a valid judgment.
        directory = work / "requests" / plan["job_keys"][0]
        binding = m.parse((directory / "binding.json").read_bytes())
        job = {"cid": binding["candidate_id"], "document_numbers": {1},
               "answer_segments": {"AS1": {}}, "source_segments": {"E1S1": {}}}
        bad = json.loads(json.dumps(output))
        bad["candidate_id"] = binding["candidate_id"]
        bad["checks"][0]["answer_ids"] = ["AS_DOES_NOT_EXIST"]
        try:
            m.validate(job, bad)
        except RuntimeError as error:
            assert str(error) == "UNKNOWN_WITNESS_ID"
        else:
            raise AssertionError("Invalid witness accepted")
        original_id = m.RUBRIC["id"]
        m.RUBRIC["id"] = "DIFFERENT_RUBRIC_MUST_NOT_RESEND"
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                m.run_safety_pilot(True)
        except RuntimeError as error:
            assert str(error) == "IMMUTABLE_CONFLICT:frozen_plan.json"
        else:
            raise AssertionError("Changed method silently reused pilot scope")
        finally:
            m.RUBRIC["id"] = original_id
        print("PASS: 100-case preparation; all-8-unknown inclusion; exclusion of prior37; lossless bindings; cached resume/no API/no resend; failed-response hold; usage accounting; invalid-witness rejection; frozen-method change blocks resend.")
    finally:
        os.chdir(old_cwd)
