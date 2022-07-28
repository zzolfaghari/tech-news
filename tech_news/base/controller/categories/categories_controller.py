from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from base.logic.category.category_logic import CategoryLogic


class CategoryController(View):
    def __init__(self):
        super().__init__()
        self.category_logic = CategoryLogic()

    def get(self, request, slug, page=1):
        category = self.category_logic.get_category_by_status_and_slug(status=True, slug=slug)
        articles_list = category.articles.published()
        paginator = Paginator(articles_list, 1)
        paginated_articles = paginator.get_page(page)
        context = {
            'category': category,
            'articles': paginated_articles
        }
        return render(request, template_name='base/category.html', context=context)


