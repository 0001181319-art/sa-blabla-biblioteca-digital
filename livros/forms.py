from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Livro, Autor, Categoria


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu usuário', 'autofocus': True})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '••••••••'})
    )


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'biografia']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome completo do autor'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Brasileiro, Americano...'}),
            'biografia': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Breve biografia...'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 2:
            raise forms.ValidationError('O nome deve ter pelo menos 2 caracteres.')
        return nome


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome da categoria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Descrição opcional...'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 2:
            raise forms.ValidationError('O nome deve ter pelo menos 2 caracteres.')
        return nome


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria', 'isbn', 'ano_publicacao', 'paginas', 'sinopse', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título do livro'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 978-3-16-148410-0'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 2023'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Número de páginas'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Breve sinopse do livro...'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 2:
            raise forms.ValidationError('O título deve ter pelo menos 2 caracteres.')
        return titulo

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').strip()
        cleaned = isbn.replace('-', '').replace(' ', '')
        if len(cleaned) not in [10, 13]:
            raise forms.ValidationError('ISBN inválido. Deve ter 10 ou 13 dígitos.')
        return isbn
