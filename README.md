# sa-blabla-biblioteca-digital
tive uma dificuldade para fazer mas deu bom (acho)
# 📚 Biblioteca Digital

> Sistema de gerenciamento de acervo literário desenvolvido com **Django 4.2** e **Django REST Framework** como projeto de portfólio fullstack.

---

## 🖥️ Demonstração

| Tela | Descrição |
|------|-----------|
| `/login/` | Autenticação de usuário |
| `/` | Dashboard com estatísticas do acervo |
| `/livros/` | Listagem, busca e filtro de livros |
| `/autores/` | Gerenciamento de autores |
| `/categorias/` | Gerenciamento de categorias |
| `/api/` | API REST navegável (DRF) |

---

## 🚀 Tecnologias

- **Python 3.10+**
- **Django 4.2**
- **Django REST Framework 3.14**
- **SQLite** (banco padrão, sem configuração extra)
- HTML/CSS puro nos templates (sem frameworks externos)

---

## ⚙️ Como instalar e rodar

### Pré-requisitos
- Python 3.10 ou superior instalado
- Git instalado

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/biblioteca-digital.git
cd biblioteca-digital
```

**2. Entre na pasta do projeto**
```bash
cd biblioteca
```

**3. Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**4. Instale as dependências**
```bash
pip install -r requirements.txt
```

**5. Rode as migrações**
```bash
python manage.py makemigrations livros
python manage.py migrate
```

**6. Carregue os dados de exemplo** *(opcional)*
```bash
python manage.py loaddata livros/fixtures/initial_data.json
```

**7. Crie um superusuário**
```bash
python manage.py createsuperuser
```

**8. Inicie o servidor**
```bash
python manage.py runserver
```

Acesse em: **http://localhost:8000**

---

## 🔗 Rotas da aplicação

### Interface Web

| Método | Rota | Descrição | Login? |
|--------|------|-----------|--------|
| GET | `/login/` | Página de login | ❌ |
| GET | `/` | Dashboard | ✅ |
| GET/POST | `/livros/` | Listar livros | ✅ |
| GET/POST | `/livros/novo/` | Cadastrar livro | ✅ |
| GET | `/livros/<id>/` | Detalhe do livro | ✅ |
| GET/POST | `/livros/<id>/editar/` | Editar livro | ✅ |
| POST | `/livros/<id>/excluir/` | Excluir livro | ✅ |
| GET/POST | `/autores/` | Listar autores | ✅ |
| GET/POST | `/categorias/` | Listar categorias | ✅ |

### API REST

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/livros/` | Listar livros |
| POST | `/api/livros/` | Criar livro |
| GET | `/api/livros/<id>/` | Detalhe do livro |
| PUT/PATCH | `/api/livros/<id>/` | Atualizar livro |
| DELETE | `/api/livros/<id>/` | Excluir livro |
| GET | `/api/livros/por-status/` | Livros por status |
| GET | `/api/autores/` | Listar autores |
| POST | `/api/autores/` | Criar autor |
| GET/PUT/DELETE | `/api/autores/<id>/` | CRUD autor |
| GET | `/api/categorias/` | Listar categorias |
| POST | `/api/categorias/` | Criar categoria |
| GET/PUT/DELETE | `/api/categorias/<id>/` | CRUD categoria |

#### Filtros disponíveis na API
```
GET /api/livros/?q=tolkien
GET /api/livros/?status=disponivel
GET /api/livros/?categoria=1
GET /api/autores/?q=machado
```

---

## 📁 Estrutura do projeto

```
biblioteca/
├── biblioteca/                  # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── livros/                      # App principal
│   ├── models.py                # Models: Livro, Autor, Categoria
│   ├── views.py                 # Views web com @login_required
│   ├── forms.py                 # Formulários com validação
│   ├── serializers.py           # ModelSerializers para a API
│   ├── api_views.py             # ViewSets DRF
│   ├── api_urls.py              # Rotas da API
│   ├── admin.py                 # Painel administrativo
│   ├── fixtures/
│   │   └── initial_data.json    # Dados de exemplo
│   └── templates/livros/
│       ├── base.html            # Template base (herança)
│       ├── login.html
│       ├── dashboard.html
│       ├── livro_list.html
│       ├── livro_detail.html
│       ├── livro_form.html
│       ├── autor_list.html
│       ├── autor_form.html
│       ├── categoria_list.html
│       ├── categoria_form.html
│       └── confirm_delete.html
│
├── static/                      # Arquivos estáticos
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✅ Funcionalidades implementadas

- [x] Página de login com autenticação Django
- [x] Proteção de rotas com `@login_required`
- [x] Dashboard com estatísticas do acervo
- [x] CRUD completo de **Livros**, **Autores** e **Categorias**
- [x] Busca e filtros nas listagens
- [x] API REST com CRUD completo (DRF ViewSets)
- [x] `ModelSerializer` com campos calculados
- [x] Status codes HTTP corretos (200, 201, 400, 404)
- [x] Mensagens de feedback em todas as ações
- [x] Validação de formulários com erros específicos
- [x] Tratamento de erros com `get_object_or_404`
- [x] Proteção de exclusão (autor com livros não pode ser excluído)
- [x] Herança de templates com `base.html`
- [x] Menu de navegação lateral funcional
- [x] Interface responsiva com menu hambúrguer para mobile
- [x] Painel administrativo Django (`/admin/`)

---

## 📦 Dependências

```
Django>=4.2,<5.0
djangorestframework>=3.14
```
