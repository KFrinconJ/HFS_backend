from fastapi import FastAPI
from routers.main_router import api_router 


# from routers.users import user

# Se importan la configuracion para el acceso a la base de datos


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)


# app.include_router(user)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
