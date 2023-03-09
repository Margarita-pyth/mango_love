from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

User = get_user_model()
 
class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )
 
    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Участник"))
 
    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk }
 
 
class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=_("Чат"), on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    message = models.TextField(_("Сообщение"))
    pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
    is_readed = models.BooleanField(_('Прочитано'), default=False)
 
    class Meta:
        ordering=['pub_date']
 
    def __str__(self):
        return self.message
