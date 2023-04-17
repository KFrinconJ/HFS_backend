from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    is_active: bool



class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    rol: Optional[int]
    contrato: Optional[int]

    class Config:
        orm_mode = True