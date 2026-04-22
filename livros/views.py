from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import Livro, Autor, Categoria
from .forms import LoginForm, LivroForm, AutorForm, CategoriaForm


# ─── Auth ────────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.get_full_name() or user.username}!')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'livros/login.html', {'form': form})


# ─── Dashboard ───────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    stats = {
        'total_livros': Livro.objects.count(),
        'total_autores': Autor.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'disponiveis': Livro.objects.filter(status='disponivel').count(),
        'emprestados': Livro.objects.filter(status='emprestado').count(),
        'reservados': Livro.objects.filter(status='reservado').count(),
    }
    livros_recentes = Livro.objects.select_related('autor', 'categoria').order_by('-criado_em')[:5]
    context = {'stats': stats, 'livros_recentes': livros_recentes}
    return render(request, 'livros/dashboard.html', context)


# ─── Livros ──────────────────────────────────────────────────────────────────

@login_required
def livro_list(request):
    q = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    categoria_filter = request.GET.get('categoria', '')

    livros = Livro.objects.select_related('autor', 'categoria').all()

    if q:
        livros = livros.filter(Q(titulo__icontains=q) | Q(autor__nome__icontains=q) | Q(isbn__icontains=q))
    if status_filter:
        livros = livros.filter(status=status_filter)
    if categoria_filter:
        livros = livros.filter(categoria_id=categoria_filter)

    categorias = Categoria.objects.all()
    context = {
        'livros': livros,
        'categorias': categorias,
        'q': q,
        'status_filter': status_filter,
        'categoria_filter': categoria_filter,
        'status_choices': Livro.STATUS_CHOICES,
    }
    return render(request, 'livros/livro_list.html', context)


@login_required
def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro})


@login_required
def livro_create(request):
    form = LivroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        livro = form.save()
        messages.success(request, f'Livro "{livro.titulo}" cadastrado com sucesso!')
        return redirect('livro_list')
    return render(request, 'livros/livro_form.html', {'form': form, 'titulo': 'Novo Livro', 'action': 'Cadastrar'})


@login_required
def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Livro "{livro.titulo}" atualizado com sucesso!')
        return redirect('livro_list')
    return render(request, 'livros/livro_form.html', {'form': form, 'titulo': 'Editar Livro', 'action': 'Salvar', 'livro': livro})


@login_required
def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        titulo = livro.titulo
        livro.delete()
        messages.success(request, f'Livro "{titulo}" excluído com sucesso!')
        return redirect('livro_list')
    return render(request, 'livros/confirm_delete.html', {'objeto': livro, 'tipo': 'Livro', 'cancel_url': 'livro_list'})


# ─── Autores ─────────────────────────────────────────────────────────────────

@login_required
def autor_list(request):
    q = request.GET.get('q', '')
    autores = Autor.objects.annotate(qtd_livros=Count('livros'))
    if q:
        autores = autores.filter(Q(nome__icontains=q) | Q(nacionalidade__icontains=q))
    return render(request, 'livros/autor_list.html', {'autores': autores, 'q': q})


@login_required
def autor_create(request):
    form = AutorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        autor = form.save()
        messages.success(request, f'Autor "{autor.nome}" cadastrado com sucesso!')
        return redirect('autor_list')
    return render(request, 'livros/autor_form.html', {'form': form, 'titulo': 'Novo Autor', 'action': 'Cadastrar'})


@login_required
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Autor "{autor.nome}" atualizado com sucesso!')
        return redirect('autor_list')
    return render(request, 'livros/autor_form.html', {'form': form, 'titulo': 'Editar Autor', 'action': 'Salvar', 'autor': autor})


@login_required
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        try:
            nome = autor.nome
            autor.delete()
            messages.success(request, f'Autor "{nome}" excluído com sucesso!')
        except Exception:
            messages.error(request, 'Não é possível excluir este autor pois ele possui livros cadastrados.')
        return redirect('autor_list')
    return render(request, 'livros/confirm_delete.html', {'objeto': autor, 'tipo': 'Autor', 'cancel_url': 'autor_list'})


# ─── Categorias ──────────────────────────────────────────────────────────────

@login_required
def categoria_list(request):
    q = request.GET.get('q', '')
    categorias = Categoria.objects.annotate(qtd_livros=Count('livros'))
    if q:
        categorias = categorias.filter(nome__icontains=q)
    return render(request, 'livros/categoria_list.html', {'categorias': categorias, 'q': q})


@login_required
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        categoria = form.save()
        messages.success(request, f'Categoria "{categoria.nome}" cadastrada com sucesso!')
        return redirect('categoria_list')
    return render(request, 'livros/categoria_form.html', {'form': form, 'titulo': 'Nova Categoria', 'action': 'Cadastrar'})


@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Categoria "{categoria.nome}" atualizada com sucesso!')
        return redirect('categoria_list')
    return render(request, 'livros/categoria_form.html', {'form': form, 'titulo': 'Editar Categoria', 'action': 'Salvar', 'categoria': categoria})


@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        nome = categoria.nome
        categoria.delete()
        messages.success(request, f'Categoria "{nome}" excluída com sucesso!')
        return redirect('categoria_list')
    return render(request, 'livros/confirm_delete.html', {'objeto': categoria, 'tipo': 'Categoria', 'cancel_url': 'categoria_list'})
