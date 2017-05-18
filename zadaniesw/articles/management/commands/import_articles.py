# -*- coding: utf-8 -*-
import urllib.request

from django.core.management.base import BaseCommand

from xml.dom import minidom
from dateutil import parser

from articles.models import Article


def create_articles(content):
    """
    
    """
    # Open XML document using minidom parser
    DOMTree = minidom.parseString(content)

    # pobieramy elementy struktury dokumentu XML
    cNodes = DOMTree.childNodes

    # W tuplach przyporządkowuję nazwom pól modelu nazwy tagów z xmla, którego
    # otrzymuję w pobranej ze strony treści
    tags = [('title', 'title'),
            ('link', 'link'),
            ('content', 'description'),
            ('date_published', 'pubDate')]

    for i in cNodes[0].getElementsByTagName('item'):
        # sprawdzam, czy artykuł istnieje po tagu guid, który jest unikalny
        guid = i.getElementsByTagName('guid')[0].childNodes[0].toxml()
        article, created = Article.objects.get_or_create(guid=guid)
        # w przypadku nowo utworzonych obiektów uzupełniam ich dane
        if created:
            for tag in tags:
                attr_name, tag_name = tag
                content = i.getElementsByTagName(tag_name)[0].childNodes[0]\
                    .toxml()
                if tag_name == 'pubDate':
                    content = parser.parse(content)
                setattr(article, attr_name, content)
            article.save()


class Command(BaseCommand):
    help = 'Imports and saves news from the djangoproject.com'

    def handle(self, *args, **options):
        url = 'https://www.djangoproject.com/rss/weblog/'
        # pobieram zawartość strony
        response = urllib.request.urlopen(url)
        content = response.read()
        create_articles(content)
