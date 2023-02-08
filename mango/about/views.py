from django.views.generic.base import TemplateView

class AboutProjectPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'about/about.html' 

class TechProjectPage(TemplateView):
    template_name = 'about/tech.html' 