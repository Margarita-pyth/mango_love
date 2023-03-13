from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/',
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

    path('reset/<uidb64>/<token>/',
      PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
      name='confirm'),

    path('reset/done/',
      PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
      name='complete_reset'),

    path('signup/', views.SignUp.as_view(), name='signup'),
] 