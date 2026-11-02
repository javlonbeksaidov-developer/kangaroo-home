from django.db import models


class MulkTuri(models.TextChoices):
    SALE = "SALE", "Sotuv"
    RENT = "RENT", "Ijara"


class MulkStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Mavjud"
    RESERVED = "RESERVED", "Band qilingan"
    SOLD = "SOLD", "Sotilgan"
    RENTED = "RENTED", "Ijaraga berilgan"
    UNAVAILABLE = "UNAVAILABLE", "Mavjud emas"


class PublicationStatus(models.TextChoices):
    PENDING = "PENDING", "Tasdiqlash kutilmoqda"
    PUBLISHED = "PUBLISHED", "E'lon qilingan"
    REJECTED = "REJECTED", "Rad etilgan"


class MulkCategory(models.TextChoices):
    APARTMENT = "APARTMENT", "Kvartira"
    HOUSE = "HOUSE", "Hovli"
