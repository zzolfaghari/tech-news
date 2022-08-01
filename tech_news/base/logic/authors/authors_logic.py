from base.dal.dao.authors.authors_dao import AuthorDao


class AuthorLogic:
    def __init__(self):
        super().__init__()
        self.author_dao = AuthorDao()

    def get_author_by_username(self, username):
        return self.author_dao.get_author_by_username(username)


