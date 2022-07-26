from django.shortcuts import render
from django.views import View

from base.logic.category.category_logic import CategoryLogic


class CategoryController(View):
    def __init__(self):
        super().__init__()
        self.category_logic = CategoryLogic()

    def get(self, request, slug):
        context = {
            'category': self.category_logic.get_category_by_status_and_slug(status=True, slug=slug)}
        return render(request, template_name='base/category.html', context=context)


