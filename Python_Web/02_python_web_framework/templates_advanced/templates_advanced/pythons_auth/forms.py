from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from templates_advanced.pythons_auth.models import PythonsUser


class SignInForm(forms.Form):
    user = None
    username = forms.CharField(
        max_length=20,
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput,
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Username/Password not valid!')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = PythonsUser
        fields = ('username',)
