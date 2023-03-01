from django.contrib import admin
from .models import Like

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'questionnaire_user',)
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
admin.site.register(Like, LikeAdmin)