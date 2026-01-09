from django import forms
from django.conf import settings

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get("username")
        password = cleaned.get("password")

        if not username or not password:
            return cleaned

        if username not in settings.USERS_DB:
            raise forms.ValidationError("User does not exists")

        if settings.USERS_DB[username] != password:
            raise forms.ValidationError("Invalid password")

        return cleaned
