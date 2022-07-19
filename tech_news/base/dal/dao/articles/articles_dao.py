from base.models import Article


class ArticleDao:
    def __init__(self):
        super(ArticleDao, self).__init__()

    def get_all_articles(self):
        articles = Article.objects.all()
        return articles