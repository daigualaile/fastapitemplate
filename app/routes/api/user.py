from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from app.models.user import UserCreate
from app.services.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session  # 导入 Session
from app.db.session import get_db
from app.core.auth import create_access_token
from app.config import settings
router = APIRouter()

@router.post("/server/user/register")
def register(usercreate:UserCreate, db: Session = Depends(get_db)):
    print(usercreate.user_name)
    userservice = UserService(db)
    is_registered = userservice.is_registered(usercreate.user_name)
    if(is_registered):
        return {"code": 400, "msg": "用户名已存在"}
    user = userservice.create_user(obj_in=usercreate)
    return {"code": 200, "msg": "ok"}

@router.post("/server/user/login/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer","info":{"id":user.id,"name":user.user_name}}

