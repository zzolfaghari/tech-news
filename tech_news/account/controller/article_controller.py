from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from base.logic.articles.article_logic import ArticleLogic


class ArticleList(LoginRequiredMixin, ListView):
    queryset = ArticleLogic().get_all_articles()
    template_name = "registration/home.html"

