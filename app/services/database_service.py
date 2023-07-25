from sqlalchemy.orm import Session

class DatabaseService:
    def __init__(self, model, db: Session):
        self.model = model
        self.db = db

    def create(self, obj_in):
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def read(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def update(self, id, obj_in):
        db_obj = self.db.query(self.model).filter(self.model.id == id).first()
        for var, value in vars(obj_in).items():
            setattr(db_obj, var, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id):
        db_obj = self.db.query(self.model).filter(self.model.id == id).first()
        self.db.delete(db_obj)
        self.db.commit()
        return db_obj
    
    def read_all(self):
        return self.db.query(self.model).all()
