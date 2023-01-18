from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница со списком участников
def list_users(request):
    return HttpResponse('Список участников')

# Страница с информацией об одном участнике
def users_detail(request, pk):
    return HttpResponse(f'Участник {pk}') 