from django.contrib.auth import views
from django.urls import path

from account.controller.article_controller import ArticleList, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from account.controller.login_controller import Login, PasswordChange
from account.controller.profile_controller import ProfileView

app_name = 'account'
urlpatterns = [
    path("", ArticleList.as_view(), name="home"),
    path("article/create/", ArticleCreateView.as_view(), name="article-create"),
    path("article/update/<int:pk>", ArticleUpdateView.as_view(), name="article-update"),
    path("article/delete/<int:pk>", ArticleDeleteView.as_view(), name="article-delete"),
    path("profile/", ProfileView.as_view(), name="profile"),

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
