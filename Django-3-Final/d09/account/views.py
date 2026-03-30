from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "account/account.html"

    def form_valid(self, form):
        # login automatique
        response = super().form_valid(form)
        return JsonResponse({"success": True})

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        return JsonResponse({"success": False, "errors": errors})


def user_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"logged_in": True, "username": request.user.username})
    return JsonResponse({"logged_in": False})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "POST required"}, status=400)