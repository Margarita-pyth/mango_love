from django.urls import path
from . import views
from .views import SearchResultsView

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('questionnaire/create', views.questionnaire_create, name='questionnaire_create'),
    path('detail/<int:pk>/edit', views.questionnaire_edit, name='questionnaire_edit'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
] 