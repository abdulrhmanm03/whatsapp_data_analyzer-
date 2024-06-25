from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    data_frames = relationship("data_frame", back_populates="owner")


class data_frame(Base):
    __tablename__ = "data_frame"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    df_json = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="data_frames")