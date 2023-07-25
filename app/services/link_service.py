from sqlalchemy.orm import Session
from app.models.links import Links
from app.services.database_service import DatabaseService

class LinkService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(Link, db)

    def delete_by_id(self, id: int):
        link = self.db.query(self.model).get(id)
        if link:
            self.db.delete(link)
            self.db.commit()
            return True
        return False
