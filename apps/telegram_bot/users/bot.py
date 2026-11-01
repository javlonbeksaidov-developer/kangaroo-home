from django.contrib.auth import get_user_model
from telebot import TeleBot

from apps.telegram_bot.models import TelegramUser

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

        telegram_user, created = UserServices.save_user(data)  # noqa: RUF059
        if telegram_user:
            bot.send_message(
                msg.chat.id,
                f"Welcome {telegram_first_name} !\n🏡 Kangaroo Home platformasiga xush kelibsiz!",
                reply_markup=Keyboard.login(),
            )

    User = get_user_model()

    @bot.message_handler(func=lambda message: message.text == "🔐 LOGIN")
    def login(message):
        msg = bot.send_message(message.chat.id, "👤 Username kiriting:")
        bot.register_next_step_handler(msg, get_username)

    def get_username(message):
        username = message.text.strip()
        msg = bot.send_message(message.chat.id, "🔑 Password kiriting:")
        bot.register_next_step_handler(msg, get_password, username)

    def get_password(message, username):
        password = message.text.strip()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and user.is_active:
                telegram_user = TelegramUser.objects.get(
                    telegram_id=message.from_user.id
                )

                telegram_user.user = user
                telegram_user.save(update_fields=["user"])

                is_admin = user.is_staff or user.is_superuser

                if user.profile.profile_image:
                    bot.send_photo(
                        message.chat.id,
                        photo=user.profile.profile_image.open("rb"),
                        caption=f"✅ Xush kelibsiz, {user.username}!",
                        reply_markup=Keyboard.main(is_admin=is_admin)
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        f"✅ Xush kelibsiz, {user.username}!",
                        reply_markup=Keyboard.main(is_admin=is_admin)
                    )

            else:
                bot.send_message(
                    message.chat.id,
                    "❌ Username yoki password noto'g'ri!",
                    reply_markup=Keyboard.login(),
                )

        except User.DoesNotExist:
            bot.send_message(
                message.chat.id,
                "❌ Username yoki password noto'g'ri!",
                reply_markup=Keyboard.login(),
            )

        except TelegramUser.DoesNotExist:
            bot.send_message(
                message.chat.id,
                "❌ Telegram profilingiz topilmadi. /start buyrug'ini yuboring.",
                reply_markup=Keyboard.login(),
            )
