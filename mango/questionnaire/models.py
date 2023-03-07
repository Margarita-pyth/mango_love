from django.db import models
from django.contrib.auth import get_user_model
from .choices import AGE_CHOICES, COUNTRY_CHOICES

User = get_user_model()

class Questionnaire(models.Model):
    """Класс пользовательская анкета."""
    user = models.OneToOneField(User, 
                                on_delete = models.CASCADE,
                                primary_key = True)
    name = models.CharField("Имя",
                            max_length=200, 
                            help_text='Как к Вам обращаться')
    photo = models.ImageField(
        'Фотография',
        upload_to='photos/',
        blank=False)
    age = models.CharField(
        "Ваш возраст",
        choices = AGE_CHOICES,
        default = ' ',
        max_length=20,
        help_text='Сколько вам лет')
    city = models.CharField(
        "Ваш город",
        choices = COUNTRY_CHOICES,
        default = ' ',
        max_length=30,
        help_text='Добавьте город проживания')
    text = models.TextField(
        "Ваша цель",
        help_text='Добавьте цель пребывания на сайте')
    contact = models.EmailField(
        "email",
        help_text="Добавьте адрес электронной почты")
    pub_date = models.DateTimeField(
        "Дата регистрации",
        auto_now_add=True)

    class Meta:
      verbose_name_plural = "Анкеты"

    
    def __str__(self) -> str:
        return self.name
