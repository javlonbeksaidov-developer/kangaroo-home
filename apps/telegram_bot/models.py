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
    username = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Telegram Username"
    )
    first_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Ismi"
    )
    last_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Familiyasi"
    )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Telefon raqami"
    )

    is_active = models.BooleanField(
        default=True, verbose_name="Aktivmi (bloklamaganmi)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Qo'shilgan vaqti"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return f"{self.first_name or 'Foydalanuvchi'} (@{self.username or self.telegram_id})"

    class Meta:
        verbose_name = "Telegram Foydalanuvchi"
        verbose_name_plural = "Telegram Foydalanuvchilar"
