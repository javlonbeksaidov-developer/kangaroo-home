import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

# Telegram bot
from decouple import config
from telebot import TeleBot

BOT_TOKEN = config("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN)

from apps.telegram_bot.users.bot import register_handlers as user

user(bot)


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
