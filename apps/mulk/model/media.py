from django.db import models

from apps.mulk.models import Mulk


class Image(models.Model):
    image = models.ImageField(upload_to="mulk_images/", verbose_name="Mulk rasmi")
    is_main = models.BooleanField(default=False, verbose_name="Asosiy rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqt")

    mulk = models.ForeignKey(Mulk, on_delete=models.CASCADE, related_name="image")

    def __str__(self):
        return f"{self.mulk.title} - rasm"

    class Meta:
        verbose_name = "Mulk rasmi"
        verbose_name_plural = "Mulk rasmlari"


class Video(models.Model):
    video = models.FileField(upload_to="mulk_videos/", verbose_name="Mulk videosi")
    title = models.CharField(max_length=255, blank=True, verbose_name="Video nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqt")

    mulk = models.ForeignKey(Mulk, on_delete=models.CASCADE, related_name="vedio")

    def __str__(self):
        return f"{self.mulk.title} - video"

    class Meta:
        verbose_name = "Mulk videosi"
        verbose_name_plural = "Mulk videolari"
