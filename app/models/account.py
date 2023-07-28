from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account_info'

    id = Column(Integer, primary_key=True)
    account_type = Column(String(20), nullable=False) # 修改为str类型
    recharge_date = Column(Date, nullable=False)
    account = Column(String(50), nullable=False)
    account_password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    email_password = Column(String(50), nullable=False)
    user = Column(String(50), nullable=False)
    account_status = Column(String(20), nullable=False) # 修改为str类型

    def __repr__(self):
        return f'<Account(id={self.id}, account_type={self.account_type}, recharge_date={self.recharge_date}, account={self.account}, account_password={self.account_password}, email={self.email}, email_password={self.email_password}, user={self.user}, account_status={self.account_status})>'


class AccountCreate(BaseModel):
    account_type: str # 修改为str类型
    recharge_date: date
    account: str
    account_password: str
    email: str
    email_password: str
    user: str
    account_status: str # 修改为str类型
