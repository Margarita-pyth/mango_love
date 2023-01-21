from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('list/', views.list_users, name='list_users'), # Список участников 
    path('detail/<int:pk>/', views.users_detail), # Один участник
] 