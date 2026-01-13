import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_TIMEZONE

import timescaledb
from timescaledb import create_engine



if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set ")


engine = timescaledb.create_engine(DATABASE_URL, timezone=DB_TIMEZONE)


#create table  database
def init_db():
    print("create database")
    SQLModel.metadata.create_all(engine)
    print("create hypertables")
    timescaledb.metadata.create_all(engine)




def get_session():
    with Session(engine) as session:
        yield  session

