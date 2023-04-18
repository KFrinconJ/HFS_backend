from typing import Any
from typing import Generator


import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from config.db import Base, get_db
from routers.main_router import api_router



#Para el uso de variables de entorno
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)



#Inicia la aplicacion para la fase de pruebas
def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app




#Conexion con la base de datos de prueba
USER:str = os.getenv("MySQL_USER")
PASSWORD = os.getenv("MySQL_PASSWORD")
HOST:str = os.getenv("MySQL_HOST")
PORT:str = os.getenv("MySQL_PORT")
SCHEMA_NAME:str = os.getenv("MySQL_TEST_SCHEMA")

MYSQL_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA_NAME}"
engine = create_engine(MYSQL_DATABASE_URL)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)




@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)



@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client