from fastapi import APIRouter
from .schema import EventSchema

router = APIRouter()

# create events endpoint "routes"
@router.get("/")
def read_events():
    return{
        "events": [1,2,3,4,5]
    }

@router.get("/{event_id}")
def read_events(event_id:int) -> EventSchema:
    return{
        "id": event_id
    }

