from typing import Union
from fastapi import FastAPI
from api.events import router as event_router 


# create fastapi app and include routers 
app = FastAPI()
app.include_router(event_router, prefix="/api/events")




#health check endpoint 
@app.get("/healthz")
def read_health_api():
    return{
        "status": "healthy"
    }
