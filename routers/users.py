# Modulo donde van a ir todas las rutas que tienen que ver con usuarios
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import user as UserSchema
from utils import user_utils
from config.db import get_db
from typing import List
from pydantic import EmailStr


router_user = APIRouter()


@router_user.get("/users/{user_id}", response_model=UserSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_utils.get_user(db, user_id=user_id)


@router_user.post("/users/", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    return user_utils.create_user(db=db, user=user)


@router_user.get("/users/", response_model=List[UserSchema.User])
def read_users(db: Session = Depends(get_db)):
    return user_utils.list_users(db)


@router_user.put("/users/{user_id}", response_model=UserSchema.User)
def update_user(user_id: int,
                user: UserSchema.UserUpdate,
                db: Session = Depends(get_db)):
    return user_utils.update_user(db=db, user=user, user_id=user_id)


@router_user.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_utils.delete_user(user_id=user_id, db=db)


@router_user.delete("/users/{user_email}", status_code=204)
def delete_user_by_email(user_email: EmailStr, db: Session = Depends(get_db)):
    return user_utils.delete_user_by_email(user_email=user_email, db=db)