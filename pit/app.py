from tornado.web import RequestHandler, Application, URLSpec

from pit.settings import app_settings as configuration


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


def create_app(config={}):

    configuration.update(config)

    url_list = [
        URLSpec(r'/', MainHandler, name='index'),
    ]

    application = Application(url_list, **configuration)

    return application
