from models.database import db


class CouponModel(db.Model):
    __tablename__ = 'coupons'
    id = db.Column(db.Integer, primary_key=True)
    limit_times = db.Column(db.Integer)
    used_times = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    # limit_times modify later
    def __init__(self, user_id,  store_id, limit_times=10000, used_times=0):
        self.limit_times = limit_times
        self.used_times = used_times
        self.user_id = user_id
        self.store_id = store_id

    def __repr__(self):
        return '<Store %r, User %r>' % (self.store_id, self.user_id)

    def json(self):
        return {'id': self.id,
                'limit_times': self.limit_times,
                'used_times': self.used_times,
                'user_id': self.user_id,
                'store_id': self.store_id}

    @classmethod
    def find_by_user_store(cls, user_id, store_id):
        return cls.query.filter_by(user_id=user_id, store_id=store_id,).first()

    @classmethod
    def find_by_id(cls, coupon_id):
        return cls.query.filter_by(id=coupon_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
