from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  # 导入 Session
from app.db.session import get_db
from app.services.link_service import LinkService

router = APIRouter()

@router.get("/server/getLinks", response_model=List[dict])
def get_links(db: Session = Depends(get_db)):
    service = LinkService(db)
    links = service.read_all()  # 读取所有 links
    print(links)
    return {"code": 200, "msg": "ok", "data": links}


