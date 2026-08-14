from telegram import Update
from telegram.ext import ContextTypes

from services.status_reader import load_status

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        load_status().get("FNNAS", "Không có dữ liệu.")
    )