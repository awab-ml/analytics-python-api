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
    
    
    page: str = Field(index= True) #about, connect page whatever page visited
    user_agent : Optional[str] = Field(default="", index=True)
    id_address : Optional[str] = Field(default="", index=True)
    referrer : Optional[str] = Field(default="", index=True)
    session_id : Optional[str] = Field(default="", index=True)
    duration : Optional[str] = Field(default="", index=True)



    __chunk_time_interval__ = "INTERVAL 1 DAY"
    __drop_after__ = "INTERVAL 3 DAY"
    
    
    



class EventListSchema(SQLModel):
    results : List[EventModel]
    count : int 

class EventBucketSchema(SQLModel):
    bucket : datetime
    page : str
    count : int 


class EventCreateSchema(SQLModel):
    page : str
    


class EventUpateSchema(SQLModel):
    description : str



