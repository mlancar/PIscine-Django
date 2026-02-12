from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update-username/", views.update_username, name="update_username"),
    path('tip/delete/<int:tip_id>/', views.delete_tip, name='delete_tip'),
    path('tip/upvote/<int:tip_id>/', views.up_vote, name='up_vote'),
    path('tip/downvote/<int:tip_id>/', views.down_vote, name='down_vote'),


]