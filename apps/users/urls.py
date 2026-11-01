from django.urls import path

from .views import ProfilePage

app_name = "users"

urlpatterns = [
    path("", ProfilePage.as_view(), name="user"),
]