from django.urls import reverse_lazy
from django.views.generic import UpdateView

from account.forms import ProfileForm
from account.logic.user_logic import UserLogic
from account.models import User


class ProfileView(UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):
        return UserLogic().get_user_by_id(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update(
            {'user': self.request.user}
        )
        return kwargs
