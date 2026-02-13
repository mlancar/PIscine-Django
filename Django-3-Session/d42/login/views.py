from django.shortcuts import render, redirect
from .forms import LoginForm
from .auth_utils import authenticate_user
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)

            if user is None:
                messages.error(request, "User already exists")
                form.add_error("username", "User already exists")

            else:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    return render(request, "login/index.html", {
        "form": form,
    })
