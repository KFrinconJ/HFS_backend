from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import orm_all as UserModel
from schemas import user as UserSchema
from utils.hashing import Hasher
from pydantic import EmailStr


#Obtener usuario por ID
def get_user(db: Session, user_id: int):
    db_user = db.query(UserModel.Usuario).filter(UserModel.Usuario.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


#Listar todos los usuarios
def list_users(db: Session):
    db_users = db.query(UserModel.Usuario).filter(UserModel.Usuario.is_active == True).all()
    if db_users is None:
        raise HTTPException(status_code=404, detail="Not Users Registered or Active")
    return db_users


#Obtenener usuario por correo
def get_user_by_email(db: Session, email: str):
    return db.query(
        UserModel.Usuario).filter(UserModel.Usuario.email == email).first()

#Crear usuario
# En user especificamos que el tipo de dato que debe de tener es de la clase UserCreate
def create_user(db: Session, user: UserSchema.UserCreate):

    db_user = get_user_by_email(db,email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    

    # En el de user se llaman los campos de user segun se nombro en el esquema

    # Los campos tienen que ir con el mismo nombre que va en el modelo
    db_user = UserModel.Usuario(nombre=user.nombre,
                                apellido=user.apellido,
                                email=user.email,
                                password=Hasher.get_password_hash(
                                    user.password),
                                is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



#Actualizar usuario por id
def update_user(db: Session, user: UserSchema.UserUpdate, user_id:int):
    db_user = get_user(db,user_id)


    for campo, valor in user.dict(exclude_unset=True).items():
        setattr(db_user, campo, valor)
    db.commit()
    db.refresh(db_user)

    return db_user


#Eliminar usuario por id


def delete_user(user_id:int, db: Session):
    db_user = get_user(db,user_id)

    db.delete(db_user)
    db.commit()

    return {"mensaje": "Usuario eliminado exitosamente"}




#Eliminar usuario por correo

def delete_user_by_email(user_email:EmailStr, db:Session):
    db_user = get_user_by_email(user_email,db)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email no se encuentra")
    db.delete(db_user)
    db.commit()

    return {"mensaje": "Usuario eliminado exitosamente"}
    