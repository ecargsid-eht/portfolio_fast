from fastapi import APIRouter,Depends,HTTPException
from database import database,models,schemas
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from dependencies import password_hash,verify_password
from .JWTToken import create_access_token,ALGORITHM,SECRET_KEY



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

@router.post("/login",status_code=200)
def login_user(user: schemas.UserLogin, db:Session = Depends(database.get_db)):
    selected_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not selected_user:
        raise HTTPException(status_code=404,detail="User not found")
    passw = verify_password(user.password,selected_user.password)
    if passw:
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401,detail="Incorrect password")    


@router.post("/verify-admin/{token}",status_code=200)
def verify_admin(token: str ,db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user
