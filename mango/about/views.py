from django.views.generic.base import TemplateView


class AboutProjectPage(TemplateView):
    template_name = 'about/about.html'


class TechProjectPage(TemplateView):
    template_name = 'about/tech.html'
