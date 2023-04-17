# Modulo donde van a ir todas las rutas que tienen que ver con usuarios
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import orm_all as UserModel
from schemas import user as UserSchema
from utils import user_utils
from config.db import SessionLocal, engine

UserModel.Base.metadata.create_all(bind=engine)


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/{user_id}", response_model=UserSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_utils.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_utils.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_utils.create_user(db=db, user=user)

