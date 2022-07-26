from base.dal.dao.category.category_dao import CategoryDao


class CategoryLogic:
    def __init__(self):
        super().__init__()
        self.category_dao = CategoryDao()

    def get_category_by_status_and_slug(self, status, slug):
        return self.category_dao.get_category_by_status_and_slug(status, slug)
