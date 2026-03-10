from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"