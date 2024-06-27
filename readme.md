# Workout API

Esta é a `Workout API`, uma API desenvolvida com FastAPI para gerenciar informações relacionadas a atividades físicas, atletas e centros de treinamento.

## Estrutura do Projeto

    fast_api/
    │
    ├── alembic.ini
    ├── alembic/
    │ └── ... (configurações e scripts de migração do Alembic)
    ├── docker-compose.yml
    ├── Makefile
    ├── requirements.txt
    └── workout_api/
    ├── init.py
    ├── athlete/
    ├── categories/
    ├── configs/
    ├── contrib/
    ├── main.py
    ├── routers.py
    └── training_center/


### Descrição dos Arquivos e Diretórios

- `alembic.ini`: Arquivo de configuração para o Alembic, uma ferramenta de migração de banco de dados.
- `alembic/`: Diretório contendo scripts e configurações do Alembic.
- `docker-compose.yml`: Arquivo de configuração para Docker Compose.
- `Makefile`: Arquivo com comandos de automação.
- `requirements.txt`: Arquivo que lista as dependências do projeto.
- `workout_api/`: Diretório principal contendo o código da API.
  - `__init__.py`: Indica que o diretório é um pacote Python.
  - `athlete/`: Contém funcionalidades relacionadas a atletas.
  - `categories/`: Contém funcionalidades relacionadas a categorias.
  - `configs/`: Contém arquivos de configuração.
  - `contrib/`: Geralmente utilizado para código contribuído externamente.
  - `main.py`: Arquivo principal que inicia a aplicação.
  - `routers.py`: Define as rotas da API.
  - `training_center/`: Contém funcionalidades relacionadas ao centro de treinamento.

## Requisitos

- Python 3.8+
- FastAPI
- Alembic
- Docker (opcional, para usar o Docker Compose)
- SQLAlchemy

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/workout_api.git
   cd workout_api
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale todas as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados utilizando Alembic:
    ```bash
    make create-migrations
    make run-migrations
    ```
    Caso o make não funcione no seu ambiente, use:
    ```bash
    alembic revision --autogenerate
    alembic upgrade head
    ```

## Executando a Aplicação

1. Usando Docker

    Se preferir usar Docker, você pode utilizar o Docker Compose:

    ```bash
    docker-compose up --build -d
    ```

2. Localmente

    Para rodar a aplicação localmente, execute o seguinte comando:
    ```bash
    make run
    ```
    Caso o make não funcione no seu ambiente, use:
    ```bash
    uvicorn workout_api.main:app --reload
    ```
## Rotas da API
A documentação completa das rotas da API pode ser acessada através do Swagger UI quando a aplicação estiver em execução:
    
    http://127.0.0.1:8000/docs
    

#

Projeto desenvolvido por Victor Brito durante o bootcap da [DIO](https://www.dio.me/), usando os materias de aula e aplicando conhecimentos adquiridos no bootcamp.