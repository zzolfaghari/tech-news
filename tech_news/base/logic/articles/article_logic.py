from base.dal.dao.articles.articles_dao import ArticleDao


class ArticleLogic:
    def __init__(self):
        super().__init__()
        self.article_dao = ArticleDao()

    def get_all_articles(self):
        return self.article_dao.get_all_articles()

    def get_article_by_slug(self, slug):
        return self.article_dao.get_articles_by_slug(slug)