from telegram import Update
from telegram.ext import ContextTypes

from services.status_reader import load_status

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = load_status()

    text = ""

    for k, v in data.items():
        text += f"{k}\n{v}\n\n"

    if text == "":
        text = "status.env chưa tồn tại."

    await update.message.reply_text(text)