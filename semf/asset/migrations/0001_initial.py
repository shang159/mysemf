# Generated by Django 2.2.5 on 2019-09-09 03:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=50, null=True, unique=True, verbose_name='系统编号')),
                ('asset_name', models.CharField(max_length=100, verbose_name='资产名称')),
                ('asset_type', models.CharField(max_length=100, verbose_name='资产类型')),
                ('asset_key', models.CharField(max_length=50, unique=True, verbose_name='唯一标记')),
                ('asset_description', models.TextField(null=True, verbose_name='资产介绍')),
                ('asset_link', models.TextField(blank=True, null=True, verbose_name='生产线')),
                ('asset_score', models.IntegerField(default='0', verbose_name='重要性估值')),
                ('asset_starttime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('asset_updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='联系人邮箱')),
                ('asset_user', models.ManyToManyField(blank=True, related_name='asset_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
