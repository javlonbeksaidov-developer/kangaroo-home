from django.contrib.auth.models import User
from django.db import models


class TelegramUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="telegram_profile",
    )

    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    telegram_username = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Telegram Username"
    )
    telegram_first_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Ismi"
    )
    telegram_last_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Familiyasi"
    )

    joined_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(
            f"{self.telegram_first_name or 'Foydalanuvchi'} - {self.telegram_id}"
        )

    class Meta:
        verbose_name = "Telegram Foydalanuvchi"
        verbose_name_plural = "Telegram Foydalanuvchilar"
