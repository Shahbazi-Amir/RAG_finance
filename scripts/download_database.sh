#!/bin/bash

set -e

SERVER_USER="ubuntu"
SERVER_IP="188.121.105.50"
REMOTE_FILE="/home/ubuntu/RAG_finance/data/database/rag_demo.db"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOCAL_FILE="$PROJECT_ROOT/data/database/rag_demo.db"

mkdir -p "$(dirname "$LOCAL_FILE")"

scp "${SERVER_USER}@${SERVER_IP}:${REMOTE_FILE}" "$LOCAL_FILE"

echo "Database downloaded successfully."