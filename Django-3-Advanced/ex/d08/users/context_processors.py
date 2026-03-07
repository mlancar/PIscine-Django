from .forms import CustomLoginForm

def login_form(request):

    return {"login_form": CustomLoginForm()}