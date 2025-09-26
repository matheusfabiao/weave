from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    """Formulário de cadastro de usuário.

    Args:
        UserCreationForm (class): Classe de cadastro nativa do Django
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
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
