from tornado.web import Application, URLSpec

from pit.extensions import db
from pit.settings import app_settings as configuration
from pit.views.master import IndexHandler


def create_app(config={}):

    configuration.update(config)

    url_list = [
        URLSpec(r'/', IndexHandler, name='index'),
    ]

    application = Application(url_list, **configuration)

    db.init_app(application)

    return application
