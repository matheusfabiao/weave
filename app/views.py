import os
from urllib.parse import unquote

from django.conf import settings
from django.http import Http404, HttpResponse
from django.utils._os import safe_join  # noqa
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


def docs_view(request, path=''):
    docs_root = os.path.join(settings.BASE_DIR, 'docs_build')

    # Decodifica o path e remove trailing slash se existir
    path = unquote(path).rstrip('/') if path else ''

    # Se o path estiver vazio, serve o index
    if not path:
        path = 'index.html'

    # Se o path não terminar com .html e não tiver extensão, adiciona index.html  # noqa
    elif not path.endswith('.html') and '.' not in os.path.basename(path):
        path = os.path.join(path, 'index.html')

    file_path = safe_join(docs_root, path)

    if not os.path.exists(file_path):
        raise Http404(f'Arquivo não encontrado: {path}')

    with open(file_path, 'rb') as f:
        content = f.read()

    response = HttpResponse(content)

    # Define content type apropriado
    if path.endswith('.css'):
        response['Content-Type'] = 'text/css'
    elif path.endswith('.js'):
        response['Content-Type'] = 'application/javascript'
    elif path.endswith('.png'):
        response['Content-Type'] = 'image/png'
    elif path.endswith('.jpg') or path.endswith('.jpeg'):
        response['Content-Type'] = 'image/jpeg'
    else:
        response['Content-Type'] = 'text/html'

    return response
