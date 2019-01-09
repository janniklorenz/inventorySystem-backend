from flask import request
from flask_restful import Resource
from models import db, Location, LocationSchema

from .helper import *

location_list_schema = LocationSchema(many=True)
location_schema = LocationSchema()

# Location
# shows a single Location
class LocationResource(Resource):
    def get(self, locationID):
        return generic_get_single(Location, locationID, location_schema)

    # Delete Location
    def delete(self, locationID):
        location = Location.query.filter(Location.id == locationID).delete()
        db.session.commit()
        result = location_schema.dump(location).data
        return result, 204

# Location List
# - get to show a list of all Locations
# - post to add a new Location
# - put to edit a existing Location
# - delete to delete Location
class LocationListResource(Resource):
    # Get Locations
    def get(self):
        return generic_get_all(Location, location_list_schema)


    # New Location
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        location, errors = location_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(location)
        db.session.commit()

        result = location_schema.dump(location).data

        return result, 201


    # Edit Location
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = location_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        location = Location.query.filter(Location.id == data.id).first()
        location.updateFromSchema(data)
        db.session.commit()

        result = location_schema.dump(location).data

        return result, 201
