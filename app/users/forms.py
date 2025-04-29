from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Mets:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label="Имя пользователя",
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         "class": "form-control",
    #         "placeholder": "Введите имя пользователя",
    #     }))
    # password = forms.CharField(
    #     label="Введите ваш пароль",
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         "class": "form-control",
    #         "placeholder": "Введите ваш пароль",
    #     }),
    # )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()