from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Database(object):
    
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.app.settings.setdefault('sqlalchemy_uri', 'sqlite:///:memory:')
        self.engine = create_engine(self.app.settings.get('sqlalchemy_uri'))
        self.base = declarative_base()
