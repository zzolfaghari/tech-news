from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class AuthorDao():
    def __init__(self):
        super(AuthorDao, self).__init__()

    def get_author_by_username(self, username):
        return get_object_or_404(User, username=username)