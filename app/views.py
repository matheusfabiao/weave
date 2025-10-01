import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from articles.models import Article
from articles.services import get_trending


@method_decorator(cache_page(60), name='dispatch')
class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):  # noqa
        context = super().get_context_data(**kwargs)
        context['trending'] = get_trending()
        return context

    @staticmethod
    def get_queryset():
        return Article.objects.order_by('-created_at')[:3]


def docs_view(request, path='index.html'):
    docs_root = os.path.join(settings.BASE_DIR, 'docs_build')
    file_path = os.path.join(docs_root, path)

    if not os.path.exists(file_path):
        raise Http404('Página não encontrada')

    with open(file_path, encoding='utf-8') as f:
        return HttpResponse(f.read())
