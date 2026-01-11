from pydantic import BaseModel
from typing import List, Optional

class EventCreateSchema(BaseModel):
    page: str   # ("/test")




class EventUpdateSchema(BaseModel):
    description: str




class EventListSchema(BaseModel):
    results: List[int]
    count: int




class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = ""



