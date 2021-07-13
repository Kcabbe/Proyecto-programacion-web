from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True)
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre Categoria')
    

class Noticia(models.Model):
    idNoticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=50, verbose_name='Titulo')
    texto=models.TextField(max_length=500)
    imagen=models.CharField(max_length=100, default='')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Usuario(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=10)