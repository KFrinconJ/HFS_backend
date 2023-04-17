#Archivo de configuracion de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




#Informacion para acceder a la base de datos con mysql
USER = "root"
PASSWORD = "root"
HOST = "localhost"
PORT = "3306"
SCHEMA_NAME = "fs_programasacademicos"

MYSQL_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA_NAME}"

engine = create_engine(MYSQL_DATABASE_URL)
#Cada instancia de la clase SessionLocal es una sesion en la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Se usa la calse Base para crear los modelos de SQLAlchemy
Base = declarative_base()

