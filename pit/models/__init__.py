from datetime import datetime
from hashlib import sha256

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

from pit.extensions import db


class Role(db.Model):

    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    users = relationship('User', backref='role')


class User(db.Model):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(62), nullable=False)
    nickname = Column(String(30), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    pits = relationship('Pit', backref='author')
    replys = relationship('Reply', backref='author')
    role_id = Column(Integer, ForeignKey('role.id'))

    def set_password(self, raw_pwd):
        self.password = User.hash_password(raw_pwd)

    @staticmethod
    def hash_password(raw_pwd):
        salt = db.app.settings.get('salt', 'SALT')
        hash_str = "%s|%s|%s" % (salt, raw_pwd, salt)
        return sha256(hash_str).hexdigest()


class Topic(db.Model):

    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    pits = relationship('Pit', backref='topic')


class Pit(db.Model):

    __tablename__ = 'pit'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    description = Column(Text)
    replys = relationship('Reply', backref='pit')
    created = Column(DateTime, default=datetime.utcnow)


class Reply(db.Model):

    __tablename__ = 'reply'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    pit_id = Column(Integer, ForeignKey('pit.id'))
    reply = Column(Text)
    created = Column(DateTime, default=datetime.utcnow)
