from pydantic import BaseModel
from datetime import date


class Contract(BaseModel):
    id: int
    fecha_inicio: date
    fecha_final: date
    tipo_contrato: int

    class Config:
        orm_mode = True


class ContractType:
    id: int
    tipo_contrato: str

    class Config:
        orm_mode = True
