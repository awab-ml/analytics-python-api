from fastapi import APIRouter
from .schema import EventSchema, EventListSchema

router = APIRouter()

# create events endpoint "routes"
@router.get("/", response_model=EventListSchema)
def read_events()  :
    return{
        "results": [1,2,3,4,5],
        "count": 5
    }


@router.post("/", response_model=EventListSchema)
def create_events()  :
    return{
        "results": [1,2,3,4,5],
        "count": 5
    }



@router.get("/{event_id}")
def get_events(event_id:int) -> EventSchema:
    return{
        "id": event_id
    }

