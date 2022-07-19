from base.dal.dao.articles.articles_dao import ArticleDao


class ArticleLogic:
    def __init__(self):
        super().__init__()
        self.article_dao = ArticleDao()

    def get_all_articles(self):
        return self.article_dao.get_all_articles()