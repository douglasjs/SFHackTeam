from flask import Flask
from flask_restful import Api
from resources.users import UserList, User
from resources.stores import StoreList, Store
from resources.coupons import CouponList, Coupon

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sfhacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Actually setup the Api resource routing here
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/stores/<store_id>')
api.add_resource(CouponList, '/coupons')
api.add_resource(Coupon, '/coupon')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    from models.database import db
    db.init_app(app)
    app.run(port=5000, debug=True)
