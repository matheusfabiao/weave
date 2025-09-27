from django import forms


class AIArticleForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='Título',
        widget=forms.TextInput({'class': 'form-control'}),
    )
    idea = forms.CharField(
        label='Ideia Central',
        widget=forms.Textarea({'class': 'form-control'}),
    )
    audience = forms.CharField(
        max_length=255,
        required=False,
        label='Público Alvo',
        widget=forms.TextInput({'class': 'form-control'}),
    )
    tone = forms.ChoiceField(
        choices=[
            ('formal', 'Formal'),
            ('casual', 'Casual'),
            ('inspirador', 'Inspirador'),
        ],
        initial='formal',
        label='Tom',
        widget=forms.Select({'class': 'form-control'}),
    )
    extra_notes = forms.CharField(
        required=False,
        label='Observações extras',
        widget=forms.Textarea({'class': 'form-control'}),
    )
