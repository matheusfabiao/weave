# Weave - Rede Social para Desenvolvedores

![Licença](https://img.shields.io/badge/license-MIT-blue.svg)

## 📖 Sobre

O Weave é uma rede social para a comunidade de tecnologia, inspirada em plataformas como Twitter e DevMedia. Seu grande diferencial é a criação de artigos em Markdown, com a possibilidade de utilizar Inteligência Artificial para aprimorar ou gerar conteúdo.

Este projeto foi desenvolvido como um ambiente para aprendizado e portfólio, demonstrando habilidades em desenvolvimento web com Django, Docker e integração com serviços de IA.

## ✨ Funcionalidades

*   **Autenticação de Usuários:** Sistema completo de registro e login.
*   **Perfis de Usuário:** Cada usuário possui um perfil customizável.
*   **Criação de Artigos:** Escreva e publique artigos utilizando a sintaxe Markdown.
*   **Assistente de IA:** Utilize o poder do Google Gemini para gerar ou melhorar o conteúdo dos seus artigos.
*   **Sistema de Tags:** Organize e encontre artigos por tags.
*   **Ambiente Dockerizado:** Facilidade na configuração e execução do ambiente de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Django
*   **Banco de Dados:** PostgreSQL (via Docker)
*   **Cache:** Redis
*   **Inteligência Artificial:** Google Gemini
*   **Autenticação Social:** Firebase Admin
*   **Containerização:** Docker & Docker Compose
*   **Gerenciador de Tarefas:** Taskipy
*   **Linter/Formatter:** Ruff

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   [Python 3.13+](https://www.python.org/downloads/) (para o gerenciador de pacotes `uv` e `taskipy`)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/matheusfabiao/django-blog-project.git
    cd django-blog-project
    ```

2.  **Instale as dependências do projeto (Taskipy):**
    ```bash
    pip install taskipy
    ```

3.  **Configure as variáveis de ambiente:**
    - Renomeie o arquivo `secrets/.env.example` para `secrets/.env`.
    - Preencha as variáveis com suas credenciais (chave secreta do Django, credenciais do banco de dados, etc.).

4.  **Configure as credenciais do Firebase:**
    - Renomeie o arquivo `secrets/firebase_credentials_example.json` para `secrets/firebase_credentials.json`.
    - Adicione as credenciais da sua conta de serviço do Firebase neste arquivo.

5.  **Construa e inicie os containers Docker:**
    Este comando irá construir as imagens, iniciar os containers e aplicar as migrações do banco de dados.
    ```bash
    task build
    ```
    *Como alternativa, você pode executar `docker-compose up --build`.*

6.  **Acesse a aplicação:**
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