from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from base.logic.category.category_logic import CategoryLogic


class CategoryController(ListView):
    paginate_by = 5
    template_name = 'base/category_list.html'

    def __init__(self):
        super().__init__()
        self.category_logic = CategoryLogic()

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = self.category_logic.get_category_by_status_and_slug(status=True, slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context



