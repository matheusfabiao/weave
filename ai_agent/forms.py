from django import forms


class AIArticleForm(forms.Form):
    title = forms.CharField(max_length=255, label='Título')
    idea = forms.CharField(widget=forms.Textarea, label='Ideia Central')
    audience = forms.CharField(
        max_length=255, required=False, label='Público Alvo'
    )
    tone = forms.ChoiceField(
        choices=[
            ('formal', 'Formal'),
            ('casual', 'Casual'),
            ('inspirador', 'Inspirador'),
        ],
        initial='formal',
        label='Tom',
    )
    extra_notes = forms.CharField(
        widget=forms.Textarea, required=False, label='Observações extras'
    )
