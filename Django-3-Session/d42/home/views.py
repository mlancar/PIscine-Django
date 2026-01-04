from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import random
import json


# Create your views here.

def home(request):
    if "username" not in request.session:
        request.session["username"] = random.choice(settings.RANDOM_USER_NAMES)

    return render(request, 'home/index.html', {
        "username": request.session["username"],
        "RANDOM_USER_NAMES": settings.RANDOM_USER_NAMES})

def update_username(request):
    username = random.choice(settings.RANDOM_USER_NAMES)
    request.session["username"] = username
    return JsonResponse({"username": username})

# json response quand on renvoit que des donnees pas une page html
# render renvoie une page complete, navigateur recharge tout