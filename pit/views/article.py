from tornado.web import RequestHandler

from pit.models import Pit


class ArticleView(RequestHandler):

    def get(self):
        print Pit.query.first()
        return self.render('article/pits.html')
