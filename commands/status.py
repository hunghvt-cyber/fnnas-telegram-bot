from services.auth_guard import check
from services.status_reader import load_status
from services.formatter import format_status

async def command(update, context):

    if not await check(update):
        return

    await update.message.reply_text(
        format_status(load_status())
    )