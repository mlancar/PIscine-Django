from django import forms

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

     