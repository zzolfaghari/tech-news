from account.dal.dao.user_dao import UserDao


class UserLogic:
    def __init__(self):
        super().__init__()
        self.user_dao = UserDao()

    def get_user_by_id(self, pk):
        return self.user_dao.get_user_by_id(pk=pk)
