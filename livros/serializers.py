from rest_framework import serializers
from .models import Livro, Autor, Categoria


class AutorSerializer(serializers.ModelSerializer):
    total_livros = serializers.SerializerMethodField()

    class Meta:
        model = Autor
        fields = ['id', 'nome', 'nacionalidade', 'biografia', 'total_livros', 'criado_em', 'atualizado_em']
        read_only_fields = ['criado_em', 'atualizado_em']

    def get_total_livros(self, obj):
        return obj.livros.count()

    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError('O nome deve ter pelo menos 2 caracteres.')
        return value.strip()


class CategoriaSerializer(serializers.ModelSerializer):
    total_livros = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'total_livros', 'criado_em']
        read_only_fields = ['criado_em']

    def get_total_livros(self, obj):
        return obj.livros.count()

    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError('O nome deve ter pelo menos 2 caracteres.')
        return value.strip()


class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.CharField(source='autor.nome', read_only=True)
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Livro
        fields = [
            'id', 'titulo', 'autor', 'autor_nome', 'categoria', 'categoria_nome',
            'isbn', 'ano_publicacao', 'paginas', 'sinopse', 'status', 'status_display',
            'criado_em', 'atualizado_em'
        ]
        read_only_fields = ['criado_em', 'atualizado_em']

    def validate_titulo(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError('O título deve ter pelo menos 2 caracteres.')
        return value.strip()

    def validate_isbn(self, value):
        cleaned = value.replace('-', '').replace(' ', '')
        if len(cleaned) not in [10, 13]:
            raise serializers.ValidationError('ISBN inválido. Deve ter 10 ou 13 dígitos.')
        return value

    def validate_ano_publicacao(self, value):
        if value < 1000 or value > 2100:
            raise serializers.ValidationError('Ano de publicação inválido.')
        return value

    def validate_paginas(self, value):
        if value < 1:
            raise serializers.ValidationError('O número de páginas deve ser maior que zero.')
        return value
