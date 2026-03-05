from django import forms
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get("username")
        password = cleaned.get("password")

        if not username or not password:
            return cleaned
        
        return cleaned


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",  )