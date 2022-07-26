from django.urls import path

from .controller.articles.articles_controller import ArticleController, ArticleDetailView
from .controller.categories.categories_controller import CategoryController

app_name = 'base'
urlpatterns = [
    path('', ArticleController.as_view(), name='home'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
path('category/<slug:slug>/', CategoryController.as_view(), name='category')

]
