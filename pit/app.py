from tornado.web import RequestHandler, Application

from pit.settings import app_settings as configuration


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


def create_app(config={}):

    configuration.update(config)

    application = Application([
        (r"/", MainHandler),
    ], **configuration)

    return application
