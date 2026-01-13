import os 


from sqlmodel import Session, select
from api.db.session import get_session


from fastapi import APIRouter, Depends, HTTPException
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

                 query = select(EventModel).order_by(EventModel.id.asc()).limit(100)
                 results = session.exec(query).all()

                 return{
                    "result": results,
                    "count": len(results)


                 }
    
    

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


# update date 
#PUT /api/events/{event_id}
@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id: int,
                    payload:EventUpateSchema,
                    session: Session =Depends(get_session)) :

            query = select(EventModel).where(EventModel.id == event_id)
            obj = session.exec(query).first()
            if not obj:
                raise HTTPException(status_code=404, detail="Event not found found")

            

            data = payload.model_dump()

            for k, v in data.items():
                setattr(obj, k, v)

            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj


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
                       
                        
                            


