from fastapi import APIRouter,Depends,HTTPException
from database import schemas,database,models
from sqlalchemy.orm import Session
from routers.JWTToken import oauth2_scheme

router = APIRouter(
    prefix='/experiences',
    tags= ['experiences']
)

@router.get("/",response_model=list[schemas.Exprience])
def get_experiences(db : Session = Depends(database.get_db)):
    experience = db.query(models.Experience).all()
    return experience

@router.post("/create-experience",response_model=schemas.Exprience)
def create_experiences(experience : schemas.ExperienceCreate,db : Session = Depends(database.get_db),token : str = Depends(oauth2_scheme)):
    new_experience = models.Experience(**experience.dict())
    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)
    return new_experience
    
@router.delete("/delete-experience/{id}")
def delete_experiences(id: int,db : Session = Depends(database.get_db),token : str = Depends(oauth2_scheme)):
    experience = db.get(models.Experience,id)
    if not experience:
        raise HTTPException(status_code=404,detail="Experience not found")
    db.delete(experience)
    db.commit()
    return id

@router.patch("/update-experience/{id}",response_model=schemas.Exprience)
def update_experience(exp: schemas.ExperienceCreate,id:int, db : Session = Depends(database.get_db), token : str = Depends(oauth2_scheme)):
    experience = db.query(models.Experience).filter(models.Experience.id == id)
    if not experience.first():
        raise HTTPException(status_code=404,detail="Experience not found")
    experience.update(exp.dict(exclude_unset = True))
    db.commit()
    return experience.first()
