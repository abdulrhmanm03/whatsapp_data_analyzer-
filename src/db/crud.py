from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import Optional 
from fastapi import Cookie, Depends
from src.db import database, models, schemas
from src.utils.auth import load_session_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.user_name == user_name).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(user_name=user.user_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_current_user_id(token: Optional[str] = Cookie(None), db: Session = Depends(database.SessionLocal)):
    user_name = load_session_token(token)
    user = get_user(db, user_name)
    if user_name:
        return user.id  
    else:
        return None


def get_df_item(db: Session, id: int):
    return db.query(models.data_frame).filter(models.data_frame.id == id).first()


def create_user_df(db: Session, item: schemas.df_create, user_id: int):
    db_df = models.data_frame(**item, owner_id=user_id)
    db.add(db_df)
    db.commit()
    db.refresh(db_df)
    return db_df


