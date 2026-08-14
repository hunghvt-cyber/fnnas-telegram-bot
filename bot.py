from telegram.ext import (
    Application,
    CommandHandler,
)

from config.config import BOT_TOKEN

from commands import (
    start,
    help,
    status,
    homepage,
    fnnas,
    portainer,
    sftpgo,
    frigate,
)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start.command))
app.add_handler(CommandHandler("help", help.command))
app.add_handler(CommandHandler("status", status.command))
app.add_handler(CommandHandler("homepage", homepage.command))
app.add_handler(CommandHandler("fnnas", fnnas.command))
app.add_handler(CommandHandler("portainer", portainer.command))
app.add_handler(CommandHandler("sftpgo", sftpgo.command))
app.add_handler(CommandHandler("frigate", frigate.command))
from services.logger import logger

logger.info("FnNAS Telegram Bot started")
app.run_polling()