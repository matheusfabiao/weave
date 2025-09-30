# Aplicativo Agente de IA (ai_agent)

O aplicativo `ai_agent` integra a plataforma com a API do Google Gemini para gerar conteúdo de artigos de forma automatizada.

## Funcionalidades

-   **Geração de Artigos:** Permite que os usuários criem um novo artigo fornecendo um conjunto de instruções, como título, ideia central, público-alvo e tom de voz.
-   **Geração de Resumos:** Gera um resumo curto e chamativo para um artigo existente.

## Componentes Principais

### `utils.py`

Este arquivo contém a lógica principal para interagir com a API do Gemini.

-   `generate_ai_article(title, idea, ...)`: Monta o prompt com base nas instruções do usuário, envia para a API do Gemini e retorna o conteúdo do artigo gerado em formato HTML (convertido de Markdown).
-   `generate_ai_article_resume(title, content)`: Cria um prompt para gerar um resumo de um artigo existente e retorna o resultado.

### `views.py`

-   `AIArticleCreateView`: Uma view baseada em classe que manipula as requisições `GET` e `POST` para a criação de artigos via IA.
    -   No método `GET`, exibe o formulário `AIArticleForm`.
    -   No método `POST`, valida os dados do formulário, chama a função `generate_ai_article` e, se bem-sucedido, cria e salva uma nova instância do modelo `Article`.

### `forms.py`

-   `AIArticleForm`: Um formulário que coleta as instruções do usuário para a geração do artigo. Os campos incluem:
    -   `title`: Título do artigo.
    -   `idea`: A ideia central a ser desenvolvida.
    -   `audience`: O público-alvo.
    -   `tone`: O tom de voz (Formal, Casual, Inspirador).
    -   `extra_notes`: Observações adicionais para guiar a IA.

## Endpoints (URLs)

| Rota                | Nome da URL         | View Responsável      | Descrição                               |
| ------------------- | ------------------- | --------------------- | --------------------------------------- |
| `/ai/create/`       | `article_create_ai` | `AIArticleCreateView` | Página para criar um novo artigo com IA. |
