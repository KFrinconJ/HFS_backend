#Archivo de configuracion de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

import os
from dotenv import load_dotenv
from pathlib import Path

#Para el uso de variables de entorno
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


#Informacion para acceder a la base de datos con mysql
USER:str = os.getenv("MySQL_USER")
PASSWORD = os.getenv("MySQL_PASSWORD")
HOST:str = os.getenv("MySQL_HOST")
PORT:str = os.getenv("MySQL_PORT")
SCHEMA_NAME:str = os.getenv("MySQL_SCHEMA_NAME")

MYSQL_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA_NAME}"

engine = create_engine(MYSQL_DATABASE_URL)
#Cada instancia de la clase SessionLocal es una sesion en la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Se usa la calse Base para crear los modelos de SQLAlchemy
Base = declarative_base()


def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
