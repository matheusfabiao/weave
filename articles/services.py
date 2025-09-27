from django.utils import timezone
from firebase_admin import db


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
