from fastapi import APIRouter,Depends
from database import database,models,schemas
from sqlalchemy.orm import Session
from dependencies import password_hash,verify_password

router = APIRouter(
    prefix="/users",
    tags=['user']
)

@router.post("/create-user",response_model=schemas.User,status_code=201)
def create_user(user : schemas.UserCreate,db: Session = Depends(database.get_db)):
    hashed_password = password_hash(user.password)
    new_user = models.User(name = user.name,email = user.email,password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/",response_model=list[schemas.User])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users
