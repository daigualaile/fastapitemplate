import datetime
from typing import Dict, Any

from sqlalchemy.orm import Session
from app.models.links import Links
from app.services.database_service import DatabaseService

class LinkService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(Links, db)

    def create(self, obj_in: Dict[str,Any]) -> Links:
        db_obj = self.model(url=obj_in.url, created_at=datetime.datetime.now())  # Assuming create_time is needed
        print(db_obj)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj