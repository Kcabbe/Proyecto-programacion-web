"""PruebaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from administrador.views import api, eliminarNoticia, formC, formN, guardarCategoria, guardarModificarNoticia, guardarNoticia, loginAdmin, modificarNoticia, principal, validarusuario, verN
from principal.views import inicio, noticias, noticiasES, contacto, paginaCovid, login,paginaInter, legalizacion, periodistas, registro, verNoticias
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('inicio/', inicio),
    path('noticias', verNoticias),
    path('noticiasEspaciales', noticiasES),
    path('Contacto', contacto),
    path('covid', paginaCovid),
    path('login/', login),
    path('inter', paginaInter),
    path('legalizacion', legalizacion),
    path('periodistas', periodistas),
    path('registro', registro),
    path('loginAdmin', loginAdmin),
    path('formC', formC),
    path('formN', formN),
    path('guardarCategoria', guardarCategoria),
    path('verN', verN),
    path('guardarNoticia', guardarNoticia),
    path('eliminarN/<int:xxx>', eliminarNoticia),
    path('modificarN/<int:xxx>', modificarNoticia),
    path('guardarModificarNoticia', guardarModificarNoticia),
    path('validarusuario', validarusuario),
    path('pri', principal),
    path('api/V1.0/', include('administrador.urls')),
    path('api/V1.0/', include('administrador.urls')),
    path('api', api),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)