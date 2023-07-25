from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.sql.sqltypes import Enum
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship


Base = declarative_base()

class SubscriptionType(PyEnum):
    ONE_MONTH = "一个月"
    ONE_QUARTER = "一个季度"
    ONE_YEAR = "一年"
    
    
class Subscription(Base):
    __tablename__ = 'subscriptions'
    subscription_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Assuming 'users.id' is the foreign key
    subscription_type = Column(Enum(SubscriptionType), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
    user = relationship('User', back_populates='subscriptions', lazy='joined', uselist=False)  

class CreatSub(PydanticBaseModel):
    user_id: int
    subscription_type:str
    start_date:str
    end_date:str
    