from django.urls import path
from .views import AccountAuthView
from . import views

urlpatterns = [
    path("", AccountAuthView.as_view(), name="account"),
    path("user-status/", views.user_status, name="user_status"),
     path("logout/", views.logout_view, name="logout"),
]