from flask import request
from flask_restful import Resource
from models import db, Device, DeviceSchema, DeviceSchemaSmall

from .helper import *

device_list_schema = DeviceSchemaSmall(many=True)
device_schema = DeviceSchema()

# Device
# shows a single device
class DeviceResource(Resource):
    def get(self, deviceID):
        return generic_get_single(Device, deviceID, device_schema)

    # Delete Device
    def delete(self, deviceID):
        device = Device.query.filter(Device.id == deviceID).delete()
        db.session.commit()

        result = device_schema.dump(device).data

        return result, 204

# Device List
# - get to show a list of all devices
# - post to add a new device
# - put to edit a existing device
# - delete to delete device
class DeviceListResource(Resource):
    # Get Devices
    def get(self):
        # return generic_get_all(Device, device_list_schema)

        # TESTING:
        json_data = request.get_json(force=False)
        if not json_data:
            return generic_get_all(Device, device_list_schema)

        entry = Device.query.filter(Device.name.like("%"+json_data["name"]+"%"))
        entry = device_list_schema.dump(entry).data
        return entry, 200

    # New Device
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        device, errors = device_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(device)
        db.session.commit()

        result = device_schema.dump(device).data

        return result, 201


    # Edit Device
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = device_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        device = Device.query.filter(Device.id == data.id).first()
        device.updateFromSchema(data)
        db.session.commit()

        result = device_schema.dump(device).data

        return result, 201
