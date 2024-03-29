from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# mysql
# FOR HOSTING SERVER
SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@{os.getenv("HOSTNAME")}:{os.getenv("PORT")}/{os.getenv("DATABASE")}'
# SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{os.getenv("MYSQLUSER")}:{os.getenv("MYSQLPASSWORD")}@{os.getenv("MYSQLHOST")}:{os.getenv("MYSQLPORT")}/{os.getenv("MYSQLDATABASE")}'
# SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{os.getenv("USERNAMEE")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DATABASE")}'
# FOR LOCALHOST
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@db/test'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost:3307/test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
