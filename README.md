# FnNAS Telegram Bot

## Features

- /start
- /help
- /status
- /homepage
- /fnnas
- /portainer
- /sftpgo
- /frigate

## Docker

```bash
docker compose up -d --build
```

## Environment

Copy

```
.env.example
```

to

```
.env
```

Fill:

- BOT_TOKEN
- ALLOWED_USER_ID

## Logs

```
logs/bot.log
```

## Status file

```
data/status.env
```