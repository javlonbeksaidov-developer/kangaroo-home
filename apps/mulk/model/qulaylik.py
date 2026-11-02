from django.db import models


class Qulaylik(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Qulaylik nomi")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Ikonka nomi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Qulaylik"
        verbose_name_plural = "Qulayliklar"


class MulkQulaylik(models.Model):
    mulk = models.ForeignKey(
        "mulk.Mulk", on_delete=models.CASCADE, related_name="mulk_qulayliklari"
    )

    qulaylik = models.ForeignKey(
        "mulk.Qulaylik", on_delete=models.PROTECT, related_name="mulk_boglanishlari"
    )

    def __str__(self):
        return f"{self.mulk.title} - {self.qulaylik.name}"

    class Meta:
        verbose_name = "Mulk qulayligi"
        verbose_name_plural = "Mulk qulayliklari"
