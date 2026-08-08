import os
from pathlib import Path

from dotenv import load_dotenv


def _default_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


RESOURCE_ROOT = Path(
    os.getenv("RAG_FINANCE_RESOURCE_ROOT", str(_default_project_root()))
).resolve()

WRITABLE_ROOT = Path(
    os.getenv(
        "RAG_FINANCE_WRITABLE_ROOT",
        str(RESOURCE_ROOT),
    )
).resolve()

# Launcher loads the delivery .env before Streamlit starts. This keeps normal
# source execution compatible with the existing Phase 1 behavior.
load_dotenv(RESOURCE_ROOT / ".env")
load_dotenv(WRITABLE_ROOT / ".env", override=False)

BASE_DIR = str(RESOURCE_ROOT)

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Qdrant Configuration
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = "financial_knowledge_base"

# Embedding Model
EMBEDDING_MODEL = "text-embedding-3-large"

# LLM Model
LLM_MODEL = "gpt-4o-mini"

# Chunking Settings
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

# Data Paths
DATA_RAW_PATH = str(RESOURCE_ROOT / "data" / "raw")
DATA_PROCESSED_PATH = str(RESOURCE_ROOT / "data" / "processed")
DATA_CHUNKS_PATH = str(RESOURCE_ROOT / "data" / "chunks")
DATA_EMBEDDINGS_PATH = str(RESOURCE_ROOT / "data" / "embeddings")
DATA_VECTORSTORE_PATH = os.getenv(
    "RAG_FINANCE_VECTORSTORE_PATH",
    str(RESOURCE_ROOT / "data" / "vectorstore"),
)
DATA_INDEX_PATH = str(RESOURCE_ROOT / "data" / "index")
