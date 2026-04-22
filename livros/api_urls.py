from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AutorViewSet, CategoriaViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='api-autores')
router.register(r'categorias', CategoriaViewSet, basename='api-categorias')
router.register(r'livros', LivroViewSet, basename='api-livros')

urlpatterns = [
    path('', include(router.urls)),
]
