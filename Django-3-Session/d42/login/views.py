from django.shortcuts import render, redirect
from .forms import LoginForm
from .auth_utils import authenticate_user
from django.contrib import messages

# Create your views here.

def login(request):
    user = request.session.get("user")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if not authenticate_user(username, password):
                messages.error(request, "User already exists")
                form.add_error("username", "User already exists")
            
            # elif password != form.cleaned_data.get("confirm_password"):
            #     form.add_error(None, "Passwords do not match")
            
            else:
                request.session["user"] = username
                return redirect("home")
    else:
        form = LoginForm()

    return render(request, "login/index.html", {
        "form": form,
        "user": user
    })
