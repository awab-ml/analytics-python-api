from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def read_events():
    return{
        "events": [1,2,3,4,5]
    }

