from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/',
      # Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      # Да, во view-классах так можно! Как их не полюбить. http://127.0.0.1:8000/auth/logout/
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
    path('login/',
      LoginView.as_view(template_name='users/login.html'),
      name='login'),

    path('reset/',
      PasswordResetView.as_view(template_name='users/password_reset_form.html'),
      name='reset_password'),

    path('password_reset/done/',
      PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
      name='done'),

    path('signup/', views.SignUp.as_view(), name='signup'),
] 