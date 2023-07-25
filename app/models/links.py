from sqlalchemy import String, Column
from .base import BaseModel
from pydantic import BaseModel as PydanticBaseModel
class Links(BaseModel):
    __tablename__ = "links"
    title = Column(String, index=True)
    url = Column(String)
    

class LinksCreate(PydanticBaseModel):
    url:str

# class LinksUpdate(PydanticBaseModel):
#     title:str
#     url:str
    
# class LinksDelete(PydanticBaseModel):
#     id:int