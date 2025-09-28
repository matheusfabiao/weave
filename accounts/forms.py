from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    """Formulário de cadastro de usuário.

    Args:
        UserCreationForm (class): Classe de cadastro nativa do Django
    """

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )
        widgets = {
            'first_name': forms.TextInput({'class': 'form-control'}),
            'last_name': forms.TextInput({'class': 'form-control'}),
            'username': forms.TextInput({'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu usuário',
            }
        ),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )


class UserForm(forms.ModelForm):
    """Formulário das informações referentes ao
    usuário padrão do django.

    Args:
        ModelForm (class):
            Classe para criar um formulário a partir dos modelos
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {'username': None}
        widgets = {
            'username': forms.TextInput({'class': 'form-control'}),
            'first_name': forms.TextInput({'class': 'form-control'}),
            'last_name': forms.TextInput({'class': 'form-control'}),
            'email': forms.TextInput({'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    """Formulário das informações referentes ao perfil
    do usuário, criado a partir da instância do usuário padrão.

    Args:
        ModelForm (class):
            Classe para criar um formulário a partir dos modelos
    """

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'phone', 'birth_date', 'picture')
        widgets = {
            'bio': forms.Textarea({'class': 'form-control'}),
            'location': forms.Select({'class': 'form-control'}),
            'phone': forms.TextInput({'class': 'form-control'}),
            'birth_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d',
            ),
            'picture': forms.ClearableFileInput({'class': 'form-control'}),
        }
