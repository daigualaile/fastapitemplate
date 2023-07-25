from typing import List
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.auth import get_current_user  # 导入 Session
from app.db.session import get_db
from app.models.links import LinksCreate
from app.services.link_service import LinkService

router = APIRouter()

@router.get("/server/getLinks")
def get_links(db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    service = LinkService(db)
    links = service.read_all()  # 读取所有 links
    return {"code": 200, "msg": "ok", "data": links}


@router.post("/server/insetLinks")
def create_link(url: LinksCreate, db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    service = LinkService(db)
    link = service.create(url)
    return {"code": 200, "msg": "ok", "data": link}


@router.delete("/server/delLinks/{id}")
def delete_link(id: int, db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    service = LinkService(db)
    is_deleted = service.delete(id)
    if is_deleted:
        return {"code": 200, "msg": "ok"}
    else:
        raise HTTPException(status_code=404, detail="Link not found")