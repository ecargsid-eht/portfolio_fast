import datetime
from fastapi import UploadFile
from pydantic import BaseModel,Field,EmailStr

# project pydantic schema

class ProjectBase(BaseModel):
    title : str
    description : str
    link : str


class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id : int

    class Config:
        orm_mode = True

# blog pydantic schema

class BlogBase(BaseModel):
    blog_title : str
    content : str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id : int
    published_at : datetime.datetime

    class Config:
        orm_mode = True

# blog pydantic schema

class MessageBase(BaseModel):
    user_name : str = Field(...,min_length=3)
    user_email : EmailStr = Field(...)
    message : str = Field(...,min_length=3)

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id : int
    received_at : datetime.datetime

    class Config: 
        orm_mode = True

# user pydantic schema

class UserBase(BaseModel):
    name : str
    email : str

class UserCreate(UserBase):
    password : str
    
class User(UserBase):
    id : int
    is_admin : bool

    class Config:
        orm_mode = True