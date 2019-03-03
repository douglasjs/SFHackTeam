from sqlalchemy import Column, Integer, String
from models.database import Base


class Coupon(Base):
    __tablename__ = 'coupons'
    id = Column(Integer, primary_key=True)
    store_name = Column(String(50), unique=True)

    def __init__(self, store_name=None):
        self.store_name = store_name

    def __repr__(self):
        return '<Store %r>' % (self.store_name)
