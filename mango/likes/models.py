from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(
        User,
        related_name='current_user',
        on_delete=models.CASCADE
    )
    questionnaire_user = models.ForeignKey(
        User,
        related_name='liked',
        on_delete=models.CASCADE
    )
    UniqueConstraint(fields=['user', 'questionnaire_user'],
                     name='unique_likes')

    class Meta:
        verbose_name_plural = "Лайки"
