# Guia Rápido

Este guia irá ajudá-lo a configurar o ambiente de desenvolvimento e executar o projeto Weave localmente.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte instalado:
- [Python](https://www.python.org/downloads/) (versão 3.13+)
- [Docker](https://www.docker.com/products/docker-desktop/) e Docker Compose
- [uv](https://github.com/astral-sh/uv) (um instalador de pacotes Python rápido)

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/django-blog-project.git
    cd django-blog-project
    ```

2.  **Configure as variáveis de ambiente:**
    Copie o arquivo de exemplo `.env.example` para `.env` e preencha as variáveis necessárias.

    ```bash
    cp secrets/.env.example secrets/.env
    ```
    > **Nota:** Você precisará preencher `SECRET_KEY`, `DEBUG`, e as configurações do banco de dados.

3.  **Instale as dependências Python:**
    Utilizamos `uv` para gerenciar as dependências.
    
    Você instalar as dependências pelo método tradicional, usando o bom e velho `pip`:

    ```bash
    uv pip install -r requirements.txt
    ```

    Ou usar a maneira mais moderna com o gerenciador `uv`:
    
    ```bash
    uv sync --locked
    ```

## Executando com Docker

A maneira mais simples de rodar o projeto é usando Docker. Esse processo é simplificado através da biblioteca `taskipy`, que nos permite criar atalhos para comandos no terminal.

1.  **Construa os contêineres:**
    Este comando irá construir as imagens e iniciar os serviços (aplicação web e banco de dados).
    Ele será válido apenas da primeira vez que rodar o projeto ou quando tiver que reiniciá-lo.

    ```bash
    task build
    ```

2.  **Suba os contêineres:**
    Este comando irá subir todos os serviços (aplicação web e banco de dados). Rode-o apenas se já tiver rodado o comando de build anterior.

    ```bash
    task run
    ```

3.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:8000](http://localhost:8000).

## Executando Localmente (Sem Docker)

Se preferir rodar a aplicação diretamente na sua máquina:

1.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

2.  **Crie um superusuário:**
    Isso permitirá o acesso ao painel de administração do Django.
    ```bash
    python manage.py createsuperuser
    ```

3.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

4.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:8000](http://localhost:8000).