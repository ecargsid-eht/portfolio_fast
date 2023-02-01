from fastapi import APIRouter,Depends
from database import database,models,schemas
from sqlalchemy.orm import Session
from routers.JWTToken import oauth2_scheme,verify_admin
router = APIRouter(
    prefix="/messages",
    tags=['message']
)

@router.get("/",response_model=list[schemas.Message])
def get_messages(token : str = Depends(verify_admin),db: Session = Depends(database.get_db)):
    messages = db.query(models.Message).all()
    return messages
    # return {"token" : token}

@router.post("/create-message",response_model=schemas.Message,status_code=201)
def create_message(message: schemas.MessageCreate,db: Session = Depends(database.get_db)):
    new_message = models.Message(user_name = message.user_name, user_email = message.user_email, message = message.message)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

@router.delete('/delete-message/{id}')
def delete_message(id:int,db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    db.query(models.Message).filter(models.Message.id == id).delete()
    db.commit()
    return id