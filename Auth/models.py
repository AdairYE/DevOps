from django.db import models

# Create your models here.


# 父级菜单
class parentMenus(models.Model):
    name = models.CharField(
        verbose_name="父级菜单",
        max_length=43,
        null=True,
        blank=True,
        default="其他",
        help_text="添加子菜单时需要选择父级菜单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "父级菜单"
        verbose_name_plural = verbose_name
# 菜单
class Menus(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="菜单")
    parent = models.ForeignKey(
        parentMenus, verbose_name="父级菜单",
        null=True,
        blank=True,
        default=0,
        on_delete=models.CASCADE,
        help_text="添加子菜单时需要选择父级菜单")
    show = models.BooleanField(
        verbose_name="是否显示",
        default=False,
        help_text="菜单是否显示，默认添加不显示")
    url = models.CharField(
        max_length=300,
        verbose_name="菜单URL地址",
        null=True,
        blank=True,
        default="javascript:void(0)",
        help_text="为菜单设置url地址")
    priority = models.IntegerField(
        verbose_name="优先级",
        null=True,
        blank=True,
        default=-1,
        help_text="菜单显示的顺序，数字越大越靠前"
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name
