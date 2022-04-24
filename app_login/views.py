from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

from app_login.forms import RegistroUsuarios, EditarUsuarios, UserAvatarForm
from app_login.models import Avatar

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# Modulo de Login
def iniciar_sesion(request):

    if request.method == "POST":
            form = AuthenticationForm()
            formulario = AuthenticationForm(request, data=request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data

                nombre_usuario = data.get("username")
                contrasenia = data.get("password")

                usuario = authenticate(username=nombre_usuario, password=contrasenia)

                if usuario is not None:
                    login(request, usuario)
                    return redirect("Inicio")

            else:
                
                return render(request, "app_login/login.html", {"error": "Formulario erroneo","form": form})    
    else:
            form = AuthenticationForm()
            return render(request, "app_login/login.html", {"form": form})

def registro(request):

    if request.method == "POST":

        form = RegistroUsuarios(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "app_entrega1/posts.html", {"mensaje":"El usuario ha sido creado exitosamente"})
        
    else:

        form = RegistroUsuarios()

    return render(request, "app_login/signup.html", {"form":form})

@login_required
def editar_usuario(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    usuario = request.user

    if request.method == "POST":
        
        miFormulario = EditarUsuarios(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()

            return render(request, 'app_login/editarperfil.html', {"miFormulario": miFormulario, "edit_success": True, "avatar": avatar})
        else:
            return render(request, 'app_login/editarperfil.html', {"miFormulario": miFormulario, "avatar": avatar})
    
    else: 

        miFormulario = EditarUsuarios(initial={'email': usuario.email})
        user_avatar_form = UserAvatarForm()

    return render(request, "app_login/editarperfil.html", {"miFormulario":miFormulario, "usuario": usuario, "user_avatar_form": user_avatar_form, "avatar": avatar})

@login_required
def avatar_upload(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    user_avatar_form = UserAvatarForm()
    if request.method == "POST":
        image_form = UserAvatarForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if image_form.is_valid():
            print("valid")
            #Preguntamos por avatar existentes
            existent_avatar = Avatar.objects.filter(user=request.user)
            if len(existent_avatar)>0:
                print(existent_avatar)
                existent_avatar = existent_avatar[0]
                existent_avatar.image = image_form.cleaned_data["image"]
                existent_avatar.save()
                return render(request, 'app_login/editarperfil.html', { "user_avatar_form": image_form, "edit_success": True, "avatar": existent_avatar})
            else:
                try:
                    usuario = User.objects.get(username=request.user)
                    print(usuario)
                    avatar = Avatar(user=usuario, imagen=image_form.cleaned_data["image"])
                    avatar.save()
                    return render(request, 'app_login/editarperfil.html', { "user_avatar_form": image_form, "edit_success": True, "avatar": avatar})
                except Exception as e:
                    print(e)
                    return render(request, 'app_login/editarperfil.html', { "user_avatar_form": image_form, "avatar": None})
        else:
            print("not valid")
            return render(request, 'app_login/editarperfil.html', { "user_avatar_form": image_form, "avatar": avatar})
    else:
        print("hola")
        return render(request, 'app_login/editar_avatar.html', { "user_avatar_form": user_avatar_form, "avatar": avatar})





