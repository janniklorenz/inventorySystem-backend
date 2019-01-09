from flask import request
from flask_restful import Resource
from models import db, Inventory, InventorySchema, InventorySchema, Device, DeviceSchema
import json

from .helper import *

inventory_list_schema = InventorySchema(many=True, exclude=['instances'])
inventory_schema = InventorySchema()

# inventory
# shows a single inventory
class InventoryResource(Resource):
    def get(self, inventoryID):
        entry = Inventory.query.filter(Inventory.id==inventoryID).outerjoin(Device).first()
        return generic_single(entry, inventory_schema)

    # Delete Inventory
    def delete(self, inventoryID):
        inventory = Inventory.query.filter(Inventory.id == inventoryID).delete()
        db.session.commit()
        result = inventory_schema.dump(inventory).data
        return result, 204

# Inventory List
# - get to show a list of all Inventorys
# - post to add a new Inventory
# - put to edit a existing Inventory
# - delete to delete Inventory
class InventoryListResource(Resource):
    # Get Inventorys
    def get(self):
        entry = Inventory.query.outerjoin(Device).all()
        return generic_all(entry, inventory_list_schema)


    # New Inventory
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        inventory, errors = inventory_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(inventory)
        db.session.commit()

        result = inventory_schema.dump(inventory).data

        return result, 201


    # Edit Inventory
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = inventory_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        inventory = Inventory.query.filter(Inventory.id == data.id).first()
        inventory.updateFromSchema(data)
        db.session.commit()

        result = inventory_schema.dump(inventory).data

        return result, 201
