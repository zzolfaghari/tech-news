from django.urls import path

from .controller.articles.articles_controller import ArticleController, ArticleDetailView, ArticlePreview
from .controller.authors.authors_controller import AuthorController
from .controller.categories.categories_controller import CategoryController

app_name = 'base'
urlpatterns = [
    path('', ArticleController.as_view(), name='home'),
    path('page/<int:page>/', ArticleController.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('preview/<int:pk>/', ArticlePreview.as_view(), name='preview'),
    path('category/<slug:slug>/', CategoryController.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>/', CategoryController.as_view(), name='category'),
    path('author/<slug:username>/', AuthorController.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>/', AuthorController.as_view(), name='author')

]
