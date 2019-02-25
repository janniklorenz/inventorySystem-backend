from models import db, ma, BaseSchema



class Inventory(db.Model):
    __tablename__ = 'inventorys'
    id = db.Column(db.Integer, primary_key=True)
    deviceID = db.Column(db.Integer, db.ForeignKey('devices.id', ondelete="CASCADE"), nullable=False)
    device = db.relationship('Device', backref='inventorys')
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.String(2500), nullable=True)
    owners = db.relationship('User', secondary = "has_owner", backref = db.backref("inventorys"))
    instances = db.relationship('Instance', cascade="all, delete-orphan", backref = db.backref("inventorys", single_parent=True, cascade="all"))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)
    group = db.relationship('Group', backref=db.backref('items', single_parent=True, cascade="all"))

    def updateFromSchema(self, new):
        self.device = new.device
        self.owners = new.owners
        self.group = new.group
        self.description = new.description

class InventorySchema(ma.ModelSchema):
    device = ma.Nested('DeviceSchema', exclude=["inventorys"])
    owners = ma.Nested('UserSchema', many=True)
    instances = ma.Nested('InstanceSchema', exclude=["inventory"], many=True)
    group = ma.Nested('GroupSchema', exclude=["items"], allow_none=True)
    class Meta(BaseSchema.Meta):
        model = Inventory

    instances_count = ma.Method("get_instances_count")
    def get_instances_count(self, obj):
        return len(obj.instances)
