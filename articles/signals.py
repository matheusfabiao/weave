from django.db.models.signals import pre_save
from django.dispatch import receiver

from ai_agent.utils import generate_ai_article_resume

from .models import Article


@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, **kwargs):
    if not instance.resume:
        try:
            instance.resume = generate_ai_article_resume(
                instance.title, instance.content
            )
            print(f'Resumo automático gerado:\n{instance.resume}')
        except Exception as e:
            instance.resume = None
            print(f'Erro ao gerar resumo automático: {e}')
