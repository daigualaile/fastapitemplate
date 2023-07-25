
from fastapi.params import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.db.session import get_db
from app.models.subscription import CreatSub  # 导入 Session
from app.services.sub_service import SubService

router = APIRouter()

@router.get("/user/subscriptions/{user_id}")
def get_SubInfo(user_id:int,db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    service = SubService(db)
    subinfo = service.read(user_id=user_id)
    return {"code": 200, "msg": "ok"}

@router.post("/users/subscription")
async def create_subscription(subscription: CreatSub,db: Session = Depends(get_db)):
    # 在数据库中创建订阅，这需要你实现
    service = SubService(db)
    created_subscription_id = service.create(obj_in=subscription.model_dump())
    return {"subscription_id": created_subscription_id}

