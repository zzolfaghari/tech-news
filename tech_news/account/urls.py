from django.contrib.auth import views
from django.urls import path

from account.controller.article_controller import ArticleList, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'account'
urlpatterns = [
    path("", ArticleList.as_view(), name="home"),
    path("article/create/", ArticleCreateView.as_view(), name="article-create"),
    path("article/update/<int:pk>", ArticleUpdateView.as_view(), name="article-update"),
    path("article/delete/<int:pk>", ArticleDeleteView.as_view(), name="article-delete"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]
