from django.shortcuts import redirect, render
from django.views.generic import View

from articles.models import Article

from .forms import AIArticleForm
from .utils import generate_ai_prompt, generate_ai_response


class AIArticleCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = AIArticleForm(request.POST)
        if form.is_valid():
            instructions = form.cleaned_data
            prompt = generate_ai_prompt(
                title=instructions.get('title'),
                idea=instructions.get('idea'),
                audience=instructions.get('audience'),
                tone=instructions.get('tone'),
                extra_notes=instructions.get('extra_notes'),
            )
            content = generate_ai_response(prompt)
            Article.objects.create(
                author=request.user.profile,
                title=instructions.get('title'),
                content=content,
            )
            return redirect('article_list')

    @staticmethod
    def get(request, *args, **kwargs):
        form = AIArticleForm()
        context = {'form': form}
        return render(request, 'ai_article_create.html', context)
