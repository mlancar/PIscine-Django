from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update-username/", views.update_username, name="update_username"),
]