![logo do projeto](docs/assets/weave-logo.png){ width="300" }

# Weave - Plataforma de Blog com IA

![Licença](https://img.shields.io/badge/license-MIT-blue.svg)

## 📖 Sobre

O **Weave** é uma plataforma de blog inteligente que utiliza agentes de IA para auxiliar na criação e gerenciamento de conteúdo.

Este projeto foi desenvolvido como um ambiente para aprendizado e portfólio, demonstrando habilidades em desenvolvimento web com Django, Docker e integração com serviços de IA. Para uma visão mais aprofundada, consulte a **[documentação completa](docs/index.md)**.

## ✨ Funcionalidades

*   **Autenticação de Usuários:** Sistema completo de registro e login.
*   **Perfis de Usuário:** Cada usuário possui um perfil customizável.
*   **Criação de Artigos:** Escreva e publique artigos utilizando a sintaxe Markdown.
*   **Assistente de IA:** Utilize o poder do Google Gemini para gerar ou melhorar o conteúdo dos seus artigos.
*   **Sistema de Tags:** Organize e encontre artigos por tags.
*   **Ambiente Dockerizado:** Facilidade na configuração e execução do ambiente de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Django
*   **Banco de Dados Principal:** PostgreSQL (via Docker)
*   **Cache:** Redis
*   **Inteligência Artificial:** Google Gemini
*   **Integração com Banco de Dados em Nuvem:** Firebase Admin
*   **Containerização:** Docker & Docker Compose
*   **Gerenciador de Tarefas:** Taskipy
*   **Linter/Formatter:** Ruff
*   **Gerenciador de Pacotes:** UV

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

*   [Python 3.13+](https://www.python.org/downloads/)
*   [Docker](https://www.docker.com/get-started) e Docker Compose
*   [uv](https://github.com/astral-sh/uv) (Gerenciador de pacotes)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/matheusfabiao/django-blog-project.git
    cd django-blog-project
    ```

2.  **Configure as variáveis de ambiente:**
    Copie os arquivos de exemplo e preencha com suas credenciais.
    ```bash
    cp secrets/.env.example secrets/.env
    cp secrets/firebase_credentials_example.json secrets/firebase_credentials.json
    ```

3.  **Instale as dependências:**
    O `uv sync` garante que o ambiente virtual esteja exatamente como definido no `uv.lock`.
    ```bash
    uv sync --locked
    ```

4.  **Construa e inicie os containers Docker:**
    Este comando irá construir as imagens, iniciar os serviços e aplicar as migrações do banco de dados.
    ```bash
    task build
    ```
    *Como alternativa, você pode executar `docker-compose up --build`.*

5.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:8000](http://localhost:8000).

### Comandos Úteis (via Taskipy)

*   **Iniciar os containers:** `task run`
*   **Parar os containers:** `task down`
*   **Executar migrações:** `task migrate`
*   **Verificar o código (lint):** `task lint`
*   **Formatar o código:** `task format`

## 👨‍💻 Autor

*   **Matheus Fabião**
*   **GitHub:** [@matheusfabiao](https://github.com/matheusfabiao)
*   **LinkedIn:** [matheusfabiao](https://www.linkedin.com/in/matheusfabiao/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.