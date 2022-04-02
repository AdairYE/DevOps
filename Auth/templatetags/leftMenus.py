from django import template

from django.utils.safestring import mark_safe

from Auth.models import parentMenus, Menus

register = template.Library()


@register.inclusion_tag("menu.html")
def Menus():
    leftMenu = {}
    parent = parentMenus.objects.all()
    for p in parent:
        obj = parentMenus.objects.get(name=p)
        leftMenu[p.name] = []
        for menus in obj.menus_set.all():
            leftMenu[p.name].append(
                {
                    "name": menus.name,
                    "url": menus.url,
                    "isShow": menus.show,
                    "priority": menus.priority
                }
            )
    return {
        "leftMenu": leftMenu
    }
