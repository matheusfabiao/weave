from django.urls import path

from .views import AIArticleCreateView

urlpatterns = [
    path('create/', AIArticleCreateView.as_view(), name='article_create_ai'),
]
