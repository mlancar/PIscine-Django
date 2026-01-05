from django.shortcuts import render
from django.conf import settings
from .forms import RegisterForm
import logging

# Create your views here.

logger = logging.getLogger('form_logger')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            logger.info(f"register: {register}")

            return render(request, "register/index.html", {
                "form": RegisterForm(),
                "success": True,
                "username": username
            })
    else:
        form = RegisterForm()

    return render(request, "register/index.html", {
        "form": form
    })