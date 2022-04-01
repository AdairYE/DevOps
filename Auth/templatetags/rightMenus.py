from django import template

from django.utils.safestring import mark_safe

from Auth.models import parentMenus, Menus

register = template.Library()

@register.simple_tag
def rightMenu():
    rightMenu = {}
    parent = parentMenus.objects.all()
    for p in parent:
        obj = parentMenus.objects.get(name=p)
        rightMenu[p.name] = []
        for menus in obj.menus_set.all():
            rightMenu[p.name].append(
                {
                    "name": menus.name,
                    "url": menus.url,
                    "isShow": menus.show,
                    "priority": menus.priority
                }
            )
    return mark_safe(rightMenu)