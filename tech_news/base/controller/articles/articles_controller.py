from django.shortcuts import render
from django.views import View

from base.dal.dao.category.category_dao import CategoryDao
from base.logic.articles.article_logic import ArticleLogic
from base.logic.category.category_logic import CategoryLogic


class ArticleController(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()
        self.category_logic = CategoryLogic()

    def get(self, request):
        context = {
            'articles': self.article_logic.get_all_articles(),
            'category': self.category_logic.get_category_by_status(status=True)}
        return render(request, template_name='base/index.html', context=context)


class ArticleDetailView(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request, slug):
        article = self.article_logic.get_article_by_slug(slug)
        return render(request, template_name='base/post.html', context={'article': article})
