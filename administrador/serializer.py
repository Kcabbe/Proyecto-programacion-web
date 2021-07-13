from django.db.models import fields
from administrador.models import Categoria, Noticia
from rest_framework import serializers

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class NoticiaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'