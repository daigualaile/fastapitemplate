from sqlalchemy.orm import Session
from .database_service import DatabaseService
from app.models.account import Account

class AccountService(DatabaseService):
    def __init__(self, db: Session):
        super().__init__(Account, db)

    def create_account(self, account_type, recharge_date, account, account_password, email, email_password, user, account_status):
        obj_in = {
            'account_type': account_type,
            'recharge_date': recharge_date,
            'account': account,
            'account_password': account_password,
            'email': email,
            'email_password': email_password,
            'user': user,
            'account_status': account_status
        }
        return self.create(obj_in)

    def read_account(self, id):
        return self.read(id)

    def update_account(self, id, obj_in):
        return self.update(id, obj_in)

    def delete_account(self, id):
        return self.delete(id)
    
    def read_all_accounts(self):
        return self.read_all()
