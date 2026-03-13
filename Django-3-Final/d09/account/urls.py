from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("user-status/", views.user_status, name="user_status"),
     path("logout/", views.logout_view, name="logout"),
]