from services.command_helper import reply_url

async def command(update, context):
    await reply_url(update, "PORTAINER", "📦 Portainer")