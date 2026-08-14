from services.auth_guard import check

async def command(update, context):

    if not await check(update):
        return

    await update.message.reply_text(
        "FnNAS Telegram Bot\n\n/help"
    )