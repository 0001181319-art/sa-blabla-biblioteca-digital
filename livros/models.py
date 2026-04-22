from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Autor(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    nacionalidade = models.CharField(max_length=100, verbose_name='Nacionalidade')
    biografia = models.TextField(blank=True, verbose_name='Biografia')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('reservado', 'Reservado'),
    ]

    titulo = models.CharField(max_length=300, verbose_name='Título')
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros', verbose_name='Autor')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='livros', verbose_name='Categoria')
    isbn = models.CharField(max_length=20, unique=True, verbose_name='ISBN')
    ano_publicacao = models.IntegerField(
        verbose_name='Ano de Publicação',
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    sinopse = models.TextField(blank=True, verbose_name='Sinopse')
    paginas = models.IntegerField(verbose_name='Número de Páginas', validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel', verbose_name='Status')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return f'{self.titulo} — {self.autor.nome}'
