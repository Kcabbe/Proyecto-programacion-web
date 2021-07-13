from django.db import router
from rest_framework import routers, urlpatterns
from administrador.viewsets import CategoriaViewSet, NoticiaViewSet

router = routers.SimpleRouter()
router.register('Categoria', CategoriaViewSet)
router.register('Noticia', NoticiaViewSet)

urlpatterns = router.urls

