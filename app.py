from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
from resources.Device import DeviceResource, DeviceListResource
api.add_resource(DeviceListResource, '/device')
api.add_resource(DeviceResource, '/device/<deviceID>')

from resources.Tag import TagResource, TagListResource
api.add_resource(TagListResource, '/tag')
api.add_resource(TagResource, '/tag/<tagID>')

from resources.User import UserResource, UserListResource
api.add_resource(UserListResource, '/user')
api.add_resource(UserResource, '/user/<userID>')

from resources.Location import LocationResource, LocationListResource
api.add_resource(LocationListResource, '/location')
api.add_resource(LocationResource, '/location/<locationID>')

from resources.Group import GroupResource, GroupListResource
api.add_resource(GroupListResource, '/group')
api.add_resource(GroupResource, '/group/<groupID>')

from resources.Inventory import InventoryResource, InventoryListResource
api.add_resource(InventoryListResource, '/inventory')
api.add_resource(InventoryResource, '/inventory/<inventoryID>')

from resources.Job import JobResource, JobListResource
api.add_resource(JobListResource, '/job')
api.add_resource(JobResource, '/job/<jobID>')
