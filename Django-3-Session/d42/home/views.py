from django.shortcuts import render
from django.conf import settings
import random

# Create your views here.

def home(request):
    username = random.choice(settings.RANDOM_USER_NAMES)
    context = {
        "username": username
    }
    return render(request, 'home/index.html', context)