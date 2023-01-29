from django.urls import path
from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('list/', views.list_users, name='list_questionnaires'), # Список участников 
    path('detail/<int:pk>/', views.users_detail), # Один участник
] 