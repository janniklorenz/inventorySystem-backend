from flask import request
from flask_restful import Resource
from models import db, Group, GroupSchema

from .helper import *

group_list_schema = GroupSchema(many=True)
group_schema = GroupSchema()

# Group
# shows a single group
class GroupResource(Resource):
    def get(self, groupID):
        return generic_get_single(Group, groupID, group_schema)

    # Delete Group
    def delete(self, groupID):
        group = Group.query.filter(Group.id == groupID).delete()
        db.session.commit()

        result = group_schema.dump(group).data

        return result, 204

# Group List
# - get to show a list of all groups
# - post to add a new group
# - put to edit a existing group
# - delete to delete group
class GroupListResource(Resource):
    # Get Groups
    def get(self):
        # return generic_get_all(Group, group_list_schema)

        # TESTING:
        json_data = request.get_json(force=False)
        if not json_data:
            return generic_get_all(Group, group_list_schema)

        entry = Group.query.filter(Group.name.like("%"+json_data["name"]+"%"))
        entry = group_list_schema.dump(entry).data
        return entry, 200

    # New Group
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        group, errors = group_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(group)
        db.session.commit()

        result = group_schema.dump(group).data

        return result, 201


    # Edit Group
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = group_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        group = Group.query.filter(Group.id == data.id).first()
        group.updateFromSchema(data)
        db.session.commit()

        result = group_schema.dump(group).data

        return result, 201
