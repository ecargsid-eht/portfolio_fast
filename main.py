
from fastapi import FastAPI
from routers.blog_router import router as BlogRouter
from routers.user_router import router as UserRouter
from routers.project_router import router as ProjectRouter
from routers.message_router import router as MessageRouter
from database import models
from database.database import engine,SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None,redoc_url=None)
origins = [
    "https://amrit-utsav.netlify.app"
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
