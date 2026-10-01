from telegram.ext import Application, CommandHandler

from config.config import BOT_TOKEN
from commands.start import command as start_command
from commands.help import command as help_command
from commands.url import command as url_command
from commands.tapo import command as tapo_command

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("url", url_command))
app.add_handler(CommandHandler("tapo", tapo_command))

app.run_polling()
