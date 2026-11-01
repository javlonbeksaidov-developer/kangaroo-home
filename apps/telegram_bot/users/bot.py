from telebot import TeleBot

from .keyboard import Keyboard
from .service import UserServices


def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def welcome(msg):
        telegram_id = msg.from_user.id
        telegram_first_name = msg.from_user.first_name
        telegram_last_name = msg.from_user.last_name or ""
        telegram_username = msg.from_user.username or ""

        data = {
            "telegram_id": telegram_id,
            "telegram_first_name": telegram_first_name,
            "telegram_last_name": telegram_last_name,
            "telegram_username": telegram_username,
        }

        telegram_user, created = UserServices.save_user(data)
        if telegram_user:
            bot.send_message(
                msg.chat.id,
                f"Welcome {telegram_first_name} !",
                reply_markup=Keyboard.main(),
            )
