from django.contrib import admin
from .models import Livro, Autor, Categoria


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'criado_em']
    search_fields = ['nome', 'nacionalidade']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado_em']
    search_fields = ['nome']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'isbn', 'status', 'criado_em']
    list_filter = ['status', 'categoria']
    search_fields = ['titulo', 'autor__nome', 'isbn']
