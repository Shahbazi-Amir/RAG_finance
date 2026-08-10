import asyncio
import logging
import mimetypes
import os
import sys
from pathlib import Path

import bale
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

import config.settings as settings
from src.database.bale_feedback import (
    initialize_feedback_database,
    save_audio_feedback,
    save_text_feedback,
)
from src.pipeline.rag_pipeline import RAGPipeline


logging.basicConfig(
    level=os.getenv("BALE_LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("ragfinance.bale")

BALE_BOT_TOKEN = os.getenv("BALE_BOT_TOKEN")
if not BALE_BOT_TOKEN:
    raise RuntimeError("BALE_BOT_TOKEN is not set")

TOP_K = int(os.getenv("BALE_TOP_K", "5"))
FEEDBACK_BUTTON = "📝 ارسال بازخورد"
CANCEL_FEEDBACK_BUTTON = "❌ لغو بازخورد"

AUDIO_DIR = PROJECT_ROOT / "data" / "bale_feedback_audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_BALE_VECTORSTORE = (
    PROJECT_ROOT / "data" / "vectorstore" / "qdrant_bale"
)
BALE_VECTORSTORE_PATH = Path(
    os.getenv("BALE_VECTORSTORE_PATH", str(DEFAULT_BALE_VECTORSTORE))
).expanduser().resolve()

BALE_CACHE_FILE = PROJECT_ROOT / "data" / "cache" / "bale_rag_cache.json"
BALE_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

if not BALE_VECTORSTORE_PATH.exists():
    raise FileNotFoundError(
        "Bale vector store was not found at "
        f"{BALE_VECTORSTORE_PATH}. Copy qdrant_local to qdrant_bale on the server."
    )

initialize_feedback_database()

rag = RAGPipeline(
    vectorstore_path=BALE_VECTORSTORE_PATH,
    collection_name=settings.COLLECTION_NAME,
    cache_file=BALE_CACHE_FILE,
    use_cache=True,
)

bot = bale.Bot(token=BALE_BOT_TOKEN)
feedback_mode_chats: set[str] = set()


def main_menu() -> bale.MenuKeyboardMarkup:
    menu = bale.MenuKeyboardMarkup()
    menu.add(bale.MenuKeyboardButton(FEEDBACK_BUTTON), row=1)
    return menu


def feedback_menu() -> bale.MenuKeyboardMarkup:
    menu = bale.MenuKeyboardMarkup()
    menu.add(bale.MenuKeyboardButton(CANCEL_FEEDBACK_BUTTON), row=1)
    return menu


def message_identity(message: bale.Message) -> tuple[str, str | None, str | None]:
    chat_id = str(message.chat_id)
    author = message.author
    user_id = str(author.id) if author else None
    username = author.username if author else None
    return chat_id, user_id, username


def is_audio_feedback(message: bale.Message) -> bool:
    attachment = message.attachment
    if not attachment:
        return False

    if message.audio is not None:
        return True

    mime_type = getattr(attachment, "mime_type", None)
    return bool(mime_type and mime_type.lower().startswith("audio/"))


def audio_extension(message: bale.Message) -> str:
    attachment = message.attachment
    file_name = getattr(attachment, "file_name", None)
    if file_name:
        suffix = Path(file_name).suffix
        if suffix and len(suffix) <= 10:
            return suffix.lower()

    mime_type = getattr(attachment, "mime_type", None)
    guessed = mimetypes.guess_extension(mime_type or "")
    return guessed or ".ogg"


def format_sources(sources: list[dict]) -> str:
    lines = []
    for index, source in enumerate(sources, start=1):
        title = source.get("title") or f"منبع {index}"
        url = source.get("url")
        if url:
            lines.append(f"{index}. {title}\n{url}")
        else:
            lines.append(f"{index}. {title}")
    return "\n\n".join(lines)


def split_text(text: str, limit: int = 3900) -> list[str]:
    text = text.strip()
    if len(text) <= limit:
        return [text]

    chunks: list[str] = []
    remaining = text
    while remaining:
        if len(remaining) <= limit:
            chunks.append(remaining)
            break

        cut = remaining.rfind("\n", 0, limit)
        if cut < limit // 2:
            cut = remaining.rfind(" ", 0, limit)
        if cut < limit // 2:
            cut = limit

        chunks.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()

    return [chunk for chunk in chunks if chunk]


async def reply_chunks(
    message: bale.Message,
    text: str,
    *,
    components: bale.MenuKeyboardMarkup | None = None,
) -> None:
    chunks = split_text(text)
    for index, chunk in enumerate(chunks):
        await message.reply(
            chunk,
            components=components if index == len(chunks) - 1 else None,
        )


async def save_feedback_audio(message: bale.Message) -> None:
    attachment = message.attachment
    if attachment is None:
        raise ValueError("Audio attachment is missing")

    chat_id, user_id, username = message_identity(message)
    extension = audio_extension(message)
    safe_message_id = str(message.message_id).replace("/", "_")
    file_name = f"{chat_id}_{safe_message_id}{extension}"
    destination = AUDIO_DIR / file_name

    audio_bytes = await attachment.get()
    destination.write_bytes(audio_bytes)

    save_audio_feedback(
        chat_id=chat_id,
        user_id=user_id,
        username=username,
        message_id=str(message.message_id),
        audio_path=str(destination.relative_to(PROJECT_ROOT)),
        mime_type=getattr(attachment, "mime_type", None),
    )


async def answer_rag(message: bale.Message, question: str) -> None:
    await message.reply("در حال بررسی سؤال شما...", components=main_menu())

    try:
        result = await asyncio.to_thread(rag.ask, question, TOP_K)
    except Exception:
        logger.exception("RAG request failed for chat_id=%s", message.chat_id)
        await message.reply(
            "در حال حاضر امکان تولید پاسخ وجود ندارد. لطفاً کمی بعد دوباره تلاش کنید.",
            components=main_menu(),
        )
        return

    answer = result.get("answer") or "پاسخی تولید نشد."
    await reply_chunks(message, answer, components=main_menu())

    sources = result.get("sources") or []
    if sources:
        await reply_chunks(
            message,
            "منابع:\n\n" + format_sources(sources),
            components=main_menu(),
        )


@bot.event
async def on_before_ready():
    # Polling and webhook must not be active at the same time.
    await bot.delete_webhook()


@bot.event
async def on_ready():
    logger.info("Bale bot is ready as @%s", getattr(bot.user, "username", "unknown"))


@bot.event
async def on_message(message: bale.Message):
    if message.author and message.author.is_bot:
        return

    chat_key = str(message.chat_id)
    content = (message.content or "").strip()

    if content == "/start":
        feedback_mode_chats.discard(chat_key)
        await message.reply(
            "سلام. من دستیار مالی RAG هستم. سؤال خود را همین‌جا بنویسید.\n\n"
            "برای ثبت نظر درباره برنامه، گزینه «ارسال بازخورد» را بزنید؛ "
            "بعد می‌توانید بازخورد را به‌صورت متن یا صدا ارسال کنید.",
            components=main_menu(),
        )
        return

    if content == FEEDBACK_BUTTON or content == "/feedback":
        feedback_mode_chats.add(chat_key)
        await message.reply(
            "بازخوردتان را بفرستید. می‌توانید متن بنویسید یا یک پیام صوتی ارسال کنید.",
            components=feedback_menu(),
        )
        return

    if content == CANCEL_FEEDBACK_BUTTON or content == "/cancel":
        feedback_mode_chats.discard(chat_key)
        await message.reply("ارسال بازخورد لغو شد.", components=main_menu())
        return

    if chat_key in feedback_mode_chats:
        chat_id, user_id, username = message_identity(message)

        try:
            if is_audio_feedback(message):
                await save_feedback_audio(message)
                feedback_mode_chats.discard(chat_key)
                await message.reply(
                    "بازخورد صوتی شما ذخیره شد. ممنونم.",
                    components=main_menu(),
                )
                return

            if content:
                save_text_feedback(
                    chat_id=chat_id,
                    user_id=user_id,
                    username=username,
                    message_id=str(message.message_id),
                    text=content,
                )
                feedback_mode_chats.discard(chat_key)
                await message.reply(
                    "بازخورد متنی شما ذخیره شد. ممنونم.",
                    components=main_menu(),
                )
                return

            await message.reply(
                "فقط متن یا پیام صوتی بفرستید، یا «لغو بازخورد» را بزنید.",
                components=feedback_menu(),
            )
        except Exception:
            logger.exception("Failed to save Bale feedback for chat_id=%s", chat_id)
            await message.reply(
                "ذخیره بازخورد با خطا مواجه شد. لطفاً دوباره تلاش کنید.",
                components=feedback_menu(),
            )
        return

    if is_audio_feedback(message):
        await message.reply(
            "برای ثبت این صدا به‌عنوان بازخورد، ابتدا گزینه «ارسال بازخورد» را بزنید.",
            components=main_menu(),
        )
        return

    if not content:
        await message.reply(
            "لطفاً سؤال خود را به‌صورت متن ارسال کنید.",
            components=main_menu(),
        )
        return

    await answer_rag(message, content)


if __name__ == "__main__":
    try:
        bot.run()
    finally:
        rag.close()
