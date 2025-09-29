from django.contrib.auth.mixins import LoginRequiredMixin
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

from .forms import ArticleForm, CommentForm
from .models import Article
from .services import (
    add_comment,
    add_like,
    get_article_comments,
    get_article_likes,
    get_trending,
)


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):  # noqa
        context = super().get_context_data(**kwargs)
        context['trending'] = get_trending()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        """Adicionando likes no contexto da View"""
        context = super().get_context_data(**kwargs)
        article_id = self.object.id
        context['likes'] = get_article_likes(article_id)
        context['comments'] = get_article_comments(article_id)
        context['comment_form'] = CommentForm()
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('article_list')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user.profile)


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user.profile)


class ArticleLikeView(View):
    """View para incrementar likes"""

    @staticmethod
    def post(request, pk):
        add_like(pk)
        return redirect('article_detail', pk=pk)


class ArticleCommentView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    @staticmethod
    def post(request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user.username
            add_comment(pk, author, form.cleaned_data['text'])
        return redirect('article_detail', pk=pk)
