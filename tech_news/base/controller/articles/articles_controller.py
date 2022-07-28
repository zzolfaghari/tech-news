from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from base.logic.articles.article_logic import ArticleLogic


class ArticleController(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request, page=1):
        article = self.article_logic.get_all_articles()
        paginator = Paginator(article, 6)
        paginated_articles = paginator.get_page(page)
        context = {
            'articles': paginated_articles}
        return render(request, template_name='base/index.html', context=context)


class ArticleDetailView(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request, slug):
        article = self.article_logic.get_article_by_slug(slug)
        return render(request, template_name='base/post.html', context={'article': article})
