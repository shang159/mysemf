# Generated by Django 2.2.5 on 2019-09-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='asset_description',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_score',
        ),
    ]
