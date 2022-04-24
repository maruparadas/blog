from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_login.views import *


class RegistroUsuarios(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Constraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','first_name', 'last_name','email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}

class EditarUsuarios(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class UserAvatarForm(forms.Form):
    image = forms.ImageField()




