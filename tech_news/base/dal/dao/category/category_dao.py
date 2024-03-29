from base.models import Category


class CategoryDao:
    def __init__(self):
        super().__init__()

    def get_category_by_status_and_slug(self, status, slug):
        categories = Category.objects.filter(status=status, slug=slug).first()
        return categories
