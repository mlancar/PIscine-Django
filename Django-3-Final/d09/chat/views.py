from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Chatroom

# Create your views here.

@login_required(login_url='/account/')
def chat_page(request):
    rooms = Chatroom.objects.all()
    return render(request, "chat/chat.html", {"rooms": rooms})

def chat_room(request, room_id):
    room = Chatroom.objects.get(id=room_id)
    # print("room = ", room)
    return render(request, "chat/chatroom.html", {"room": room})

def room_join(request):
    if request.method == "POST":
        room_id = request.POST["room_id"]
        room = Chatroom.objects.get(id=room_id)
        return redirect(reverse('chat', kwargs={'id': room.id}))
    else:
        return render(request, 'chat/join.html')