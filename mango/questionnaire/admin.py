from django.contrib import admin
from .models import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'photo', 'age',
                    'floor', 'city', 'text', 'pub_date',)
    search_fields = ('name', 'age',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Questionnaire, QuestionnaireAdmin)
