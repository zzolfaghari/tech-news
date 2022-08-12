from django.urls import reverse_lazy
from django.views.generic import UpdateView

from account.logic.user_logic import UserLogic
from account.models import User


class ProfileView(UpdateView):
    model = User
    template_name = "registration/profile.html"
    fields = ["username", "email", "first_name", "last_name", "special_user", "is_author"]
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):
        return UserLogic().get_user_by_id(pk=self.request.user.pk)
