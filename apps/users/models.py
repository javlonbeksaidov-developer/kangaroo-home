from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    profile_image = models.ImageField(upload_to="profile_image/", blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username} profili"
