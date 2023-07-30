from django.db import models

class UserInfo(models.Model):
    ''' 用户表 '''
    user = models.CharField(verbose_name="用户名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=64)

    role_choices = (
        ("admin", "管理员"),
        ("user", "用户"),
        ("manager", "经理"),

    )

    role = models.CharField(verbose_name="角色", max_length=16, choices=role_choices, default='user')

class Depart(models.Model):
    ''' 部门表 '''
    title = models.CharField(verbose_name="用户名", max_length=32)
    count = models.IntegerField(verbose_name="人数")


