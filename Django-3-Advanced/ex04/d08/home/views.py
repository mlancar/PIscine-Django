from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def home(request):

    if request.GET.get("logout"):  # si ?logout=1 est dans l'URL
        logout(request)
        return redirect("home") 

    user = request.user

    return render(request, 'home/index.html', {
        "user": user,
        })