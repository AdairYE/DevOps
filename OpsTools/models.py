from django.db import models

# Create your models here.

# 数据库管理
class dbms(models.Model):
    name = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        verbose_name="数据库名称"
    )
    _env = (
        ("QA","QA"),
        ("UAT","UAT"),
        ("STAGE","STAGE"),
        ("PRO","PRO"),
    )
    env = models.CharField(
        max_length=16,
        null=True,
        verbose_name="所属环境",
        choices=_env
    )

    _dbType = (
        ("mysql","mysql"),
    )
    dbType = models.CharField(
        max_length=24,
        null=True,
        verbose_name="数据库类型",
        choices=_dbType
    )

    dbHost = models.CharField(
        max_length=128,
        null=True,
        verbose_name="数据库主机"
    )

    dbPort = models.CharField(
        max_length=16,
        null=True,
        verbose_name="数据库端口",
        default=3306
    )

    dbUser = models.CharField(
        max_length=24,
        null=True,
        verbose_name="数据库用户名"
    )
    dbPasswd = models.CharField(
        max_length=64,
        null=True,
        verbose_name="数据库密码"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "数据库管理"
        verbose_name_plural = verbose_name

class dbHouse(models.Model):
    dbID = models.ForeignKey(
        dbms,
        null=True,
        on_delete = models.SET_NULL,
        verbose_name="数据库ID"
    )

    name = models.CharField(
        max_length=64,
        null=True,
        verbose_name="数据仓库"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "数据仓库"
        verbose_name_plural = verbose_name