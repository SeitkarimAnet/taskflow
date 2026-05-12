from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm, ProfileUpdateForm
from .models import CustomUser


# регистрация нового пользователя
class RegisterView(CreateView):

    form_class = RegisterForm

    template_name = 'registration/register.html'

    success_url = reverse_lazy('login')


# редактирование профиля
class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = CustomUser

    form_class = ProfileUpdateForm

    template_name = 'accounts/profile_update.html'

    success_url = reverse_lazy('task-list')

    # пользователь редактирует только свой профиль
    def get_object(self):

        return self.request.user


# выход из аккаунта
def logout_view(request):

    logout(request)

    return redirect('/')