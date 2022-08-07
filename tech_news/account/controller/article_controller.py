from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from base.logic.articles.article_logic import ArticleLogic
from base.models import Article


class ArticleList(LoginRequiredMixin, ListView):
    queryset = ArticleLogic().get_all_articles()
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticleLogic().get_all_articles()
        else:
            return ArticleLogic().get_article_by_author(author=self.request.user)


class ArticleCreateView(CreateView):
    model = Article
    fields = ["author",
              "title",
              "slug",
              "description",
              "category",
              "thumbnail",
              "publish",
              "status"]
    template_name = "registration/article-create-update.html"
