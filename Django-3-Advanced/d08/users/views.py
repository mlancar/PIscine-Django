from .forms import RegisterForm, LoginForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

class RegisterView(FormView):

    form_class = RegisterForm
    template_name = "register/index.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)