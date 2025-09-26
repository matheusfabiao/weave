from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .forms import ArticleForm
from .models import Article
from .services import add_like, get_article_likes


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        """Adicionando likes no contexto da View"""
        context = super().get_context_data(**kwargs)
        article_id = self.object.id
        context['likes'] = get_article_likes(article_id)
        return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleLikeView(View):
    """View para incrementar likes"""

    @staticmethod
    def post(request, pk):
        add_like(pk)
        return redirect('article_detail', pk=pk)
