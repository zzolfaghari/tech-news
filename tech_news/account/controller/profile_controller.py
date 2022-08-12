from django.views.generic import UpdateView

from account.models import User


class ProfileView(UpdateView):
    model = User
    template_name = "registration/profile.html"
    fields = ["username", "email", "first_name", "last_name", "special_user", "is_author"]