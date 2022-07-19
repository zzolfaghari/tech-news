from django.shortcuts import render
from django.views import View
from base.logic.articles.article_logic import ArticleLogic


class ArticleController(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request):
        articles = self.article_logic.get_all_articles()
        return render(request, template_name='base/home.html', context=articles)
