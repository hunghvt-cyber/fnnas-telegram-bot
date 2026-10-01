# FnNAS Telegram Bot

## Features

/start
/help
/url
/tapo — Tapo daily maintenance status

## Docker

```bash
docker compose up -d --build
```

## Environment

Copy `.env.example` to `.env` and fill:

- BOT_TOKEN
- ALLOWED_USER_ID

## Status files

General FnNAS status:
`data/status.env`

Tapo daily maintenance status:
`data/tapo-status.env`

The Tapo maintenance job writes the compact status contract into the shared TelegramBot data directory. The bot does not perform maintenance or deletion.
