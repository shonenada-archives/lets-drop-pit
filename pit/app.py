from tornado.web import Application

from pit.extensions import db, rbac
from pit.settings import app_settings as configuration
from pit.routes import url_list
from pit.utils import ui_methods
from pit.permission import permission


def create_app(config={}):

    configuration.update(config)

    application = Application(url_list, ui_methods=ui_methods, **configuration)

    db.init_app(application)

    rbac.init_app(application)
    rbac.load_permission(permission)

    return application
