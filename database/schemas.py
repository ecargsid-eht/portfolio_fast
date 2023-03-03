import datetime
from fastapi import UploadFile
import database.models as models
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

# tags pydantic schema

class TagBase(BaseModel):
    tag_name : str

    class Meta:
        orm_model = models.Tags

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id : int
    
    class Config:
        orm_mode = True


# blog pydantic schema

class BlogBase(BaseModel):
    blog_title : str
    blog_image : str 
    content : str
    # tags : list[int]

    

class BlogCreate(BlogBase):
    tags : list[int]

class Blog(BlogBase):
    id : int
    published_at : datetime.date
    tags : list[Tag]

    class Config:
        orm_mode = True

# message pydantic schema

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

class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
class User(UserBase):
    id : int
    is_admin : bool

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


# experience pydantic schema

class ExperienceBase(BaseModel):
    company_name : str
    company_image : str | None
    role : str
    skills_used : str
    location : str
    start_date : datetime.date | None
    finish_date : datetime.date | None




class ExperienceCreate(ExperienceBase):
    pass

class Exprience(ExperienceBase):
    id : int
    class Config:
        orm_mode = True

