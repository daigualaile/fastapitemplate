from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # 声明这是一个抽象类

    id = Column(Integer, primary_key=True, index=True)
    
