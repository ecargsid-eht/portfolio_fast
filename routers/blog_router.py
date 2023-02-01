from fastapi import APIRouter,Depends,File,UploadFile
from sqlalchemy.orm import Session
from database import models,schemas,database
from routers.JWTToken import oauth2_scheme


router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.get("/",response_model=list[schemas.Blog])
def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post("/create-blog",response_model=schemas.Blog,status_code=201)
def create_blog(blog: schemas.BlogCreate,db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    new_blog = models.Blog(blog_title = blog.blog_title,content = blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.post("/blog-upload")
def upload(file : UploadFile = File(...)):
    return file.filename