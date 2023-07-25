from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from app.models.base import BaseModel
from pydantic import BaseModel as PydanticBaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(255), unique=True, nullable=False)
    user_password = Column(String(255), nullable=False)
    member_status = Column(TINYINT, nullable=False)
    isitan_administrator = Column(Boolean, default=False, nullable=False)
    user_status = Column(TINYINT, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class UserCreate(PydanticBaseModel):
    user_name: str
    user_password: str
