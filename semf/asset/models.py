from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
    asset_id = models.CharField('系统编号', max_length=50, unique=True, null=True,blank=True)
    asset_name = models.CharField('资产名称', max_length=100)
    asset_type = models.CharField('资产类型', max_length=100)
    asset_key = models.CharField('唯一标记', max_length=50, unique=True)
    asset_link = models.CharField('生产线', max_length=50,null=True,blank=True)
    asset_starttime = models.DateTimeField('添加时间', auto_now_add=True)
    asset_updatetime = models.DateTimeField('更新时间', auto_now=True)
    user_email = models.EmailField('联系人邮箱', null=True, blank=True)
    asset_user = models.ManyToManyField(User, related_name='asset_to_user', blank=True)


    def __str__(self):
        return self.asset_key
