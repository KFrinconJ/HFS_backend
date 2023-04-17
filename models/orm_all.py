from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship

from config.db import Base

#Aqui va todo lo que tiene que ver con el usuario, es decir, el usuario, el rol que este tiene.
class Usuario(Base):
    #Nombre de la tabla
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, index=True)
    nombre = Column(String(150))
    apellido = Column(String(150))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    rol_id = Column(Integer, ForeignKey("rol.id", ondelete='SET NULL'), nullable=True)
    contrato_id = Column(Integer,ForeignKey("contratos.id",ondelete='SET NULL'),nullable=True)
    
    
    contratos_usuario = relationship("Contrato", back_populates="usuarios_contrato")
    roles = relationship("RolUsuario", back_populates="usuarios")



class RolUsuario(Base):
    #Nombre de la tabla
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String)
    
    #Relacion con la tabla de usuarios
    usuarios = relationship("Usuario", back_populates="roles")


class Contrato(Base):
    #Nombre de la tabla
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_contrato = Column(Integer, ForeignKey("tipo_contrato.id"))
    fechaInicio =  Column(Date)
    fechaFinal =  Column(Date)
    
    #Relacion con la tabla de usuario
    usuarios_contrato = relationship("Usuario", back_populates="contratos_usuario")
    tipoContrato = relationship("ContractType", back_populates="contratos")
    

class ContractType(Base):
    #Nombres de la tabla
    __tablename__ = "tipo_contrato"
    id = Column(Integer, primary_key=True, index=True)
    tipo_contrato = Column(String(255))

    #Relacion con la tabla de contratos 
    contratos = relationship("Contrato", back_populates="tipoContrato")




    