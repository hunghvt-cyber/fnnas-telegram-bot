from telegram import Update
from telegram.ext import ContextTypes

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """

/status

/homepage

/fnnas

/portainer

/sftpgo

/frigate

"""

    await update.message.reply_text(text)