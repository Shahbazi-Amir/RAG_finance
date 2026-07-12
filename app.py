import sys
import json
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv


# ==========================
# Project Setup
# ==========================

project_root = Path(__file__).resolve().parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

load_dotenv(project_root / ".env")


# ==========================
# Imports
# ==========================

import config.settings as settings
from src.pipeline.rag_pipeline import RAGPipeline


# ==========================
# Page Config
# ==========================

APP_VERSION = "v04_context_aware_followups"

st.set_page_config(
    page_title="Financial RAG Assistant",
    page_icon="💰",
    layout="centered"
)


# ==========================
# Paths
# ==========================

APP_DATA_DIR = project_root / "data" / "app"
APP_DATA_DIR.mkdir(parents=True, exist_ok=True)

CHAT_HISTORY_FILE = APP_DATA_DIR / "chat_history.json"


# ==========================
# Chat History Helpers
# ==========================

def load_chat_history():
    if not CHAT_HISTORY_FILE.exists():
        return []

    try:
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_chat_history(messages):
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def clear_chat_history():
    st.session_state.messages = []
    save_chat_history([])


# ==========================
# Follow-up Question Helpers
# ==========================

def get_last_user_question(messages):
    for message in reversed(messages):
        if message.get("role") == "user":
            return message.get("content", "")
    return ""


def is_follow_up_question(question: str) -> bool:
    normalized = question.strip().lower()

    short_followups = [
        "نام ببر",
        "اسم ببر",
        "بگو",
        "توضیح بده",
        "بیشتر توضیح بده",
        "بیشتر بگو",
        "ادامه بده",
        "کدام‌ها",
        "کدام ها",
        "چیا هستند",
        "چی هستند",
        "چرا",
        "چطور",
        "مثال بزن",
        "منابعش چیست",
        "منابعش چیه",
        "منابع رو بگو",
        "لینک‌ها را بده",
        "لینک ها را بده",
    ]

    if normalized in short_followups:
        return True

    if len(normalized.split()) <= 3:
        followup_keywords = [
            "این",
            "اون",
            "آن",
            "همین",
            "منابع",
            "نام",
            "ادامه",
            "بیشتر",
            "چرا",
            "چطور",
            "کدام",
        ]

        return any(keyword in normalized for keyword in followup_keywords)

    return False


def rewrite_question_with_context(question: str, messages: list[dict]) -> str:
    if not is_follow_up_question(question):
        return question

    last_user_question = get_last_user_question(messages)

    if not last_user_question:
        return question

    rewritten_question = f"""
با توجه به سؤال قبلی:
{last_user_question}

سؤال جدید:
{question}
"""

    return rewritten_question.strip()


# ==========================
# Load Pipeline
# ==========================

@st.cache_resource
def load_rag_pipeline():
    qdrant_local_path = Path(settings.DATA_VECTORSTORE_PATH) / "qdrant_local"
    cache_file = project_root / "data" / "cache" / "rag_cache.json"

    rag = RAGPipeline(
        vectorstore_path=qdrant_local_path,
        collection_name=settings.COLLECTION_NAME,
        cache_file=cache_file,
        use_cache=True
    )

    return rag


rag = load_rag_pipeline()


# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()


# ==========================
# Sidebar
# ==========================

with st.sidebar:
    st.title("تنظیمات")
    st.caption(f"App version: {APP_VERSION}")

    top_k = st.slider(
        "تعداد منابع بازیابی‌شده",
        min_value=3,
        max_value=10,
        value=5
    )

    st.divider()

    user_questions = [
        message["content"]
        for message in st.session_state.messages
        if message["role"] == "user"
    ]

    st.write("تعداد کل پیام‌ها:", len(st.session_state.messages))
    st.write("تعداد سؤال‌ها:", len(user_questions))

    if user_questions:
        st.divider()
        st.write("سؤال‌های اخیر:")

        for i, question in enumerate(user_questions[-10:], start=1):
            st.caption(f"{i}. {question}")

    st.divider()

    st.write("سؤال‌های پیشنهادی:")

    sample_questions = [
        "سواد مالی یعنی چه؟",
        "منابع سواد مالی چیست؟",
        "نام ببر",
        "آیا سواد مالی فقط سرمایه‌گذاری است؟",
        "بهترین روش خرید بیت‌کوین چیست؟"
    ]

    for sample in sample_questions:
        st.caption(f"- {sample}")

    st.divider()

    if st.button("پاک کردن تاریخچه"):
        clear_chat_history()
        st.rerun()


# ==========================
# Main UI
# ==========================

st.title("💰 Financial RAG Assistant")
st.caption("پرسش‌وپاسخ فارسی بر اساس مقالات مالی دکتر کمیل رودی")


# ==========================
# Render Chat History
# ==========================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message["role"] == "assistant":
            from_cache = message.get("from_cache", False)
            sources = message.get("sources", [])
            rewritten_question = message.get("rewritten_question")

            st.caption(f"From cache: {from_cache}")

            if rewritten_question:
                with st.expander("سؤال بازنویسی‌شده"):
                    st.write(rewritten_question)

            if sources:
                with st.expander("منابع"):
                    for i, source in enumerate(sources, start=1):
                        title = source.get("title")
                        url = source.get("url")
                        score = source.get("score")
                        chunk_id = source.get("chunk_id")

                        st.write(f"{i}. {title}")
                        st.caption(f"Chunk ID: {chunk_id}")
                        st.caption(f"Score: {score}")

                        if url:
                            st.link_button(f"باز کردن منبع {i}", url)
            else:
                st.info("منبعی برای نمایش وجود ندارد.")


# ==========================
# Chat Input
# ==========================

question = st.chat_input("سؤال خود را بنویسید...")

if question:
    rewritten_question = rewrite_question_with_context(
        question=question,
        messages=st.session_state.messages
    )

    user_message = {
        "role": "user",
        "content": question,
        "rewritten_question": rewritten_question,
        "created_at": datetime.now().isoformat()
    }

    st.session_state.messages.append(user_message)
    save_chat_history(st.session_state.messages)

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("در حال تولید پاسخ..."):
            result = rag.ask(
                question=rewritten_question,
                top_k=top_k
            )

        answer = result["answer"]
        sources = result.get("sources", [])
        from_cache = result.get("from_cache", False)

        st.write(answer)
        st.caption(f"From cache: {from_cache}")

        if rewritten_question != question:
            with st.expander("سؤال بازنویسی‌شده"):
                st.write(rewritten_question)

        if sources:
            with st.expander("منابع"):
                for i, source in enumerate(sources, start=1):
                    title = source.get("title")
                    url = source.get("url")
                    score = source.get("score")
                    chunk_id = source.get("chunk_id")

                    st.write(f"{i}. {title}")
                    st.caption(f"Chunk ID: {chunk_id}")
                    st.caption(f"Score: {score}")

                    if url:
                        st.link_button(f"باز کردن منبع {i}", url)
        else:
            st.info("منبعی برای نمایش وجود ندارد.")

        assistant_message = {
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "from_cache": from_cache,
            "rewritten_question": rewritten_question if rewritten_question != question else None,
            "created_at": datetime.now().isoformat()
        }

        st.session_state.messages.append(assistant_message)
        save_chat_history(st.session_state.messages)