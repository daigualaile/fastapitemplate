from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from app.models.admin import AdminCreate
from app.services.admin_service import AdminService
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session  # 导入 Session
from app.db.session import get_db
from app.core.auth import create_access_token
from app.config import settings
router = APIRouter()

@router.post("/server/admin/login/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = AdminService.authenticate_admin(form_data.username, form_data.password)
    
    if not admin:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject={"sub": admin.admin_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/server/admin/register")
def register(admincreate:AdminCreate, db: Session = Depends(get_db)):
    print(admincreate.admin_name)
    userservice = AdminService(db)
    is_registered = userservice.is_registered(admincreate.admin_name)
    if(is_registered):
        return {"code": 400, "msg": "用户名已存在"}
    user = userservice.create_admin(obj_in=admincreate)
    return {"code": 200, "msg": "ok","user": user}