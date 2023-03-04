from django.urls import path
from . import views

app_name = 'likes'

urlpatterns = [
    path('detail/<int:pk>/add_like/', views.add_like, name='add_like'),
    path('detail/<int:pk>/dislike/', views.dislike, name='dislike'),
    path('my_likes/', views.my_likes, name='my_likes'),
] 