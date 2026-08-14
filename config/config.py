import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

ALLOWED_USER_ID = int(
    os.getenv("ALLOWED_USER_ID", "0")
)

STATUS_FILE = os.getenv(
    "STATUS_FILE",
    "/app/data/status.env"
)

LOG_FILE = os.getenv(
    "LOG_FILE",
    "/app/logs/bot.log"
)