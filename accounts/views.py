from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model()


def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("products:list-product"))
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    email = request.POST.get("email")
    password = request.POST.get("password")

    # user = User.objects.get(email=email, password=password)
    user = authenticate(email=email, password=password)
    print(user)

    if user:
        login(request, user)
        messages.success(request, "You are logged in now")
        return redirect(reverse_lazy("products:list-product"))
    else:
        messages.error(request, "Invalid creadentials")
        return redirect(reverse_lazy("accounts:login"))


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("products:list-product"))


def user_register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    email = request.POST.get("email")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    name = request.POST.get("name")
    age = request.POST.get("age")

    if password1 != password2:
        messages.error(request, "Password did not match.")
        return redirect(reverse_lazy("accounts:register"))

    user = User.objects.create_user(
        email=email, password=password1, name=name, age=age, user_type="editor")

    messages.success(request, "You are registered successfully.")
    return redirect(reverse_lazy("accounts:login"))
