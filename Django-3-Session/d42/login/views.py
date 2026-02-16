from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # print("FORM = ", form)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            print("user = ",user)
            if user is None:
                messages.error(request, "Invalid username or password")
                # form.add_error("username", "User already exists")
            else:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    
    print("ICI LA EHOH")
    return render(request, "login/index.html", {
        "form": form,
    })
