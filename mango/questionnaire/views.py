from django.shortcuts import render
from .models import Questionnaire
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

QUESTIONNAIRES = 20


# Главная страница
def index(request):
    questionnaire_list = Questionnaire.objects.get_queryset().order_by('user_id')
    paginator = Paginator(questionnaire_list, QUESTIONNAIRES)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'questionnaire/index.html', context)


def detail(request, pk):
    users = Questionnaire.objects.all()
    questionnaire = get_object_or_404(Questionnaire, user_id=pk)
    context = {
        'questionnaire': questionnaire,
    }
    return render(request, 'questionnaire/detail.html', context)


@login_required
def questionnaire_create(request):
    form = QuestionnaireForm(request.POST or None,
                    files=request.FILES or None
                    )
    if form.is_valid():
        questionnaire = form.save(commit=False)
        questionnaire.user = request.user
        questionnaire.save()
        return redirect('questionnaire:detail', questionnaire.user.id)
    return render(request, 'questionnaire/questionnaire_create.html', {'form': form})
