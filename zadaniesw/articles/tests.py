# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory

from articles.views import ArticleListView, ArticleDetailView


class ArticleListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """
        Tests if status code and template name are correct.
        """
        request = self.factory.get('/test-path')
        view = ArticleListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'articles/article_list.html')
