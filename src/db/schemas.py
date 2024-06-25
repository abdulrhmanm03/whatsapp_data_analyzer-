from typing import List

from pydantic import BaseModel


class df_base(BaseModel):
    title: str
    df_json: str 


class data_frame(df_base):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
        
class df_create(df_base):
    title: str
    df_json: str
    owner_id: int           


class UserBase(BaseModel):
    user_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    data_frames: List[data_frame] = []

    class Config:
        orm_mode = True