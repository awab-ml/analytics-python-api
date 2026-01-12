import sqlmodel
from sqlmodel import SQLModel
from .config import DATABASE_URL


if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set ")


engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("create database")
    SQLModel.metadata.create_all(engine)

