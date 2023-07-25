import datetime
from typing import Dict, Any

from sqlalchemy.orm import Session
from app.models.subscription import Subscription
from app.services.database_service import DatabaseService

class SubService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(Subscription, db)

    def read(self,user_id):
        subscription = self.db.query(Subscription).filter(Subscription.user_id == user_id).first()
        if not subscription:
            return {"error": "No subscription found for this user"}
        return subscription
    
    def create(self, obj_in: Dict[str, Any]) -> int:
        print(obj_in)
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj.id
