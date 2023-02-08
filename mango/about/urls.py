from . import views
from django.urls import path

app_name = 'about'

urlpatterns = [
    path('project/', views.AboutProjectPage.as_view(), name='project'),
    path('tech/', views.TechProjectPage.as_view(), name='tech'),
] 