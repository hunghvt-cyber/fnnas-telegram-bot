from telegram import Update
from services.auth_guard import check
from services.status_reader import load_status
from services.formatter import format_url

async def reply_url(update: Update, key: str, title: str):

    if not await check(update):
        return

    data = load_status()

    await update.message.reply_text(
        format_url(
            title,
            data.get(key, "Không có dữ liệu.")
        )
    )