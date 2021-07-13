from administrador.models import Categoria, Noticia
from rest_framework import viewsets
from administrador.serializer import CategoriaSerializer, NoticiaSerializer

class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class NoticiaViewSet (viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer