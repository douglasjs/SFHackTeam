from flask_restful import reqparse, Resource
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field can\'t be blank')

    def get(self, store_id):
        store = StoreModel.find_by_id(store_id)
        if store:
            return store.json()
        return {'msg': 'Store not found'}, 404


class StoreList(Resource):
    def get(self):
        stores = list(map(lambda x: x.json(), StoreModel.find_all()))
        return {'stores': [store for store in stores]}, 200

    def post(self):
        # parse client input data
        data = Store.parser.parse_args()
        name = data['name']
        if StoreModel.find_by_name(name):
            return {'msg': '{} already exist'.format(name)}, 400
        # create store info into database
        store = StoreModel(**data)
        store.add_to_db()
        return {'msg': 'success'}, 201
