from flask import request
from flask_restful import reqparse, Resource
from models.coupon import CouponModel


class Coupon(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help='This field can\'t be blank')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='This field can\'t be blank')

    def get(self):
        # data = Coupon.parser.parse_args()
        # user_id = data['user_id']
        # store_id = data['store_id']
        user_id = int(request.args.getlist('user_id')[0])
        store_id = int(request.args.getlist('store_id')[0])
        coupon = CouponModel.find_by_user_store(user_id, store_id)
        if coupon:
            return coupon.json()
        return {'msg': 'Coupon not found'}, 404


class CouponList(Resource):
    def get(self):
        coupons = list(map(lambda x: x.json(), CouponModel.find_all()))
        return {'coupons': [coupon for coupon in coupons]}, 200
