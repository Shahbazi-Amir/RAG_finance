from pathlib import Path
import hashlib
import json

POLICY_ID = "rag_finance_answer_action_policy_v2"

def build_request(previous_request, *, policy_path):
    """Build a new request; never send it or mutate the original."""
    policy = json.loads(Path(policy_path).read_bytes())
    if policy["policy_id"] != POLICY_ID:
        raise ValueError("POLICY_ID_MISMATCH")
    prompt = policy["system_prompt"]
    actual = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    if actual != policy["system_prompt_sha256"]:
        raise ValueError("POLICY_PROMPT_HASH_MISMATCH")
    result = json.loads(json.dumps(previous_request, ensure_ascii=False))
    system = [
        index for index, message in enumerate(result["messages"])
        if message.get("role") == "system"
    ]
    if len(system) != 1:
        raise ValueError("EXACTLY_ONE_SYSTEM_MESSAGE_REQUIRED")
    message = result["messages"][system[0]]
    old_hash = hashlib.sha256(message["content"].encode("utf-8")).hexdigest()
    if old_hash != policy["previous_prompt_sha256"]:
        raise ValueError("UNEXPECTED_PREVIOUS_SYSTEM_PROMPT")
    message["content"] = prompt
    return result
