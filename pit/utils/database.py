from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query, class_mapper
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.ext.declarative import declarative_base


class _QueryProperty(object):

    def __init__(self, sa):
        self.sa = sa

    def __get__(self, obj, type):
        try:
            mapper = class_mapper(type)
            if mapper:
                return type.query_class(mapper, session=self.sa.session)
        except UnmappedClassError:
            return None


class BaseQuery(Query):
    pass


class BaseModel(object):
    query_class = BaseQuery
    query = None


class Database(object):
    
    def __init__(self, app=None):
        if app:
            self.init_app(app)
        self.Model = declarative_base(cls=BaseModel, name='Model')
        self.Model.query = _QueryProperty(self)

    def init_app(self, app):
        self.app = app
        self.app.settings.setdefault('sqlalchemy_uri', 'sqlite:///:memory:')
        self.engine = create_engine(self.app.settings.get('sqlalchemy_uri'))
        self.session = sessionmaker(bind=self.engine)()

    def create_all(self):
        self.Model.metadata.create_all(self.engine)

    def drop_all(self):
        self.Model.metadata.drop_all(self.engine)
