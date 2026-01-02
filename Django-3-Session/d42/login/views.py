from django.shortcuts import render
from django.conf import settings
import random

# Create your views here.

def login(request):
    context = {
        
    }
    return render(request, 'login/index.html', context)