import datetime
from typing import Dict, Any
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.services.database_service import DatabaseService
from app.db.session import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def create_user(self, obj_in: Dict[str,Any]) -> User:
        obj_in.user_password =  pwd_context.hash(obj_in.user_password)
        db_obj = self.model(user_name=obj_in.user_name,user_password=obj_in.user_password,member_status=0,user_status=0, created_at=datetime.datetime.now())  # Assuming create_time is needed
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def is_registered(self,user_name: str) -> bool:
        db_obj = self.db.query(self.model).filter_by(user_name=user_name).first()
        return db_obj
    
    @staticmethod
    def authenticate_user(username: str, password: str):
        db = SessionLocal()
        user = db.query(User).filter(User.user_name == username,User.isitan_administrator==0).first()
        if not user:
            return False
        if not pwd_context.verify(password, user.user_password):
            return False
        return user
    
    def change_password(self, id: int, username: str, current_password: str, new_password: str) -> bool:
    # 根据id和username查询用户是否存在
        user = self.db.query(self.model).filter(self.model.id == id, self.model.user_name == username).first()
        if not user:
            # 如果用户不存在，返回False
            return False
        # 根据current_password验证用户是否正确
        if not pwd_context.verify(current_password, user.user_password):
            # 如果密码不正确，返回False
            return False
        # 根据new_password更新用户的密码
        user.user_password = pwd_context.hash(new_password)
        self.db.commit()
        # 返回True
        return True
