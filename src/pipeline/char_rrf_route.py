"""Explicit product entry for the opt-in char_rrf route."""

import hashlib
import math


def ask_product_char_rrf(
    pipeline, *, question, candidate_id, hybrid100_provider,
    pool50_provider, rank_provider, write_receipt, top_k=10,
):
    def require(ok, code):
        if not ok:
            raise ValueError(code)

    require(isinstance(question, str) and bool(question.strip()),
            "C134_QUESTION_REQUIRED")
    require(isinstance(candidate_id, str) and bool(candidate_id.strip()),
            "C134_CANDIDATE_ID_REQUIRED")

    question_sha = hashlib.sha256(question.encode("utf-8")).hexdigest()

    def check_identity(payload, label):
        require(
            payload["candidate_id"] == candidate_id
            and payload["question_sha256"] == question_sha,
            f"C134_QUERY_IDENTITY_CONFLICT:{label}",
        )
        digest = payload["receipt_sha256"]
        require(
            isinstance(digest, str) and len(digest) == 64
            and all(char in "0123456789abcdef" for char in digest),
            f"C134_PROVIDER_RECEIPT_HASH_REQUIRED:{label}",
        )
        return digest

    def rank_sources(*, question, candidate_id, top_k):
        hybrid = hybrid100_provider(question=question, candidate_id=candidate_id)
        hybrid_sha = check_identity(hybrid, "HYBRID100")
        hybrid_ids = hybrid["ordered_chunk_ids"]
        require(len(hybrid_ids) == len(set(hybrid_ids)) == 100,
                "C134_INVALID_HYBRID100")

        pool = pool50_provider(
            question=question, candidate_id=candidate_id,
            hybrid100=tuple(hybrid_ids),
        )
        pool_sha = check_identity(pool, "POOL50")
        pool_ids = pool["ordered_chunk_ids"]
        scores = pool["scores_by_chunk_id"]
        require(
            len(pool_ids) == len(set(pool_ids)) == 50
            and set(pool_ids) == set(hybrid_ids[:50]) == set(scores)
            and all(type(score) in (int, float) and math.isfinite(score)
                    for score in scores.values()),
            "C134_POOL50_MEMBERSHIP_OR_SCORES_CONFLICT",
        )

        ranked = rank_provider(
            question=question, candidate_id=candidate_id, top_k=top_k,
            hybrid100=tuple(hybrid_ids),
            pool50_order=tuple(pool_ids),
            pool50_scores=dict(scores),
        )
        return {
            **ranked,
            "runtime_identity": {
                **ranked["runtime_identity"],
                "hybrid100_provider_receipt_sha256": hybrid_sha,
                "pool50_provider_receipt_sha256": pool_sha,
            },
        }

    return pipeline.ask_with_char_rrf(
        question, candidate_id=candidate_id, rank_sources=rank_sources,
        write_receipt=write_receipt, top_k=top_k,
    )
