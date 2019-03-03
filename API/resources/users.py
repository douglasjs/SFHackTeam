from flask_restful import reqparse, Resource
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field can\'t be blank')

    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json()
        return {'msg': 'User not found'}, 404


class UserList(Resource):
    def get(self):
        users = list(map(lambda x: x.json(), UserModel.find_all()))
        return {'users': [user for user in users]}, 200

    def post(self):
        # parse client input data
        data = User.parser.parse_args()
        name = data['name']
        if UserModel.find_by_name(name):
            return {'msg': '{} already exist'.format(name)}, 400
        # create user info into database
        user = UserModel(**data)
        user.add_to_db()
        return {'msg': 'success'}, 201
