import os 
from typing import List

from sqlmodel import Session, select
from api.db.session import get_session

from sqlalchemy import  func
from datetime import datetime, timedelta, timezone
from timescaledb.hyperfunctions import time_bucket


from fastapi import APIRouter, Depends, HTTPException, Query
from .models import (EventModel,
                    EventBucketSchema,
                      EventListSchema,
                      EventCreateSchema, 
                      get_utc_now)

DEFAULT_LOOKUP_DATA = {"page":"/test"}


router = APIRouter()
# for database connrction 
from api.db.config import DATABASE_URL

# GET data 
#GET /api/events/
@router.get("/", response_model=List[EventBucketSchema])
def read_events(duration: str = Query(default="1 hour"),
                page : List[str] = Query(default=None),
    session: Session =Depends(get_session)
) :

    bucket = time_bucket(duration, EventModel.time).label("bucket")
    
    query = (select(
        bucket.label("bucket"),
        EventModel.page.label("page"),
        func.count().label("count")
        )
    )
    
    if page:
        query = query.where(EventModel.page.in_(page))

    query = query.group_by(
        bucket,
        EventModel.page,

    ).order_by(
        bucket,
        EventModel.page
    )

    results = session.exec(query).mappings().all()

    return results
    
    

# /api/events/{event_id}
@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int,session: Session =Depends(get_session) ) :
    query = select(EventModel).where(EventModel.id == event_id)
    event = session.exec(query).first()
    if not event: 
        raise HTTPException(status_code=404, detail="Event not found ")
    print("this a gooood one ")
    return event 
    



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



#DELETE
#DELETE event
@router.delete("/{event_id}",response_model= EventModel)
def delete_event(event_id: int, 
                session: Session =Depends(get_session)):
                        query = select(EventModel).where(EventModel.id == event_id)
                        obj = session.exec(query).first()
                        if not obj:
                            raise HTTPException(status_code=404, detail="Event not found found")

                        session.delete(obj)
                        session.commit()
                       
                            



