from .models import Questionnaire, User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from likes .models import Like
from django.views.generic import ListView

QUESTIONNAIRES = 9


class SearchResultsView(ListView):
    """Поисковая форма."""
    model = Questionnaire
    template_name = 'questionnaire/search_results.html'

    def get_queryset(self):
        """Фильтруем данные по запросу."""
        query = self.request.GET.get('q')
        object_list = Questionnaire.objects.filter(
            city__icontains=query)
        return object_list


def index(request):
    """Главная страница."""
    questionnaire_list = Questionnaire.objects.get_queryset().order_by(
        'user_id')
    paginator = Paginator(questionnaire_list, QUESTIONNAIRES)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    questionnaire_user = request.user
    context = {
        'questionnaire_user': questionnaire_user,
        'page_obj': page_obj,
    }
    return render(request, 'questionnaire/index.html', context)


def detail(request, pk):
    """Анкета одного пользователя."""
    questionnaire = get_object_or_404(Questionnaire, user_id=pk)
    questionnaire_user = get_object_or_404(User, pk=pk)
    liked = False
    if Like.objects.filter(
            user=request.user, questionnaire_user=questionnaire_user).exists():
        liked = True
    context = {
        'questionnaire': questionnaire,
        'questionnaire_user': questionnaire_user,
        'liked': liked,

    }
    return render(request, 'questionnaire/detail.html', context)


@login_required
def questionnaire_create(request):
    """Создание анкеты пользователем."""
    form = QuestionnaireForm(request.POST or None,
                             files=request.FILES or None)
    if form.is_valid():
        questionnaire = form.save(commit=False)
        questionnaire.user = request.user
        questionnaire.save()
        return redirect('questionnaire:detail', questionnaire.user.id)
    return render(request,
                  'questionnaire/questionnaire_create.html',
                  {'form': form}
                  )


@login_required
def questionnaire_edit(request, pk):
    """Редактирование своей анкеты."""
    questionnaire = get_object_or_404(Questionnaire, pk=pk)
    if questionnaire.user != request.user:
        return redirect('questionnaire:detail', user_id=pk)

    form = QuestionnaireForm(
        request.POST or None,
        files=request.FILES or None,
        instance=questionnaire
    )
    if form.is_valid():
        form.save()
        form.user = request.user
        return redirect('questionnaire:detail', form.user.id)
    context = {
        'questionnaire': questionnaire,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'questionnaire/questionnaire_create.html', context)
