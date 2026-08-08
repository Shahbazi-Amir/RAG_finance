import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _database_path() -> Path:
    writable_root = Path(
        os.getenv(
            "RAG_FINANCE_WRITABLE_ROOT",
            str(Path.cwd()),
        )
    )
    database_dir = writable_root / "data"
    database_dir.mkdir(parents=True, exist_ok=True)
    target = database_dir / "history.sqlite3"
    legacy = writable_root / "database" / "rag_demo.db"
    if not target.exists() and legacy.exists():
        target.write_bytes(legacy.read_bytes())
    return target


DATABASE_PATH = _database_path()


def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                question TEXT NOT NULL,
                rewritten_question TEXT,
                answer TEXT NOT NULL,
                sources_json TEXT,
                from_cache INTEGER NOT NULL DEFAULT 0,
                model_name TEXT,
                created_at TEXT NOT NULL,
                response_time_ms INTEGER
            )
            """
        )


def save_conversation(
    *,
    session_id: str | None,
    question: str,
    rewritten_question: str | None,
    answer: str,
    sources: list[dict[str, Any]] | None,
    from_cache: bool,
    model_name: str | None,
    response_time_ms: int | None,
) -> int:
    created_at = datetime.now(timezone.utc).isoformat()
    sources_json = json.dumps(
        sources or [],
        ensure_ascii=False,
        default=str,
    )

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO conversations (
                session_id,
                question,
                rewritten_question,
                answer,
                sources_json,
                from_cache,
                model_name,
                created_at,
                response_time_ms
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                question,
                rewritten_question,
                answer,
                sources_json,
                int(from_cache),
                model_name,
                created_at,
                response_time_ms,
            ),
        )

        return int(cursor.lastrowid)


def get_conversations(limit: int = 50) -> list[dict[str, Any]]:
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT
                id,
                session_id,
                question,
                rewritten_question,
                answer,
                sources_json,
                from_cache,
                model_name,
                created_at,
                response_time_ms
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    conversations = []

    for row in rows:
        item = dict(row)
        item["sources"] = json.loads(item.pop("sources_json") or "[]")
        item["from_cache"] = bool(item["from_cache"])
        conversations.append(item)

    return conversations
