from .forms import RegisterForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

# Create your views here.

class RegisterView(AccessMixin, FormView):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    
    form_class = RegisterForm
    template_name = "register/index.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)