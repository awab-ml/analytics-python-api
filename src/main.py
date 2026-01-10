from typing import Union
from fastapi import FastAPI
from api.events.routing import router as event_router 


# create fastapi app and include routers 
app = FastAPI()
app.include_router(event_router)




#health check endpoint 
@app.get("/healtz ")
def read_health_api():
    return{
        "status": "healthy"
    }
