from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import get_current_user  # 导入 Session
from app.db.session import get_db
from app.models.account import AccountCreate
from app.services.account_service import AccountService

router = APIRouter()

@router.get("/server/getAccounts")
def get_accounts(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = AccountService(db)
    accounts = service.read_all_accounts()  # 读取所有 accounts
    return {"code": 200, "msg": "ok", "data": accounts}


@router.post("/server/insertAccount")
def create_account(account: AccountCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = AccountService(db)
    account = service.create_account(**account.dict())
    return {"code": 200, "msg": "ok", "data": account}


@router.put("/server/updateAccount/{id}")
def update_account(id: int, account: AccountCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = AccountService(db)
    account = service.update_account(id, account)
    return {"code": 200, "msg": "ok", "data": account}


@router.delete("/server/deleteAccount/{id}")
def delete_account(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = AccountService(db)
    is_deleted = service.delete_account(id)
    if is_deleted:
        return {"code": 200, "msg": "ok"}
    else:
        raise HTTPException(status_code=404, detail="Account not found")
