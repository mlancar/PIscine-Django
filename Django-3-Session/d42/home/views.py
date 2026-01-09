from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import random


# Create your views here.

def home(request):
    if request.GET.get("logout"):  # si ?logout=1 est dans l'URL
        request.session.pop("user", None)
        return redirect("home") 

    user = request.session.get("user")

    if "username" not in request.session:
        request.session["username"] = random.choice(settings.RANDOM_USER_NAMES)
    random_username = request.session["username"]

    return render(request, 'home/index.html', {
        "user": user,
        "username": random_username,
        "RANDOM_USER_NAMES": settings.RANDOM_USER_NAMES})

def update_username(request):
    username = random.choice(settings.RANDOM_USER_NAMES)
    request.session["username"] = username
    return JsonResponse({"username": username})

def logout(request):
    request.session.pop("user", None)
    return redirect("home")
