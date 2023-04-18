from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    is_active: bool



class UserCreate(UserBase):
    password: str


class User(UserBase):
    rol: Optional[int] = None
    contrato: Optional[int] = None

    class Config:
        orm_mode = True



class UserUpdate(UserBase):
    nombre: str = None
    apellido: str = None
    email: str = None
    is_active: bool = None
    





##############################

class RolUser(BaseModel):
    id : int
    nombre_rol : str

    class Config:
        orm_mode = True


