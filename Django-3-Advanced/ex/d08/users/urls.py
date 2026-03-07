from django.contrib.auth.views import  LogoutView
from django.urls import path
from .views import RegisterView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", CustomLoginView.as_view(redirect_authenticated_user=True, template_name="register/index.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]