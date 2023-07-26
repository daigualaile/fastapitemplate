from sqlalchemy import String, Column, DateTime
from .base import BaseModel
from pydantic import BaseModel as PydanticBaseModel
import datetime
class Links(BaseModel):
    __tablename__ = "links"
    title = Column(String, index=True)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow) 
    

class LinksCreate(PydanticBaseModel):
    url:str

# class LinksUpdate(PydanticBaseModel):
#     title:str
#     url:str
    
# class LinksDelete(PydanticBaseModel):
#     id:int