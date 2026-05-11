from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def logout_view(request):
    logout(request)
    return redirect('/')