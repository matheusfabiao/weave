# Aplicativo de Artigos (articles)

O aplicativo `articles` é o núcleo da plataforma, responsável pelo gerenciamento completo de artigos, incluindo criação, leitura, atualização, exclusão (CRUD), além de interações como likes e comentários.

## Funcionalidades

-   **CRUD de Artigos:** Usuários autenticados podem criar, editar e excluir seus próprios artigos.
-   **Listagem e Detalhes:** Todos os usuários podem visualizar a lista de artigos e ver os detalhes de cada um.
-   **Sistema de Likes e Comentários:** Utiliza o Firebase Realtime Database para armazenar e gerenciar likes e comentários em tempo real.
-   **Artigos em Alta (Trending):** Um serviço calcula e exibe os artigos mais populares com base em um score de likes e comentários. O resultado é armazenado em cache com Redis para melhor performance.

## Modelos

-   `Tag`: Modelo para categorizar os artigos. Um artigo pode ter várias tags.
-   `Article`: O modelo principal que armazena o conteúdo do artigo.
    -   `author`: Chave estrangeira para o `Profile` do autor.
    -   `title`: Título do artigo.
    -   `resume`: Um resumo curto do conteúdo.
    -   `content`: O corpo principal do artigo.
    -   `tags`: Relacionamento muitos-para-muitos com o modelo `Tag`.

## `services.py`

Este arquivo desacopla a lógica de negócio das views, especialmente as interações com serviços externos como Firebase e Redis.

-   `get_article_likes`, `add_like`: Funções para ler e incrementar o número de likes de um artigo no Firebase.
-   `get_article_comments`, `add_comment`: Funções para ler e adicionar comentários no Firebase.
-   `get_trending`: Calcula os artigos mais populares. O número de comentários tem um peso maior no cálculo do score. O resultado é cacheado por 5 minutos.

## Views

O aplicativo utiliza views baseadas em classe do Django para as operações CRUD:

-   `ArticleListView`: Lista todos os artigos e inclui os artigos em alta no contexto.
-   `ArticleDetailView`: Exibe um único artigo, seus likes e comentários.
-   `ArticleCreateView`: Formulário para criar um novo artigo.
-   `ArticleUpdateView`: Formulário para editar um artigo existente (restrito ao autor).
-   `ArticleDeleteView`: Página de confirmação para excluir um artigo (restrito ao autor).
-   `ArticleLikeView`: View baseada em função para registrar um like.
-   `ArticleCommentView`: View para processar o envio de novos comentários.

## Endpoints (URLs)

| Rota                      | Nome da URL         | View Responsável      | Descrição                                      |
| ------------------------- | ------------------- | --------------------- | ---------------------------------------------- |
| `/articles/`              | `article_list`      | `ArticleListView`     | Lista todos os artigos.                        |
| `/articles/<int:pk>/`     | `article_detail`    | `ArticleDetailView`   | Exibe os detalhes de um artigo específico.     |
| `/articles/create/`       | `article_create`    | `ArticleCreateView`   | Página para criar um novo artigo.              |
| `/articles/<int:pk>/update/` | `article_update`    | `ArticleUpdateView`   | Página para atualizar um artigo.               |
| `/articles/<int:pk>/delete/` | `article_delete`    | `ArticleDeleteView`   | Página para deletar um artigo.                 |
| `/articles/<int:pk>/like/`  | `article_like`      | `ArticleLikeView`     | Endpoint para registrar um like.               |
| `/articles/<int:pk>/comment/`| `article_comment`   | `ArticleCommentView`  | Endpoint para adicionar um comentário.         |
| `/articles/ai/`           | -                   | -                     | Inclui as URLs do aplicativo `ai_agent`.       |
