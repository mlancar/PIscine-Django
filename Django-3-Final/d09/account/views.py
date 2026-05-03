from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import logout, login
from django.views.generic import FormView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.middleware.csrf import rotate_token
from django.middleware.csrf import get_token

class AccountAuthView(TemplateView):
    template_name = "account/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'login_form' not in context:
            context['login_form'] = AuthenticationForm()
        if 'register_form' not in context:
            context['register_form'] = RegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'username' in request.POST and 'password' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return JsonResponse({
                    "success": True,
                    "username": user.username,
                    "new_csrf": get_token(request) 
                })
            else:
                return JsonResponse({
                    "success": False,
                    "errors": login_form.errors
                })
           
        elif 'register_submit' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('account')
            else:
                return self.render_to_response(self.get_context_data(register_form=register_form))
        
        return self.get(request, *args, **kwargs)

def user_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"logged_in": True, "username": request.user.username})
    return JsonResponse({"logged_in": False})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        new_token = get_token(request) 
        response = JsonResponse({'success': True})
        response.set_cookie('csrftoken', new_token)
        # rotate_token(request)
        return response
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "POST required"}, status=400)