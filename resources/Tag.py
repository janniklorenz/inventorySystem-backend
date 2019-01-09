from flask import request
from flask_restful import Resource
from models import db, Tag, TagSchema

from .helper import *

tag_list_schema = TagSchema(many=True)
tag_schema = TagSchema()

# Tag
# shows a single tag
class TagResource(Resource):
    def get(self, tagID):
        return generic_get_single(Tag, tagID, tag_schema)

    # Delete Tag
    def delete(self, tagID):
        tag = Tag.query.filter(Tag.id == tagID).delete()
        db.session.commit()
        result = tag_schema.dump(tag).data
        return result, 204

# Tag List
# - get to show a list of all tags
# - post to add a new tag
# - put to edit a existing tag
# - delete to delete tag
class TagListResource(Resource):
    # Get Tags
    def get(self):
        return generic_get_all(Tag, tag_list_schema)


    # New Tag
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        tag, errors = tag_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(tag)
        db.session.commit()

        result = tag_schema.dump(tag).data

        return result, 201


    # Edit Tag
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = tag_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        tag = Tag.query.filter(Tag.id == data.id).first()
        tag.updateFromSchema(data)
        db.session.commit()

        result = tag_schema.dump(tag).data

        return result, 201
