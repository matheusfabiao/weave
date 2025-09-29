from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from articles.models import Article


@method_decorator(cache_page(60), name='dispatch')
class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'

    @staticmethod
    def get_queryset():
        return Article.objects.order_by('-created_at')[:3]
