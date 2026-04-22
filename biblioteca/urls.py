from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from livros import views as livro_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', livro_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Web pages
    path('', livro_views.dashboard, name='dashboard'),
    path('livros/', livro_views.livro_list, name='livro_list'),
    path('livros/novo/', livro_views.livro_create, name='livro_create'),
    path('livros/<int:pk>/', livro_views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/editar/', livro_views.livro_update, name='livro_update'),
    path('livros/<int:pk>/excluir/', livro_views.livro_delete, name='livro_delete'),

    path('autores/', livro_views.autor_list, name='autor_list'),
    path('autores/novo/', livro_views.autor_create, name='autor_create'),
    path('autores/<int:pk>/editar/', livro_views.autor_update, name='autor_update'),
    path('autores/<int:pk>/excluir/', livro_views.autor_delete, name='autor_delete'),

    path('categorias/', livro_views.categoria_list, name='categoria_list'),
    path('categorias/novo/', livro_views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', livro_views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/excluir/', livro_views.categoria_delete, name='categoria_delete'),

    # API
    path('api/', include('livros.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
