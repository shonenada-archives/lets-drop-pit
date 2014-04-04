from tornado.web import Application

from pit.extensions import db
from pit.settings import app_settings as configuration
from pit.routes import url_list


def create_app(config={}):

    configuration.update(config)

    application = Application(url_list, **configuration)

    db.init_app(application)

    return application
