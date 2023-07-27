from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

Base = declarative_base()

    
    
class Subscription(BaseModel):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Assuming 'users.id' is the foreign key
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
    user = relationship('User', back_populates='subscriptions', lazy='joined', uselist=False)  

class CreatSub(PydanticBaseModel):
    user_id: int
    start_date:str
    end_date:str
    
    