import os 


from sqlmodel import Session, select
from api.db.session import get_session


from fastapi import APIRouter, Depends
from .models import (EventModel,
                      EventListSchema,
                      EventCreateSchema, 
                      EventUpateSchema)


router = APIRouter()
# for database connrction 
from api.db.config import DATABASE_URL

# GET data 
#GET /api/events/
@router.get("/")
def read_events(session: Session =Depends(get_session),
                 response_model=EventListSchema) :

                 query = select(EventModel).limit(100)
                 results = session.exec(query).all()

                 return{
                    "result": results,
                    "count": len(results)


                 }
    
    

# /api/events/{event_id}
@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    print("this a gooood one ")
    return{
        "id": event_id
    }


# create event
# api/events/
@router.post("/", response_model=EventModel)
def create_event(
    payload: EventCreateSchema,
      session: Session =Depends(get_session))  :

            print(payload.page)
            data = payload.model_dump()
            object = EventModel.model_validate(data)
            session.add(object)
            session.commit()
            session.refresh(object)
            return object


# update date 
#PUT /api/events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpateSchema) -> EventModel :
    print("update is done ")
    print(payload.description)
    data = payload.model_dump()
    return{
        "id": event_id, 
        **data     
    }



