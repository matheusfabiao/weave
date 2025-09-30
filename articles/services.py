from django.core.cache import cache
from django.utils import timezone
from firebase_admin import db

from .models import Article


def __reset_trending_cache() -> None:
    """
    Remove o cache dos artigos do trending quando há um novo
    like ou comentário.
    """
    cache.delete('trending_articles_*')


def get_article_likes(article_id: int) -> int:
    """Retorna o número de likes de um artigo no Firebase"""
    ref = db.reference(f'likes/{article_id}')
    value = ref.get()
    return value if value else 0


def add_like(article_id: int) -> None:
    """Incrementa o contador de likes no Firebase"""
    ref = db.reference(f'likes/{article_id}')
    current = ref.get() or 0
    ref.set(current + 1)
    __reset_trending_cache()


def get_article_comments(article_id: int) -> list:
    """Retorna a lista de comentários de um artigo"""
    ref = db.reference(f'comments/{article_id}')
    comments = ref.get()
    if not comments:
        return []
    # transforma em lista ordenada por data
    result = []
    for key, data in comments.items():
        result.append({
            'id': key,
            'author': data.get('author', 'Anônimo'),
            'text': data.get('text', ''),
            'created_at': data.get('created_at', ''),
        })
    # ordena por data
    result.sort(key=lambda x: x['created_at'])
    return result


def get_article_comment_count(article_id: int) -> int:
    """Retorna o número de comentários de um artigo no Firebase."""
    ref = db.reference(f'comments/{article_id}')
    comments = ref.get(shallow=True)
    return len(comments) if comments else 0


def add_comment(article_id: int, author: str, text: str) -> None:
    """Adiciona comentário a um artigo"""
    ref = db.reference(f'comments/{article_id}')
    new_comment_ref = ref.push()
    new_comment_ref.set({
        'author': author or 'Anônimo',
        'text': text,
        'created_at': (
            timezone.localtime(timezone.now()).strftime('%d/%m/%Y às %H:%M')
        ),
    })
    __reset_trending_cache()


def get_trending(limit: int = 5):
    """
    Retorna os artigos mais populares com base em likes e comentários.
    Número de comentários pesam mais para a pontuação de popularidade (score).
    Usa cache Redis para evitar recomputar a cada chamada.
    """
    cache_key = f'trending_articles_{limit}'
    trending_articles = cache.get(cache_key)

    if trending_articles is not None:
        return trending_articles

    # Se não está em cache, realiza os cálculos
    articles = Article.objects.all()
    article_scores = []

    for article in articles:
        likes = get_article_likes(article.id)
        comment_count = get_article_comment_count(article.id)
        score = likes + (comment_count * 2)

        if score > 0:
            article_scores.append({
                'article': article,
                'score': score,
                'likes': likes,
                'comments': comment_count,
            })

    sorted_articles = sorted(
        article_scores, key=lambda x: x['score'], reverse=True
    )
    trending_articles = [item['article'] for item in sorted_articles][:limit]

    # Salva no cache
    cache.set(cache_key, trending_articles, timeout=60 * 5)
    return trending_articles
