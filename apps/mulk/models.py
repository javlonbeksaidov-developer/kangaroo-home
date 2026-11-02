from django.contrib.auth.models import User
from django.db import models

from .model.location import Tuman
from .model.status import (
    MulkCategory,
    MulkStatus,
    MulkTuri,
    PublicationStatus,
)


class Mulk(models.Model):
    title = models.CharField(max_length=255, verbose_name="Mulk nomi")
    description = models.TextField(verbose_name="Tavsif")
    price = models.DecimalField(
        default=0.00, max_digits=15, decimal_places=2, verbose_name="Narxi"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mulklar",
        verbose_name="Mulk egasi",
    )

    tuman = models.ForeignKey(
        Tuman,
        on_delete=models.PROTECT,
        related_name="mulklar",
        verbose_name="Tuman yoki shahar",
    )

    mulk_turi = models.CharField(
        max_length=10,
        choices=MulkTuri.choices,
        default=MulkTuri.SALE,
        verbose_name="Sotuv yoki ijara",
    )

    mulk_status = models.CharField(
        max_length=20,
        choices=MulkStatus.choices,
        default=MulkStatus.AVAILABLE,
        verbose_name="Mulk holati",
    )

    mulk_category = models.CharField(
        max_length=20, choices=MulkCategory.choices, verbose_name="Mulk kategoriyasi"
    )

    elon_status = models.CharField(
        max_length=20,
        choices=PublicationStatus.choices,
        default=PublicationStatus.PENDING,
        verbose_name="E'lon holati",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mulk"
        verbose_name_plural = "Mulklar"
