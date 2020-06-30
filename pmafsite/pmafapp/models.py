from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 模型一旦发生改变，要重新迁移
class UserProfile(AbstractUser):
    unickname = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    ubirthday = models.DateField(auto_now_add=True, verbose_name='生日', null=True)
    uaddress = models.CharField(max_length=200, verbose_name='地址')
