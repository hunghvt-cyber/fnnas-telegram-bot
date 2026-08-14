from telegram import Update

from config.auth import is_allowed


async def check(update: Update):

    if is_allowed(update.effective_user.id):
        return True

    await update.message.reply_text("Bạn không có quyền sử dụng bot.")

    return False