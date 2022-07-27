from django.shortcuts import get_object_or_404

from base.enums import StatusType
from base.models import Article


class ArticleDao:
    def __init__(self):
        super(ArticleDao, self).__init__()

    def get_all_articles(self):
        articles = Article.objects.all()
        return articles

    def get_articles_by_slug(self, slug):
        return get_object_or_404(Article.objects.published(), slug=slug)
