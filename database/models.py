import datetime
from uuid import uuid4
from sqlalchemy import DateTime, String,Integer,Text,Column,ForeignKey,Boolean,Date,Table
from sqlalchemy.orm import relationship
from .database import Base
import pytz


# for many to many relationship

blog_tags = Table('blog_tags',Base.metadata,
    Column('blog_id', ForeignKey('blogs.id'),primary_key=True),
    Column('tag_id',ForeignKey('tags.id'),primary_key=True)
)
def time_for_default():
    return datetime.datetime.now(pytz.timezone("Asia/Kolkata"))


class Project(Base):
    __tablename__ = "projects"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    title = Column(String(100), unique=True,index = True)
    description = Column(Text)
    link = Column(String(300),unique=True)

class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    tag_name = Column(String(100))
    blogs = relationship("Blog",secondary=blog_tags,back_populates="tags")


class Blog(Base):
    __tablename__ = "blogs"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    blog_title = Column(String(300),unique=True,index=True)
    blog_image = Column(String(300))
    content = Column(Text)
    tags = relationship("Tags",secondary=blog_tags,back_populates="blogs")

    published_at = Column(Date,default=datetime.date.today())
    



class Message(Base):
    __tablename__ = "messages"

    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    user_name = Column(String(300),index=True)
    user_email = Column(String(300),index=True)
    message = Column(Text)
    received_at = Column(DateTime,default=time_for_default)

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