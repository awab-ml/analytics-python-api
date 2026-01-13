from datetime import datetime, timezone
from pydantic import BaseModel
from typing import List, Optional

import sqlmodel
from sqlmodel import SQLModel, Field 

from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now





#page visited at any given time
#create the event model for the database 
class EventModel(TimescaleModel, table=True):
    #id : Optional[int] = Field(default=None, primary_key=True)
    
    page: str = Field(index= True) #about, connect page whatever page visited
    description: Optional[str] = ""


    #create_at : datetime = Field(
        #default_factory= get_utc_now, 
       # sa_type=sqlmodel.DateTime(timezone=True), 
       # nullable=False
    #)
    update_at : datetime = Field(
        default_factory= get_utc_now, 
        sa_type=sqlmodel.DateTime(timezone=True), 
        nullable=False
    )

    __chunk_time_interval__ = "INTERVAL 1 DAY"
    __drop_after__ = "INTERVAL 3 DAY"
    
    
    



class EventListSchema(SQLModel):
    results : List[EventModel]
    count : int 


class EventCreateSchema(SQLModel):
    page : str
    


class EventUpateSchema(SQLModel):
    description : str



