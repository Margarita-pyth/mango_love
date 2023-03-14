from .models import Questionnaire
from django import forms


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ('name', 'photo', 'age', 'city', 'text')
