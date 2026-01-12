from pydantic import BaseModel
from typing import List, Optional


from sqlmodel import SQLModel, Field 



class EventModel(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
   
    page: Optional[str] = ""
    description: Optional[str] = ""
    
    



class EventListSchema(SQLModel):
    results : List[EventModel]
    count : int 


class EventCreateSchema(SQLModel):
    page : str
    


class EventUpateSchema(SQLModel):
    description : str



    