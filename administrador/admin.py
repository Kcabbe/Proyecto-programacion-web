from django.contrib import admin
from administrador.models import Categoria
from administrador.models import Noticia
from administrador.models import Usuario
# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display=("titulo", "texto")
    search_fields=("titulo",)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombreCategoria",)
    search_fields=("nombreCategoria",)

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("email",)
    search_fields=("email",)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Usuario, UsuarioAdmin )

