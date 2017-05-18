# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='guid',
            field=models.CharField(default='', max_length=150, unique=True, verbose_name='globally unique identifier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(blank=True, max_length=150, verbose_name='article link'),
        ),
    ]
