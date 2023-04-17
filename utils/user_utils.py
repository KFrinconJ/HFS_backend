from sqlalchemy.orm import Session

from models import orm_all as UserModel
from schemas import user as UserSchema


def get_user(db: Session, user_id: int):
    return db.query(UserModel.Usuario).filter(UserModel.Usuario.id == user_id).first()



#En user especificamos que el tipo de dato que debe de tener es de la clase UserCreate
def create_user(db: Session, user: UserSchema.UserCreate):


    #En el de user se llaman los campos de user segun se nombro en el esquema

    # Los campos tienen que ir con el mismo nombre que va en el modelo
    db_user = UserModel.Usuario(nombre = user.nombre,apellido=user.apellido, email = user.email, password = user.password, is_active = user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_user_by_email(db: Session, email: str):
    return db.query(UserModel.Usuario).filter(UserModel.Usuario.email == email).first()