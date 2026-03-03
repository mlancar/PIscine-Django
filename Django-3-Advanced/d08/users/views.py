from .forms import RegisterForm, LoginForm
from django.views.generic import CreateView
# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "register/index.html"
    success_url = reverse_lazy("login")