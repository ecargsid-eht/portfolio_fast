
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers.blog_router import router as BlogRouter
from routers.user_router import router as UserRouter
from routers.project_router import router as ProjectRouter
from routers.message_router import router as MessageRouter
from routers.experience_router import router as ExperienceRouter
from routers.tag_router import router as TagRouter
from database import models
from database.database import engine,SessionLocal
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(docs=None,redoc_url=None)
origins = [
    # "https://amrit-utsav.netlify.app",
    # "http://localhost:3000",
    os.getenv("ALLOWED_HOST")
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)


app.include_router(BlogRouter)
app.include_router(UserRouter)
app.include_router(ProjectRouter)
app.include_router(MessageRouter)
app.include_router(ExperienceRouter)
app.include_router(TagRouter)
