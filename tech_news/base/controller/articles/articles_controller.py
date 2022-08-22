from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from account.mixins import AuthorAccessMixin
from base.logic.articles.article_logic import ArticleLogic


class ArticleController(View):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get(self, request, page=1):
        article = self.article_logic.get_all_published_articles()
        paginator = Paginator(article, 2)
        paginated_articles = paginator.get_page(page)
        context = {
            'article_list': paginated_articles}
        return render(request, template_name='base/article_list.html', context=context)


class ArticleDetailView(DetailView):
    template_name = 'base/article_detail.html'

    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get_object(self, queryset=None):
        article = self.article_logic.get_article_by_slug(self.kwargs.get('slug'))
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return ip_address


class ArticlePreview(AuthorAccessMixin, DetailView):
    def __init__(self):
        super().__init__()
        self.article_logic = ArticleLogic()

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return self.article_logic.get_article_by_id(pk)
