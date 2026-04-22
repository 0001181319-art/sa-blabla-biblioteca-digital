# 📚 Biblioteca Digital

Sistema de gerenciamento de acervo literário desenvolvido com Django e Django REST Framework. Projeto de portfólio para vaga de desenvolvedor fullstack Django.

---

## 🛠️ Tecnologias

- **Python 3.10+**
- **Django 4.2**
- **Django REST Framework 3.14**
- **SQLite** (banco de dados padrão)

---

## 📋 Funcionalidades

- ✅ Autenticação com proteção de rotas
- ✅ Dashboard com estatísticas do acervo
- ✅ CRUD completo de **Livros**, **Autores** e **Categorias** via interface web
- ✅ API REST com CRUD completo para todas as entidades
- ✅ Filtro e busca em todas as listagens
- ✅ Mensagens de feedback para todas as ações
- ✅ Validação de formulários (frontend e backend)
- ✅ Tratamento de erros (404, proteção de exclusão, etc.)
- ✅ Interface responsiva e visualmente organizada
- ✅ Herança de templates com `base.html`

---

## 🚀 Como instalar e rodar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd biblioteca
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Carregue os dados iniciais (opcional)

```bash
python manage.py loaddata livros/fixtures/initial_data.json
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

Informe usuário, e-mail (opcional) e senha quando solicitado.

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## 🔗 Rotas Principais

### Interface Web

| Rota | Descrição |
|------|-----------|
| `/login/` | Página de login |
| `/` | Dashboard (requer login) |
| `/livros/` | Lista de livros |
| `/livros/novo/` | Cadastrar livro |
| `/livros/<id>/` | Detalhe do livro |
| `/livros/<id>/editar/` | Editar livro |
| `/livros/<id>/excluir/` | Excluir livro |
| `/autores/` | Lista de autores |
| `/categorias/` | Lista de categorias |
| `/admin/` | Painel administrativo |

### API REST

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/livros/` | Listar livros |
| POST | `/api/livros/` | Criar livro |
| GET | `/api/livros/<id>/` | Detalhe do livro |
| PUT | `/api/livros/<id>/` | Atualizar livro |
| PATCH | `/api/livros/<id>/` | Atualização parcial |
| DELETE | `/api/livros/<id>/` | Excluir livro |
| GET | `/api/livros/por-status/` | Livros agrupados por status |
| GET | `/api/autores/` | Listar autores |
| POST | `/api/autores/` | Criar autor |
| GET | `/api/autores/<id>/` | Detalhe do autor |
| PUT | `/api/autores/<id>/` | Atualizar autor |
| DELETE | `/api/autores/<id>/` | Excluir autor |
| GET | `/api/categorias/` | Listar categorias |
| POST | `/api/categorias/` | Criar categoria |
| GET | `/api/categorias/<id>/` | Detalhe da categoria |
| PUT | `/api/categorias/<id>/` | Atualizar categoria |
| DELETE | `/api/categorias/<id>/` | Excluir categoria |

#### Filtros disponíveis na API

```
GET /api/livros/?q=tolkien
GET /api/livros/?status=disponivel
GET /api/livros/?categoria=1
GET /api/autores/?q=machado
```

---

## 📁 Estrutura do Projeto

```
biblioteca/
├── biblioteca/          # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── livros/              # App principal
│   ├── fixtures/
│   │   └── initial_data.json
│   ├── templates/livros/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── livro_list.html
│   │   ├── livro_detail.html
│   │   ├── livro_form.html
│   │   ├── autor_list.html
│   │   ├── autor_form.html
│   │   ├── categoria_list.html
│   │   ├── categoria_form.html
│   │   └── confirm_delete.html
│   ├── admin.py
│   ├── api_urls.py
│   ├── api_views.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py  (incluídas no biblioteca/urls.py)
│   └── views.py
├── static/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔑 Critérios de Avaliação Atendidos

1. **Proteção de Rotas** — decorator `@login_required` em todas as views protegidas; `LOGIN_URL` configurado.
2. **Validação de Formulários** — validação em `forms.py` e `serializers.py`, com mensagens de erro específicas.
3. **Tratamento de Erros** — uso de `get_object_or_404` para registros inexistentes; proteção contra exclusão de autores com livros.
4. **Serialização** — `ModelSerializer` para todas as entidades, com campos extras calculados (`total_livros`, `autor_nome`, etc.).
5. **Status Codes** — `201 Created`, `200 OK`, `400 Bad Request`, `404 Not Found` retornados corretamente.
6. **Estrutura de Rotas** — rotas intuitivas como `/api/livros/`, `/api/autores/`, `/api/categorias/`.
7. **Mensagens de Feedback** — `messages.success` e `messages.error` em todas as ações CRUD.
8. **Herança de Templates** — `base.html` centraliza layout, navbar e mensagens.
9. **Navegação** — menu lateral com links para Dashboard, Livros, Autores e Categorias.
10. **Interface Responsiva** — layout adaptável para mobile com menu hambúrguer.
11. **Organização do Código** — separação clara entre Models, Views, Templates, Forms, Serializers e URLs.
12. **Versionamento** — `.gitignore` incluído; projeto pronto para versionamento com Git.
13. **Documentação** — este `README.md` com instruções completas de instalação e uso.

---


