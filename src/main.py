from contextlib import asynccontextmanager
from api.db.session import init_db

from typing import Union
from fastapi import FastAPI
from api.events import router as event_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    # clean up -> after app shutdown




#create lifespan for the app startup and shutdown 
app = FastAPI(lifespan=lifespan)
# create fastapi app and include routers 
app.include_router(event_router, prefix="/api/events")





#health check endpoint 
@app.get("/healthz")
def read_health_api():
    return{
        "status": "healthy"
    }
