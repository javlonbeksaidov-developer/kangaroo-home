from apps.telegram_bot.models import TelegramUser


class UserServices:
    @staticmethod
    def save_user(data: dict):
        telegram_user, created = TelegramUser.objects.update_or_create(
            telegram_id=data["telegram_id"],
            defaults={
                "telegram_username": data.get("telegram_username"),
                "telegram_first_name": data.get("telegram_first_name"),
                "telegram_last_name": data.get("telegram_last_name"),
            },
        )

        return telegram_user, created
