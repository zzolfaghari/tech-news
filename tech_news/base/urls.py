from django.urls import path

from .controller.articles.articles_controller import ArticleController, ArticleDetailView

app_name = 'base'
urlpatterns = [
    path('', ArticleController.as_view(), name='home'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail')

]
