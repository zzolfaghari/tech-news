from django.shortcuts import get_object_or_404

from base.models import Article


class ArticleDao:
    def __init__(self):
        super(ArticleDao, self).__init__()

    def get_all_published_articles(self):
        return Article.objects.published()

    def get_articles_by_slug(self, slug):
        return get_object_or_404(Article.objects.published(), slug=slug)

    def get_all_articles(self):
        return Article.objects.all()

    def get_article_by_author(self, author):
        return Article.objects.filter(author=author)


