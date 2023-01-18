from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # Главная страница
    path('list/', views.list_users, name='list_users'), # Список участников 
    path('detail/<int:pk>/', views.users_detail), # Один участник
] 