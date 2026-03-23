from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_page, name="chat"),
    path('chat/<int:room_id>', views.chat_room, name="chatroom"),

]