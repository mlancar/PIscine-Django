from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        authentication_form=CustomLoginForm,
        template_name="login/index.html"
        ),
        name="login"
    ),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]