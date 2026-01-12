import os 

from fastapi import APIRouter
from .schemas import (EventSchema,
                      EventListSchema,
                      EventCreateSchema, 
                      EventUpateSchema)


router = APIRouter()
# for database connrction 
from api.db.config import DATABASE_URL

# GET data 
#GET /api/events/
@router.get("/")
def read_events() -> EventListSchema:
    print( DATABASE_URL)
    return{
        "results" : [{"id": 1},{"id": 2},{"id": 3}], 
        "count": 3
       
    }

# /api/events/{event_id}
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    print("this a gooood one ")
    return{
        "id": event_id
    }


# create event
# api/events/
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema :

        print(payload.page)
        data = payload.model_dump()
        return {
            "id": 123, 
             **data
        }


# update date 
#PUT /api/events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpateSchema) -> EventSchema :
    print("update is done ")
    print(payload.description)
    data = payload.model_dump()
    return{
        "id": event_id, 
        **data     
    }



