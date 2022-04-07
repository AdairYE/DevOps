from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 产品管理
class product(models.Model):
    """产品管理"""
    name = models.CharField(
        max_length=64,
        null=True,
        verbose_name="产品名称"
    )

    code =models.CharField(
        max_length=32,
        null=True,
        verbose_name="产品代码"
    )

    productOwner = models.ManyToManyField(
        User,
        verbose_name="产品负责人"
    )

    explain = models.TextField(
        max_length=25,
        verbose_name="产品说明"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name
