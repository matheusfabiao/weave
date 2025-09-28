from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, View

from .forms import LoginForm, ProfileForm, RegisterForm, UserForm
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
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy(
            'profile_detail', kwargs={'pk': self.request.user.pk}
        )


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


class ProfileUpdateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
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
            return redirect('profile_detail', pk=request.user.pk)

        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile_update.html', context)

    @staticmethod
    def get(request, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(
            instance=request.user.profile,
        )
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile_update.html', context)
