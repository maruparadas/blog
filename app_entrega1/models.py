from django.db import models

# Create your models here.

class Libros(models.Model):

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True)
    cuerpo = models.TextField(max_length=1000, null=True) 
    creador=  models.CharField(max_length=100, null=True)
    fecha_publicacion = models.DateField()
    #portada= models.ImageField(null = True, blank = True)
    id = models.IntegerField(primary_key=True)

class Autores(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

class Editorial(models.Model):
    
    nombre = models.CharField(max_length=100)
    web = models.CharField(max_length=40)
    pais_origen = models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)

#class Avatar(models.Model):

 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)