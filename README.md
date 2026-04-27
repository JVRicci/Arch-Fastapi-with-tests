# FastAPI Architecture Project

## Descrição Geral

Este é um projeto de exemplo que demonstra uma arquitetura modular para aplicações web utilizando o framework FastAPI em Python. O projeto foca em operações relacionadas a usuários, incluindo registro, validação e gerenciamento básico de dados. Ele serve como base para construir APIs REST robustas e escaláveis, seguindo boas práticas de organização de código.

## Estrutura das Pastas

O projeto está organizado de forma modular para facilitar a manutenção e escalabilidade:

- `main.py`: Ponto de entrada principal da aplicação.
- `src/`: Diretório contendo todo o código fonte da aplicação.
  - `controllers/`: Controladores que lidam com a lógica de requisições HTTP.
    - `user_controller.py`: Controlador para operações relacionadas a usuários.
  - `database/`: Configurações e conexões com o banco de dados.
    - `db.py`: Configuração da conexão com o banco de dados.
  - `models/`: Modelos de dados da aplicação.
    - `user_model.py`: Modelo de dados para usuários.
  - `routes/`: Definição das rotas da API.
    - `user_routes.py`: Rotas relacionadas a usuários.
  - `services/`: Lógica de negócio e serviços da aplicação.
    - `user_services.py`: Serviços para manipulação de usuários.
  - `utils/`: Utilitários diversos.
    - `email_regex.py`: Expressões regulares para validação de emails.
  - `validators/`: Validadores para entrada de dados.
    - `user_register_validator.py`: Validador para registro de usuários.
  - `server/`: Configurações do servidor.
    - `server.py`: Configuração do servidor FastAPI.
- `tests/`: Diretório contendo os testes da aplicação.
  - `test_users.py`: Testes para funcionalidades de usuários.
- `requirements.txt`: Lista de dependências Python necessárias.
- `pyproject.toml`: Arquivo de configuração do projeto (usado por ferramentas como Poetry).
- `pytest.ini`: Configuração para execução de testes com pytest.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd fastapi-arch-project
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para executar a aplicação em modo de desenvolvimento:

```bash
python main.py
```

Ou utilizando Uvicorn diretamente:

```bash
uvicorn src.server.server:app --reload
```

A aplicação estará disponível em `http://localhost:8000`. Você pode acessar a documentação automática da API em `http://localhost:8000/docs` (Swagger UI) ou `http://localhost:8000/redoc` (ReDoc).

## Testes

Para executar os testes:

```bash
pytest
```

Ou com mais detalhes:

```bash
pytest -v
```