from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from marshmallow_sqlalchemy import ModelSchema

ma = Marshmallow()
db = SQLAlchemy()

# We need to set sqla session to our session, otherwise nested fields can not be deserialized
# https://github.com/marshmallow-code/marshmallow-sqlalchemy/issues/20#issuecomment-136400602
# https://stackoverflow.com/questions/36706096/how-to-use-load-with-nested-objects-in-marshmallow-sqlalchemy
class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = db.session

# Order matters!
from models.group import Group,GroupSchema
from models.hasTags import HasTags
from models.tag import Tag,TagSchema
from models.device import Device,DeviceSchema,DeviceSchemaSmall
from models.hasOwner import HasOwner
from models.user import User,UserSchema
from models.location import Location,LocationSchema
from models.event import Event,EventSchema
from models.job import Job,JobSchema
from models.instance import Instance,InstanceSchema
from models.inventory import Inventory,InventorySchema
