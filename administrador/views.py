from principal.views import noticias
from administrador.models import Categoria, Noticia, Usuario
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.core.files.storage import FileSystemStorage

# Create your views here.

def api(request):
    noticias = Noticia.objects.all()
    datos = {'noticias': noticias}
    return render(request, 'api.html', datos)

def loginAdmin(request):
    return render(request, 'LoginAdmin.html')

def formC(request):
    if request.session.get('nombre'):
        return render(request, 'FormularioCategoria.html')
    else:
        return HttpResponse('No existe la sesion')

def guardarCategoria(request):
    v_idCategoria = request.POST.get('idCategoria')
    v_nombre = request.POST.get('nombreCategoria')

    nuevo=Categoria()
    nuevo.idCategoria = v_idCategoria
    nuevo.nombreCategoria = v_nombre

    Categoria.save(nuevo)
    
    return HttpResponse('La categoria ah sido ingresada correctamente y su nombre es: ' + v_nombre)



def formN(request):
    if request.session.get('nombre'):
        categoria = Categoria.objects.all()
        datos = {'categorias': categoria}
        return render(request, 'FormularioNoticias.html', datos)
    else:
        return HttpResponse('No existe la sesion')

def verN(request):
    if request.session.get('nombre'):
        noticias = Noticia.objects.all()
        datos = {'noticias': noticias}
        return render(request, 'verNoticia.html', datos)
    else:
        return HttpResponse('No existe la sesion')

def guardarNoticia(request):
    v_idNoticia=request.POST.get('idNoticia')
    v_titulo=request.POST.get('titulo')
    v_texto=request.POST.get('texto')
    v_categoria=request.POST.get('categoria')

    #rescata el objeto imagen del formulario
    v_imagen=request.FILES.get('imagen')
    fs = FileSystemStorage()
    file = fs.save(v_imagen.name, v_imagen)

    
    #busca la categoria por ID
    categoria=Categoria.objects.get(idCategoria=v_categoria)


    nuevo=Noticia()
    nuevo.idNoticia=v_idNoticia
    nuevo.titulo=v_titulo
    nuevo.texto=v_texto
    nuevo.imagen=file
    nuevo.categoria=categoria

    Noticia.save(nuevo)

    return redirect('/verN')
    #return HttpResponse(file)

def eliminarNoticia(request, xxx):
   noticia=Noticia.objects.get(idNoticia=xxx)
   Noticia.delete(noticia)
   return redirect('/verN')

def modificarNoticia(request, xxx):
   noticia=Noticia.objects.get(idNoticia=xxx)
   categoria=Categoria.objects.all()
   contexto={'datos':noticia,'categorias': categoria}
   return render(request, 'formModificarNoticia.html', contexto)


def guardarModificarNoticia(request):
    try:
        v_idNoticia=request.POST.get('idNoticia')
        v_titulo=request.POST.get('titulo')
        v_texto=request.POST.get('texto')
        v_imagen=request.POST.get('imagen')
        v_categoria=request.POST.get('categoria')
        #busca la categoria por ID
        categoria=Categoria.objects.get(idCategoria=v_categoria)

        #buscar la noticia a modificar
        noticia=Noticia.objects.get(idNoticia=v_idNoticia)

         #rescata el objeto imagen del formulario
        v_imagen=request.FILES.get('imagen')
        fs = FileSystemStorage()
        file = fs.save(v_imagen.name, v_imagen)

        noticia.titulo=v_titulo
        noticia.texto=v_texto
        noticia.imagen=file
        noticia.categoria=categoria
    
        
        Noticia.save(noticia)
        return redirect('/verN')
        #return HttpResponse('Exito')
    except Exception as e:
        return HttpResponse(e)

def validarusuario(request):
    try:
        v_email=request.POST.get('email')
        v_password=request.POST.get('password')


        usuario=Usuario.objects.get(password=v_password, email=v_email)

        #crear la sesion y redireccionar
        request.session['nombre']=usuario.nombre
        #return HttpResponse(v_password + ' ' + v_email)
        return redirect('/verN')


    except Exception as e:
        return HttpResponse(e)
        #return redirect('/')

def principal(request):
    #nombre='Diego Rivera'

    if request.session.get('nombre'):
        nom=request.session.get('nombre')
        #return HttpResponse('Existe')
        datos={'nombre':nom}
        return render(request, 'verNoticia.html', datos)
    else:
        #return HttpResponse('No existe')
        return redirect('/verN')
''' 
    

    
    
def cerrarSesion(request):
    del request.session['nombre']
    request.session.modified=True
    return redirect('/')
'''