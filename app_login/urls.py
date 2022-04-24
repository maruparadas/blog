from django.urls import path
from app_login.views import *
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    #path('', inicio, name = "Inicio"),
    path('accounts/login', iniciar_sesion, name = "Login"),
    path('accounts/logout', LogoutView.as_view(template_name = 'app_login/logout.html'), name = "Logout"),
    path('accounts/signup', registro, name = "Signup"),
    path('accounts/profile', editar_usuario, name = "Edit"),
    path('', include("app_entrega1.urls")),
    path('avatar_upload', avatar_upload, name="Avatar")
    ]
