from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from .forms import TipForm
from .models import Tip
import random
from django.db.utils import OperationalError
from django.contrib import messages


# Create your views here.

def home(request):

        if request.GET.get("logout"):  # si ?logout=1 est dans l'URL
            request.session.pop("user", None)
            return redirect("home") 

        user = request.session.get("user")

        if "username" not in request.session:
            request.session["username"] = random.choice(settings.RANDOM_USER_NAMES)
        random_username = request.session["username"]
        
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.session.get("user", "Anonymous")
                tip.save()
                messages.success(request, "Tip created!")
                return redirect("home")

        else:
            form = TipForm()
        try:
            tips = Tip.objects.all()
            # tips_dic = []

            # for tip in tips:
            #     tips_dic.append({
            #         'content': tip.content,
            #         'author': tip.author,
            #         'date': tip.date.isoformat()
            #     })
        except OperationalError:
            tips = []
        return render(request, 'home/index.html', {
            "user": user,
            "username": random_username,
            "RANDOM_USER_NAMES": settings.RANDOM_USER_NAMES,
            "form": form,
            "tips": tips,
            })

def update_username(request):
    username = random.choice(settings.RANDOM_USER_NAMES)
    request.session["username"] = username
    return JsonResponse({"username": username})

def logout(request):
    request.session.pop("user", None) 
    return redirect("home")

def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    tip.delete()
    return redirect("home")
