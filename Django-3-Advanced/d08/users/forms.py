from django import forms
from django.conf import settings

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


class RegisterForm(forms.Form):
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

    confirm_password = forms.CharField(
        label="Confirm password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password"
        })
    )

    def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirm = cleaned_data.get("confirm_password")

            if password and confirm and password != confirm:
                raise forms.ValidationError("Passwords do not match")

            return cleaned_data

     