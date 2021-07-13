from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from administrador.models import Categoria, Noticia

# Create your views here.

def verNoticias(request):
    noticias = Noticia.objects.all()
    datos = {'noticias': noticias}
    return render(request, 'Noticias.html', datos)

def inicio(request):
    return render(request, 'inicio.html')                                             

def noticias(request):
    return render(request, 'Noticias.html')

def noticiasES(request):
    return render(request, 'Noticiaespa.html')

def contacto(request):
    return render(request, 'PaginaContacto.html')

def paginaCovid(request):
    return render(request, 'paginaCovid.html')

def login(request):
    return render(request, 'Login.html')

def paginaInter(request):
    return render(request, 'paginaInter.html')

def legalizacion(request):
    return render(request, 'paginaLegalizacion.html')
    
def periodistas(request):
    return render(request, 'Periodistas.html')

def registro(request):
    return render(request, 'registro.html')



