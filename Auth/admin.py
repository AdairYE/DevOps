from django.contrib import admin

# Register your models here.
from Auth.models import Menus,parentMenus


class MenusAdmin(admin.ModelAdmin):
    list_display = ["id","name","parent","url","priority"]
admin.site.register(Menus,MenusAdmin)

class parentMenusAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
admin.site.register(parentMenus,parentMenusAdmin)