from pathlib import Path
import hashlib
import json

POLICY_SHA256 = "e3a664516ce943d6254d655987962d16c1142cd72f58be5c2fae1a0a29d6948b"
PROMPT_SHA256 = "0de8355cadf0479d6aa94f01d8b5bb9990173596e57702a7abfcb86b0b0f77d8"
PARENT_PROMPT_SHA256 = "4a211041cf0d7e9c371a429ae24c890e9476de21a2e38c6440f2d788564b3ab8"

def build_request(previous_request, *, policy_path):
    raw = Path(policy_path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != POLICY_SHA256:
        raise ValueError("CANDIDATE_POLICY_HASH_MISMATCH")
    policy = json.loads(raw)
    if policy["policy_id"] != "rag_finance_answer_action_policy_v2_1_candidate":
        raise ValueError("CANDIDATE_POLICY_ID_MISMATCH")
    prompt = policy["system_prompt"]
    if hashlib.sha256(prompt.encode("utf-8")).hexdigest() != PROMPT_SHA256:
        raise ValueError("CANDIDATE_PROMPT_HASH_MISMATCH")
    request = json.loads(json.dumps(previous_request, ensure_ascii=False))
    indices = [
        i for i, message in enumerate(request["messages"])
        if message.get("role") == "system"
    ]
    if len(indices) != 1:
        raise ValueError("EXACTLY_ONE_SYSTEM_MESSAGE_REQUIRED")
    message = request["messages"][indices[0]]
    if hashlib.sha256(message["content"].encode("utf-8")).hexdigest() != PARENT_PROMPT_SHA256:
        raise ValueError("PARENT_V2_PROMPT_HASH_MISMATCH")
    message["content"] = prompt
    return request

class ExplicitPolicyGenerator:
    """Explicit adapter. Transport is supplied; no default network."""
    def __init__(self, *, previous_request, question, context, policy_path, send):
        if not callable(send):
            raise ValueError("EXPLICIT_SEND_CALLBACK_REQUIRED")
        self._request = build_request(previous_request, policy_path=policy_path)
        self._question = question
        self._context = context
        self._send = send

    def generate_answer(self, *, question, context):
        if question != self._question or context != self._context:
            raise ValueError("FIXED_QUESTION_OR_CONTEXT_MISMATCH")
        request = json.loads(json.dumps(self._request, ensure_ascii=False))
        answer = self._send(request)
        if not isinstance(answer, str):
            raise ValueError("SEND_CALLBACK_MUST_RETURN_TEXT")
        return answer
