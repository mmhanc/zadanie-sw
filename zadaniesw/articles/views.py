# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    """
    List of Article objects.
    """
    model = Article
    paginate_by = 5


class ArticleDetailView(DetailView):
    """
    Article object details.
    """
    model = Article


article_list = ArticleListView.as_view()
article_detail = ArticleDetailView.as_view()
