from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

from pit.extensions import db


class User(db.base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(62), nullable=False)
    nickname = Column(String(30))
    email = Column(String(50))
    created = Column(DateTime, default=datetime.utcnow)
    pits = relationship('Pit', backref='author')
    replys = relationship('Pit', backref='author')


class Topic(db.base):
    
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    pits = relationship('Pit', backref='topic')


class Pit(db.base):

    __tablename__ = 'pit'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    description = Column(Text)
    replys = relationship('Reply', backref='pit')
    created = Column(DateTime, default=datetime.utcnow)


class Reply(db.base):

    __tablename__ = 'reply'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    pit_id = Column(Integer, ForeignKey('pit.id'))
    reply = Column(Text)
    created = Column(DateTime, default=datetime.utcnow)
