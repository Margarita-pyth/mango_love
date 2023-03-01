from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from .models import User, Like
from questionnaire.models import Questionnaire
from questionnaire.views import *
from django.shortcuts import redirect
from django.shortcuts import render


@login_required
def my_likes(request):
    """Отображаем лайки."""
    questionnaire_list = Questionnaire.objects.filter(
        user__liked__user=request.user).order_by(
        'user_id')
    paginator = Paginator(questionnaire_list, QUESTIONNAIRES)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'likes/add_like.html', context)


@login_required
def add_like(request, pk):
    """Ставим лайки."""
    questionnaire_user = get_object_or_404(User, pk=pk)
    if (questionnaire_user != request.user):
        Like.objects.get_or_create(
            user=request.user,
            questionnaire_user=questionnaire_user
        )
    return redirect('likes:my_likes')