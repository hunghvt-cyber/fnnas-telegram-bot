# FnNAS Telegram Bot Operating Rules

This file supplements the Global `GEMINI.md` with rules specific to the FnNAS Telegram Bot.

## 1. Environment & Secrets
- **Secrets**: `BOT_TOKEN` and `ALLOWED_USER_ID` belong in the `.env` file.
- **Template**: Use `.env.example` as the reference for required variables.
- **Safety**: Never commit the actual `.env` file or log the `BOT_TOKEN`.

## 2. Docker & Deployment
- **Update Workflow**: Use `docker compose up -d --build` to apply changes.
- **Downtime**: Minimize downtime during redeployment by ensuring the new image is built successfully before restarting.
- **Volumes**: Check `data/` and `logs/` persistence before removing containers.

## 3. Monitoring & Status
- **Status File**: The bot state is tracked in `data/status.env`. Verify this file when troubleshooting bot status.
- **Logs**: Check `logs/bot.log` for runtime errors.

## 4. Constraints
- The bot runs in a Docker container on FnNAS.
- Follow the Python/Aiogram patterns established in the codebase.
