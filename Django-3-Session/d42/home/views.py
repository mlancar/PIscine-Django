from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from .forms import TipForm
from .models import Tip
from .models import User
import random
from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.models import Permission

# Create your views here.

def home(request):

    if request.GET.get("logout"):  # si ?logout=1 est dans l'URL
        logout(request)
        return redirect("home") 

    user = request.user

    if not request.user.is_authenticated:
        if "username" not in request.session:
            request.session["username"] = random.choice(settings.RANDOM_USER_NAMES)
        random_username = request.session["username"]
    else:
        random_username = request.user.username

    form = TipForm()
    tips = Tip.objects.all()
    tips_dic = []

    for tip in tips:
        tips_dic.append({
            'id': tip.id,
            'content': tip.content,
            'author': tip.author,
            'date': tip.date,
            'nb_upvotes': tip.up_vote.count(),
            'nb_downvotes': tip.down_vote.count(),
        })
    return render(request, 'home/index.html', {
        "user": user,
        "username": random_username,
        "RANDOM_USER_NAMES": settings.RANDOM_USER_NAMES,
        "user_obj": user,
        'tips': tips_dic,
        "form": form,
        })

def create_tip(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, "Tip created!")

            perm = Permission.objects.get(codename="downvoter")
            request.user.user_permissions.add(perm)  
            return redirect("home")

    else:
        form = TipForm()
        return render(request, 'home/index.html', {'form': form})

def update_username(request):
    username = random.choice(settings.RANDOM_USER_NAMES)
    request.session["username"] = username
    return JsonResponse({"username": username})

# def logout(request):
#     request.session.pop("user", None)
#     return redirect("home")

def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    if not user:
        messages.error(request, "Authorization denied")
        return redirect("home")
    
    if user.is_staff or (tip.author == user):
        user.balance_reputation(tip.up_vote.count(), tip.down_vote.count())
        tip.delete()

    else:
        messages.error(request, "Authorization denied")

    return redirect("home")

def down_vote(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    print("ICI = ", user.has_perm("downvoter"))
    if tip.down_vote.filter(id=user.id).exists():
        tip.down_vote.remove(user)
        user.downvote_increase_reputation()
        messages.success(request, "remove Down Voted!")

    elif tip.up_vote.filter(id=user.id).exists():
        tip.up_vote.remove(user)
        user.upvote_decrease_reputation()
        messages.success(request, "remove Up Voted!")

    elif user.has_perm("downvoter"):
        tip.down_vote.add(user)
        user.downvote_decrease_reputation()
        messages.success(request, "Down Voted!")
    else:
        messages.error(request, "Authorization Denied!")

    return redirect("home")

def up_vote(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    
    user = request.user

    if tip.up_vote.filter(id=user.id).exists():
        tip.up_vote.remove(user)
        user.upvote_decrease_reputation()
        messages.success(request, "remove Up Voted!")
    
    elif tip.down_vote.filter(id=user.id).exists():
        tip.down_vote.remove(user)
        user.downvote_increase_reputation()
        messages.success(request, "remove Down Voted!")
    else:
        tip.up_vote.add(user)
        user.upvote_increase_reputation()
        messages.success(request, "Up Voted!")
    return redirect("home")

def get_user(request):
    
    username = request.session.get("user")
    
    if not username:
        return None
    return User.objects.filter(username=username).first()

# si je suis log ca chnage quand meme le username toutes les 42secondes cest MAL
#je suis anonymous quandje cree un tip