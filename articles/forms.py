from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'resume', 'content', 'tags']
        labels = {
            'title': 'Título',
            'resume': 'Resumo',
            'content': 'Conteúdo',
            'tags': 'Palavras-Chave',
        }
        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'resume': forms.Textarea({'class': 'form-control'}),
            'content': forms.Textarea({'class': 'form-control'}),
            'tags': forms.SelectMultiple({'class': 'form-control'}),
        }


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea({'class': 'form-control'}),
        label='Comentário',
    )
