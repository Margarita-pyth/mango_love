from django import template
# В template.Library зарегистрированы все встроенные теги и фильтры шаблонов;
# добавляем к ним и наш фильтр.
register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

# синтаксис @register... , под который описана функция addclass() - 
# это применение "декораторов", функций, меняющих поведение функций


@register.simple_tag
def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None