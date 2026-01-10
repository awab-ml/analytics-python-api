from typing import Union
from fastapi import FastAPI
from api.events.routing import router

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}



@app.get("/healthz")
def read_health_api():
    return{
        "status": "healthy"
    }
