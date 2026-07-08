import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# Base Directory
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================
# API Keys
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

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

# ==========================
# Data Paths
# ==========================

DATA_RAW_PATH = os.path.join(BASE_DIR, "data/raw")
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data/processed")
DATA_CHUNKS_PATH = os.path.join(BASE_DIR, "data/chunks")
DATA_EMBEDDINGS_PATH = os.path.join(BASE_DIR, "data/embeddings")
DATA_VECTORSTORE_PATH = os.path.join(BASE_DIR, "data/vectorstore")
DATA_INDEX_PATH = os.path.join(BASE_DIR, "data/index")