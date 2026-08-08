import importlib
import os
import tempfile
import unittest
from pathlib import Path


class HistoryDatabaseTests(unittest.TestCase):
    def test_successful_conversation_persists_after_reload(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            os.environ["RAG_FINANCE_WRITABLE_ROOT"] = temp_dir
            import src.database.database as database

            database = importlib.reload(database)
            database.initialize_database()
            database.save_conversation(
                session_id="test",
                question="سؤال",
                rewritten_question=None,
                answer="پاسخ",
                sources=[],
                from_cache=False,
                model_name="test",
                response_time_ms=1,
            )
            database = importlib.reload(database)
            rows = database.get_conversations()
            self.assertEqual(rows[0]["question"], "سؤال")
            self.assertEqual(rows[0]["answer"], "پاسخ")
            self.assertTrue(rows[0]["created_at"])
            self.assertEqual(
                database.DATABASE_PATH,
                Path(temp_dir) / "data" / "history.sqlite3",
            )


if __name__ == "__main__":
    unittest.main()
