from base.dal.dao.category.category_dao import CategoryDao


class CategoryLogic:
    def __init__(self):
        super().__init__()
        self.category_dao = CategoryDao()

    def get_category_by_status(self, status):
        return self.category_dao.get_category_by_status(status)
