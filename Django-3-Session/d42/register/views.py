from django.shortcuts import render, redirect
from .forms import RegisterForm
import logging
from .auth_utils import create_user
from django.contrib import messages

# Create your views here.

logger = logging.getLogger('form_logger')

def register(request):
    user = request.session.get("user")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            logger.info(f"register: {register}")
            if not create_user(username, password):
                messages.error(request, "User already exists")
                form.add_error("username", "User already exists")
            
            elif password != form.cleaned_data.get("confirm_password"):
                form.add_error(None, "Passwords do not match")
            
            else:
                request.session["user"] = username
                messages.success(request, "Registration successful 🎉")
                return redirect("home")       
    else:
        form = RegisterForm()

    return render(request, "register/index.html", {
        "form": form,
        "user": user
    })