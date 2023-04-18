from fastapi import FastAPI
from routers.main_router import api_router 
from models.orm_all import Base
from config.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
