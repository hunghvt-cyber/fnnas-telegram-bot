from telegram import Update
from telegram.ext import ContextTypes

from config.auth import is_allowed
from config.config import STATUS_FILE
from services.logger import logger
from services.status_reader import load_env_file


def format_tapo(data):
    if not data:
        return "Chưa có Tapo daily status."

    return "\n".join([
        "📹 Tapo Daily Maintenance",
        "",
        f"Status: {data.get('STATUS', 'Unknown')}",
        f"Backup: {data.get('BACKUP', 'Unknown')}",
        f"Verify: {data.get('VERIFY', 'Unknown')}",
        f"Archive cleanup: {data.get('ARCHIVE_CLEANUP', 'Unknown')} ({data.get('ARCHIVE_CLEANUP_COUNT', '0')})",
        f"Retention: {data.get('RETENTION', 'Unknown')} ({data.get('RETENTION_CANDIDATES', '0')} candidates)",
        f"Last update: {data.get('LAST_UPDATE', 'Unknown')}",
    ])


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not is_allowed(user.id):
        logger.warning(f"Unauthorized: {user.id}")
        return

    logger.info(f"/tapo - {user.id}")

    data = load_env_file(STATUS_FILE.replace("status.env", "tapo-status.env"))
    await update.message.reply_text(format_tapo(data))
