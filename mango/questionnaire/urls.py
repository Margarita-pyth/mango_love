from django.urls import path
from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('profile/<str:username>/', views.profile, name='profile'),
#   path('detail/<int:pk>/', views.detail, name='detail'),
] 