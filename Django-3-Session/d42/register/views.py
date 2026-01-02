from django.shortcuts import render
from django.conf import settings
import random

# Create your views here.

def register(request):
    context = {
        
    }
    return render(request, 'register/index.html', context)