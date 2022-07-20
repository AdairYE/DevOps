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

    databaseType = (
        ("mysql","mysql"),
    )
    dbType = models.CharField(
        max_length=24,
        null=True,
        verbose_name="数据库类型",
        choices=databaseType
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

class dbHouse(models.Model):
    name = models.ForeignKey(
        dbms,
        max_length=64,
        null=True,
        on_delete = models.SET_NULL,
        verbose_name="数据仓库"
    )