from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Create your models here.

# 产品管理
class product(models.Model):
    """产品管理"""
    name = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        verbose_name="产品名称"
    )

    code = models.CharField(
        max_length=32,
        null=True,
        unique=True,
        verbose_name="产品代码"
    )

    productOwner = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="产品负责人",
        related_name="product_author_user"
    )
    participator = models.ManyToManyField(
        User,
        blank=True,
        verbose_name="产品参与者",
        related_name="product_participator_user"
    )

    explain = models.TextField(
        max_length=128,
        verbose_name="产品说明"
    )
    star = models.ManyToManyField(User,
                                  verbose_name="标星产品")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name


# 项目管理
class project(models.Model):
    '''项目管理'''
    name = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        verbose_name="项目名称"
    )
    code = models.CharField(
        max_length=32,
        null=True,
        unique=True,
        verbose_name="项目编码"
    )
    product = models.ForeignKey(
        product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="关联产品"
    )
    projectType = (
        ("敏捷型", "Agile"),
        ("瀑布式", "Waterfall"),
        ("自定义", "Custom"),
    )
    proType = models.CharField(
        max_length=18,
        null=True,
        verbose_name="项目类型",
        choices=projectType
    )
    startDate = models.DateTimeField(
        default=timezone.now,
        verbose_name="项目开始时间"
    )
    endDate = models.DateTimeField(
        default=timezone.now,
        verbose_name="项目结束时间"
    )
    explain = models.TextField(
        max_length=128,
        verbose_name="项目描述"
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="项目负责人",
        related_name="project_author_user"
    )
    participator = models.ManyToManyField(
        User,
        blank=True,
        verbose_name="项目参与者",
        related_name="project_participator_user"
    )
    star = models.ManyToManyField(User,
                                       verbose_name="标星项目"
                                       )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = verbose_name

# 文件管理
class wiki(models.Model):
    name = models.CharField(max_length=32,verbose_name="文件与文件夹名")
    _fileType = (
        ("d","文件夹"),
        ("f","文件")
    )
    fileType = models.CharField(max_length=16,verbose_name="文件类型",
                                choices=_fileType)
    contactType = models.CharField(max_length=16,verbose_name="关联类型")  #