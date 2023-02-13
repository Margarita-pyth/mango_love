from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на страницу логина.
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'