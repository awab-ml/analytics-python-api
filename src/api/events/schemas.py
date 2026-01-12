from pydantic import BaseModel
from typing import List, Optional



"""
only fields required for event schema are

id
page
description
"""

class EventSchema(BaseModel):
    id : int
    page: Optional[str] = ""
    description: Optional[str] = ""
    



class EventListSchema(BaseModel):
    results : List[EventSchema]
    count : int 


class EventCreateSchema(BaseModel):
    page : str
    


class EventUpateSchema(BaseModel):
    description : str



    