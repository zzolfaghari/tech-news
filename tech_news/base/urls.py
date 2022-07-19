from django.urls import path

from .controller.articles.articles_controller import ArticleController


urlpatterns = [
    path('', ArticleController.as_view(), name='home')

]