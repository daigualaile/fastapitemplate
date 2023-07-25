from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # 声明这是一个抽象类

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
