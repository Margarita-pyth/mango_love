from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'users/index.html'
    title = 'Это Главная страница проекта'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    return render(request, template, context) 

# Страница со списком участников
def list_users(request):
    template = 'users/users_list.html'
    title = 'Тут будет список участников'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Вложенная страница',
    }
    return render(request, template, context)

# Страница с информацией об одном участнике
def users_detail(request, pk):
    return HttpResponse(f'Участник {pk}') 