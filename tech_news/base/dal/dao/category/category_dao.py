from base.models import Category


class CategoryDao:
    def __init__(self):
        super(CategoryDao, self).__init__()

    def get_category_by_status(self, status):
        articles = Category.objects.filter(status=status)
        return articles
