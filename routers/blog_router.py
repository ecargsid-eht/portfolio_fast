from fastapi import APIRouter,Depends,File,UploadFile,HTTPException
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
    print(blog.dict())
    tags = db.query(models.Tags).filter(models.Tags.id.in_(blog.tags)).all()
    blog.tags = tags
    # blog.tags = db.query(models.Tags).filter(blog.tags).all()
    new_blog = models.Blog(**blog.dict())
    # new_blog = models.Blog(blog_title = blog.blog_title,blog_image = blog.blog_image,content = blog.content,tags = blog.tags)
    # print("model created instance here.")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.post("/blog-upload")
def upload(file : UploadFile = File(...)):
    return file.filename

@router.delete("/delete-blog/{id}")
def delete_blog(id : int,db : Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    blog = db.get(models.Blog,id)
    if not blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    db.delete(blog)
    db.commit()
    return id
    