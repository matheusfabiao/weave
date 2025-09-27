from django.urls import include, path

from .views import (
    ArticleCommentView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleLikeView,
    ArticleListView,
    ArticleUpdateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path(
        '<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'
    ),
    path(
        '<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'
    ),
    path('<int:pk>/like/', ArticleLikeView.as_view(), name='article_like'),
    path(
        '<int:pk>/comment/',
        ArticleCommentView.as_view(),
        name='article_comment',
    ),
    path('ai/', include('ai_agent.urls')),
]
