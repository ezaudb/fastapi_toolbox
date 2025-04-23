# 🧰 FastAPI Toolbox

Imagem Docker com estrutura pronta para desenvolvimento de APIs modernas com FastAPI, PostgreSQL assíncrono e autenticação JWT.

## ✨ Funcionalidades

- FastAPI com suporte a CORS e middleware customizado  
- Acesso assíncrono ao banco PostgreSQL com SQLAlchemy + asyncpg  
- Controle de versão de banco de dados com Alembic  
- Autenticação via JWT com PyJWT e middleware configurável  
- Registro dinâmico de rotas via `core/registry_route/registry_route.py`  
- Suporte a arquivos `.env` para configuração por ambiente  

## 🛠️ Tecnologias Utilizadas

- `fastapi`  
- `uvicorn`  
- `asyncpg`  
- `sqlalchemy`  
- `alembic`  
- `PyJWT`  
- `dotenv`  

## 🐘 Configuração do PostgreSQL

O Alembic e o SQLAlchemy estão configurados para trabalhar com PostgreSQL via driver `asyncpg`.

Exemplo de variável de ambiente no `.env`:

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@host:5432/nome_do_banco
```

## 🚀 Como Utilizar

1. **Clone o repositório e acesse o diretório:**

```bash
git clone https://github.com/seuusuario/fastapi_toolbox.git
cd fastapi_toolbox
```

2. **Build da imagem Docker:**

```bash
docker build -t fastapi_toolbox ./src
```

3. **Executar o container:**

```bash
docker run -it -p 8000:8000 --name fastapi_app fastapi_toolbox /bin/bash
```

4. **Iniciar a aplicação dentro do container:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📌 Registro de Rotas
Todas as rotas são registradas automaticamente em **core/registry_route/registry_route.py**. 

Acompanha exemplo de duas rotas registradas: /auth/login (para obtenção de token JWT) e /home/welcome (rota protegida)