from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from account.mixins import FieldsMixin, FormValidMixin, SuperuserAccessMixin, AuthorAccessMixin
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


class ArticleCreateView(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdateView(AuthorAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleDeleteView(SuperuserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = "registration/article_confirm_delete.html"
