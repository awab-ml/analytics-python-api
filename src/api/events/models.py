from datetime import datetime, timezone
from pydantic import BaseModel
from typing import List, Optional

import sqlmodel
from sqlmodel import SQLModel, Field 


def get_utc_now():
    return datetime.now(timezone.utc)


#create the event model for the database 
class EventModel(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
   
    page: Optional[str] = ""
    description: Optional[str] = ""
    create_at : datetime = Field(
        default_factory= get_utc_now, 
        sa_type=sqlmodel.DateTime(timezone=True), 
        nullable=False

    )
    
    



class EventListSchema(SQLModel):
    results : List[EventModel]
    count : int 


class EventCreateSchema(SQLModel):
    page : str
    


class EventUpateSchema(SQLModel):
    description : str



