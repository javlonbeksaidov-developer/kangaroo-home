from django.db import models


class Viloyat(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Viloyat")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class Tuman(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tuman yoki Shahar")
    viloyat = models.ForeignKey(Viloyat, on_delete=models.PROTECT, related_name="tuman")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tuman / Shahar"
        verbose_name_plural = "Tumanlar va shaharlar"


class Koordinata(models.Model):
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True, verbose_name="Kenglik"
    )

    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True, verbose_name="Uzunlik"
    )

    mulk = models.OneToOneField(
        "mulk.Mulk",
        on_delete=models.CASCADE,
        related_name="koordinata",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude} - {self.longitude}"

    class Meta:
        verbose_name = "Joylashuv"
        verbose_name_plural = "Joylashuvlar"
