from fastapi import APIRouter,Depends,HTTPException
from database import database,models,schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/tags",
    tags=['tags']
)


@router.get("/",response_model=list[schemas.Tag])
def get_tags(db : Session = Depends(database.get_db)):
    tags = db.query(models.Tags).all()
    return tags

@router.post("/create-tag",response_model = schemas.Tag)
def create_tag(tag : schemas.TagCreate,db : Session = Depends(database.get_db)):
    tag = models.Tags(tag_name = tag.tag_name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

@router.delete("/delete-tag/{id}")
def delete_tag(id : int,db : Session = Depends(database.get_db)):
    tag = db.get(models.Tags,id)
    if not tag:
        raise HTTPException(status_code=404,detail="Tag not found")
    db.delete(tag)
    db.commit()
    return id