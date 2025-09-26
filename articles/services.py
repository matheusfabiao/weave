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
