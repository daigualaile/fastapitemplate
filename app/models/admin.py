from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from app.models.base import BaseModel
from pydantic import BaseModel as PydanticBaseModel

class Admin(BaseModel):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    admin_name = Column(String(255), unique=True, nullable=False)
    admin_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class AdminCreate(PydanticBaseModel):
    admin_name: str
    admin_password: str
