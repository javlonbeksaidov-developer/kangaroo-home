from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            messages.error(request, message="Username or password is wrong !")
            return redirect("authentication:login")

        login(request=request, user=user)
        return redirect("main:home")
    return render(request, "authentication/login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name", "")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password == password_confirm:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
        user.save()

        if user:
            return redirect("authentication:login")
    return render(request, "authentication/register.html")


def logout_page(request):
    logout(request)
    return redirect("authentication:login")
