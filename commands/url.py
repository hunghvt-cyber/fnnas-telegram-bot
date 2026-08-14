from telegram import Update
from telegram.ext import ContextTypes

from config.auth import is_allowed
from services.logger import logger
from services.status_reader import load_status
from services.formatter import format_urls


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    if not is_allowed(user.id):
        logger.warning(f"Unauthorized: {user.id}")
        return

    logger.info(f"/url - {user.id}")

    data = load_status()

    await update.message.reply_text(
        format_urls(data)
    )