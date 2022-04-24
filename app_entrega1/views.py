from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

from app_entrega1.models import Autores, Editorial, Libros

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'app_entrega1/posts.html')

def about_me(request):
    return render(request, 'app_entrega1/about.html')


def autores(request):

    lista_autores = Autores.objects.all()
    print(lista_autores)

    return render(request,"app_entrega1/autores.html",{"autores":lista_autores}) 

def formulario_autores(request):
    
    if request.method == 'POST':

        miFormulario = AutorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            autor = Autores(data['nombre'],data['apellido'])
    
            autor.save()

        return render(request,"app_entrega1/autoresFormulario.html") 

    else:

        miFormulario = AutorFormulario()

    return render(request,"app_entrega1/autoresFormulario.html",{"miFormulario":miFormulario})    


#busqueda 
def buscar_libros2(request):
    return render(request, 'app_entrega1/buscarlibros.html')

def buscar(request):
    lib_bus=request.GET.get('libro')
    if lib_bus:
        libros= Libros.objects.filter(titulo__icontains= lib_bus)
        print("lib_bus: ", lib_bus)
        print("Libros: ", libros)
        print("type: ", type(libros))
        return render(request, 'app_entrega1/buscarlibros.html', {"libros": libros, "nombre": lib_bus})
    else: 
        respuesta="No enviaste datos"
    return render(request, 'app_entrega1/buscarlibros.html', {"respuesta": respuesta})          

def buscar_libros3(request):

    data = request.GET.get('libro', "")
    error = ""

    if data:
        try:
            libro = Libros.objects.get(titulo=data)
            return render(request, 'app_entrega1/buscarlibros.html', {"libros": libro, "nombre": data})

        except Exception as exc:
            print(exc)
            error = "No existe Libro"
    return render(request, 'app_entrega1/buscarlibros.html', {"error": error})          

def buscar_libros(request):

    data = request.GET.get('libro', "")
    error = ""

    if data:
       # try:
            libros = Libros.objects.filter(titulo__icontains= data)
            print(libros)
            if libros:
                return render(request, 'app_entrega1/buscarlibros.html', {"libros": libros, "nombre": data})
            else: 
                error = "No existe Libro"
    else: 
            error = "No ingreso ningun Libro"        
    return render(request, 'app_entrega1/buscarlibros.html', {"error": error}) 


class LibrosList(ListView):

    model = Libros
    template_name = "app_entrega1/libros_lista.html"

class LibrosDetail(DetailView):

    model = Libros
    template_name = "app_entrega1/libros_detalle.html"

class LibrosCreate(CreateView):

    model = Libros
    success_url = "/app_entrega1/libros/lista"
    fields = ['isbn','idioma','titulo','fecha_publicacion','clasificacion']

class LibrosUpdate(UpdateView):

    model = Libros
    success_url = "/app_entrega1/libros/lista"
    fields = ['idioma','titulo','fecha_publicacion','clasificacion']

class LibrosDelete(DeleteView):

    model = Libros
    success_url = "/app_entrega1/libros/lista/"


