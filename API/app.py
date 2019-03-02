from flask import Flask
from flask_restful import Api
from resources.users import UserList, User

app = Flask(__name__)
api = Api(app)

# Actually setup the Api resource routing here
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)
