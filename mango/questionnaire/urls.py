from django.urls import path
from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('questionnaire/create', views.questionnaire_create, name='questionnaire_create'),
] 