from tornado.web import RequestHandler


class IndexView(RequestHandler):

    def get(self):
        
        return self.render('index.html')
