import datetime
from typing import Dict, Any
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.services.database_service import DatabaseService
from app.db.session import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AdminService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(Admin, db)

    def create_admin(self, obj_in: Dict[str,Any]) -> Admin:
        obj_in.admin_password =  pwd_context.hash(obj_in.admin_password)
        db_obj = self.model(admin_name=obj_in.admin_name,admin_password=obj_in.admin_password, created_at=datetime.datetime.now())  # Assuming create_time is needed
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def is_registered(self,admin_name: str) -> bool:
        db_obj = self.db.query(self.model).filter_by(admin_name=admin_name).first()
        return db_obj
    
    @staticmethod
    def authenticate_admin(adminname: str, password: str):
        db = SessionLocal()
        admin = db.query(Admin).filter(Admin.admin_name == adminname).first()
        if not admin:
            return False
        if not pwd_context.verify(password, admin.admin_password):
            return False
        return admin