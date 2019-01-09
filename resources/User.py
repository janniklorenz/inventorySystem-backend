from flask import request
from flask_restful import Resource
from models import db, User, UserSchema

from .helper import *

user_list_schema = UserSchema(many=True)
user_schema = UserSchema()

# user
# shows a single user
class UserResource(Resource):
    def get(self, userID):
        return generic_get_single(User, userID, user_schema)

    # Delete User
    def delete(self, userID):
        user = User.query.filter(User.id == userID).delete()
        db.session.commit()
        result = user_schema.dump(user).data
        return result, 204

# User List
# - get to show a list of all Users
# - post to add a new User
# - put to edit a existing User
# - delete to delete User
class UserListResource(Resource):
    # Get Users
    def get(self):
        return generic_get_all(User, user_list_schema)


    # New User
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        user, errors = user_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data

        return result, 201


    # Edit User
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        user = User.query.filter(User.id == data.id).first()
        user.updateFromSchema(data)
        db.session.commit()

        result = user_schema.dump(user).data

        return result, 201
