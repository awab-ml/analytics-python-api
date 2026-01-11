from fastapi import APIRouter
from .schema import (
    EventSchema,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema,
)



router = APIRouter()

# GET /api/events/
@router.get("/", response_model=EventListSchema)
def read_events():
    return {
        "results": [1, 2, 3, 4, 5],
        "count": 5
    }

# POST /api/events/
@router.post("/", response_model=EventSchema)
def create_events(payload: EventCreateSchema):
    print("Received payload:", payload.page)
    data = payload.model_dump()# paylod to -> dict 
    return {"id": 12, "page": payload.page}



# GET /api/events/{event_id}
@router.get("/{event_id}", response_model=EventSchema)
def get_events(event_id: int):
    return {"id": event_id}



# PUT /api/events/{event_id}
@router.put("/{event_id}", response_model=EventSchema)
def update_events(event_id: int, payload: EventUpdateSchema):

    print("Update payload:", payload.description)
    return {"id": event_id, "description": payload.description}
