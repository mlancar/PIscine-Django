from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        
        model = User
        fields = ("username",  )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = None
    
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": _("username")
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": _("password")
        })
        
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": _("confirm password")
        })