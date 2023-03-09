from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
path('dialogs/', views.DialogsView.as_view(), name='dialogs'),
path('dialogs/create/(?P<user_id>\d+)/$', views.CreateDialogView.as_view(), name='create_dialog'),
path('dialogs/(?P<chat_id>\d+)/$', views.MessagesView.as_view(), name='messages'),
]