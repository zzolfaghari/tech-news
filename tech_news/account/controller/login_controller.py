from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
