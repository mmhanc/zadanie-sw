# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    """
    Article model.
    """
    guid = models.CharField('globally unique identifier', unique=True,
                            max_length=150)
    title = models.CharField('title', max_length=150, blank=True)
    content = models.TextField('content', blank=True)
    date_published = models.DateTimeField('date published', null=True)
    link = models.CharField('article link', max_length=150, blank=True)

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'article'
        verbose_name_plural = 'articles'
