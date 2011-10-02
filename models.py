import web

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

def setup():
    Post.__table__
    #TODO Add in a check to see if the table exists
    Base.metadata.create_all(db)

#Table Objects go here
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key = True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime, server_default=func.current_timestamp())

    def __init__(self, title, content):
        self.title = title
        self.content = content

#This is another post model based on a file backend.
class BlogPost:
    def __init__(self, title, content, date, path):
        self.title = title
        self.content = content
        self.date = date
        self.path = path
