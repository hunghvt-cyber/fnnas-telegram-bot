from telegram import Update
from telegram.ext import ContextTypes

from config.auth import is_allowed
from services.logger import logger


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    if not is_allowed(user.id):
        logger.warning(f"Unauthorized: {user.id}")
        return

    logger.info(f"/help - {user.id}")

    await update.message.reply_text(
"""📖 Danh sách lệnh

/start
/help
/url
"""
    )