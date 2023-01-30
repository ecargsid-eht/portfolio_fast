import datetime
from uuid import uuid4
from sqlalchemy import DateTime, String,Integer,Text,Column,ForeignKey,UUID,Boolean
from .database import Base

class Project(Base):

    __tablename__ = "projects"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    title = Column(String(100), unique=True,index = True)
    description = Column(Text)
    link = Column(String(300),unique=True)

class Blog(Base):
    __tablename__ = "blogs"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    blog_title = Column(String,unique=True,index=True) 
    content = Column(Text)
    published_at = Column(DateTime,default=datetime.datetime.now())
    
class Message(Base):
    __tablename__ = "messages"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    user_name = Column(String,index=True)
    user_email = Column(String,index=True)
    message = Column(Text)
    received_at = Column(DateTime,default=datetime.datetime.now())

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String,index=True)
    email = Column(String,unique=True,index=True)
    password = Column(String)
    is_admin = Column(Boolean,default=True)
