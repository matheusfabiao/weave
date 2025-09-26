from django.views.generic import ListView

from articles.models import Article


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'

    @staticmethod
    def get_queryset():
        return Article.objects.order_by('-created_at')[:3]
