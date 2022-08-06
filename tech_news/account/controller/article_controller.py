from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from base.logic.articles.article_logic import ArticleLogic


class ArticleList(LoginRequiredMixin, ListView):
    queryset = ArticleLogic().get_all_articles()
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticleLogic().get_all_articles()
        else:
            return ArticleLogic().get_article_by_author(author=self.request.user)

