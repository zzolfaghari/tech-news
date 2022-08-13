from account.models import User


class UserDao:
    def __init__(self):
        super(UserDao, self).__init__()

    def get_user_by_id(self, pk):
        return User.objects.filter(pk=pk).first()
