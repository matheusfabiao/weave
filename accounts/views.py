from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, View

from .forms import ProfileForm, RegisterForm, UserForm
from .models import Profile


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Conta criada com sucesso! Faça login.')
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('post_list')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'


class ProfileUpdateView(View):
    @staticmethod
    def post(request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile,
            files=request.FILES,
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile.html', context)

    @staticmethod
    def get(request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(
            instance=request.user.profile,
            files=request.FILES,
        )
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile.html', context)
