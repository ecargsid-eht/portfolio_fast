import datetime
from uuid import uuid4
from sqlalchemy import DateTime, String,Integer,Text,Column,ForeignKey,UUID,Boolean,Date
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
    blog_title = Column(String(300),unique=True,index=True) 
    content = Column(Text)
    published_at = Column(DateTime,default=datetime.datetime.now())
    
class Message(Base):
    __tablename__ = "messages"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    user_name = Column(String(300),index=True)
    user_email = Column(String(300),index=True)
    message = Column(Text)
    received_at = Column(DateTime,default=datetime.datetime.now())

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String(300),index=True)
    email = Column(String(300),unique=True,index=True)
    password = Column(String(300))
    is_admin = Column(Boolean,default=True)

class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    company_name = Column(String(300),index=True)
    company_image = Column(String(300),nullable=True)
    role = Column(String(150),index=True)
    skills_used = Column(String(300))
    location = Column(String(300))
    start_date = Column(Date,default=datetime.date.today())
    finish_date = Column(Date,nullable=True,default=None)