from fastapi import APIRouter,Depends,HTTPException
from database import database,models,schemas
from routers.JWTToken import oauth2_scheme
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/projects",
    tags=['project']
)

@router.get("/",response_model=list[schemas.Project])
def get_projects(db: Session = Depends(database.get_db)):
    projects = db.query(models.Project).all()
    return projects

@router.post("/create-project",response_model=schemas.Project,status_code=201)
def create_project(project: schemas.ProjectCreate,db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    new_project = models.Project(title = project.title, description = project.description, link = project.link)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.delete("/delete-project/{id}")
def delete_project(id:int,db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project:
        raise HTTPException(status_code=404,detail="Project not found")
    project.delete()
    db.commit()
    return id