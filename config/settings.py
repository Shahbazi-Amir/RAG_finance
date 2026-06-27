import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# API KEYS
# ==========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ==========================
# Qdrant Configuration
# ==========================

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

COLLECTION_NAME = "financial_knowledge_base"

# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "text-embedding-3-large"

# ==========================
# LLM Model
# ==========================

LLM_MODEL = "gpt-4o-mini"

# ==========================
# Chunking Settings
# ==========================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ==========================
# Data Paths
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_PATH = os.path.join(BASE_DIR, "data/raw")
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data/processed")
DATA_CHUNKS_PATH = os.path.join(BASE_DIR, "data/chunks")
