import sqlite3
from datetime import datetime, timezone
from pathlib import Path


DATABASE_PATH = Path("data/database/bale_feedback.db")


def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_feedback_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS bale_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT NOT NULL,
                user_id TEXT,
                username TEXT,
                message_id TEXT,
                feedback_type TEXT NOT NULL,
                feedback_text TEXT,
                audio_path TEXT,
                mime_type TEXT,
                created_at TEXT NOT NULL
            )
            """
        )


def save_text_feedback(
    *,
    chat_id: str,
    user_id: str | None,
    username: str | None,
    message_id: str | None,
    text: str,
) -> int:
    return _insert_feedback(
        chat_id=chat_id,
        user_id=user_id,
        username=username,
        message_id=message_id,
        feedback_type="text",
        feedback_text=text,
        audio_path=None,
        mime_type=None,
    )


def save_audio_feedback(
    *,
    chat_id: str,
    user_id: str | None,
    username: str | None,
    message_id: str | None,
    audio_path: str,
    mime_type: str | None,
) -> int:
    return _insert_feedback(
        chat_id=chat_id,
        user_id=user_id,
        username=username,
        message_id=message_id,
        feedback_type="audio",
        feedback_text=None,
        audio_path=audio_path,
        mime_type=mime_type,
    )


def _insert_feedback(
    *,
    chat_id: str,
    user_id: str | None,
    username: str | None,
    message_id: str | None,
    feedback_type: str,
    feedback_text: str | None,
    audio_path: str | None,
    mime_type: str | None,
) -> int:
    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO bale_feedback (
                chat_id,
                user_id,
                username,
                message_id,
                feedback_type,
                feedback_text,
                audio_path,
                mime_type,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chat_id,
                user_id,
                username,
                message_id,
                feedback_type,
                feedback_text,
                audio_path,
                mime_type,
                created_at,
            ),
        )
        return int(cursor.lastrowid)
