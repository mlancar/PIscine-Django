from django.shortcuts import render, redirect
from .forms import RegisterForm
import logging
from .auth_utils import create_user
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login


# Create your views here.

def register(request):
    User = get_user_model()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            if password != form.cleaned_data.get("confirm_password"):
                form.add_error(None, "Passwords do not match")
            
            elif User.objects.filter(username=username).exists():
                form.add_error("username", "User already exists")

            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)

                messages.success(request, "Registration successful 🎉")
                return redirect("home")       
    else:
        form = RegisterForm()

    return render(request, "register/index.html", {
        "form": form,
    })