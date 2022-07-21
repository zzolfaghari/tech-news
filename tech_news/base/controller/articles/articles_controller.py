from django.shortcuts import render
from django.views import View
from base.logic.articles.article_logic import ArticleLogic


class ArticleController(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request):
        articles = self.article_logic.get_all_articles()
        return render(request, template_name='base/index.html', context={'articles': articles})


class ArticleDetailView(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request, slug):
        article = self.article_logic.get_article_by_slug(slug)
        return render(request, template_name='base/post.html', context={'article': article})
