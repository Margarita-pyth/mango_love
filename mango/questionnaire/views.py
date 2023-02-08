from django.http import HttpResponse
from django.shortcuts import render
from .models import Questionnaire, User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

POSTS_PER_PAGE = 10


# Главная страница
def index(request):
    questionnaire_list = Questionnaire.objects.all()
    paginator = Paginator(questionnaire_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'questionnaire/index.html', context)

# ???????
def profile(request, username):
    questionnaire_user = get_object_or_404(User, username=username)
    questionnaire_list = Questionnaire.objects.filter(user=questionnaire_user).all()

    template = 'questionnaire/profile.html'
    context = {
        'questionnaire_user': questionnaire_user,
    }
    return render(request, template, context)


def detail(request, questionnaire_id):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'questionnaire/detail.html', context)
