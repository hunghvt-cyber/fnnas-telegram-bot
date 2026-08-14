from telegram import Update
from telegram.ext import ContextTypes

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "FnNAS Telegram Bot\n\nGõ /help để xem lệnh."
    )