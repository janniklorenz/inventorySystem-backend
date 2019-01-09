from models import db, ma, BaseSchema



class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    vendor = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    tags = db.relationship('Tag', secondary = "has_tags", backref = db.backref("devices"))

    def updateFromSchema(self, new):
        self.name = new.name
        self.title = new.title
        self.vendor = new.vendor
        self.description = new.description
        self.tags = new.tags

class DeviceSchemaSmall(ma.ModelSchema):
    inventorys = ma.Nested('InventorySchema', exclude=["device", "instances"], dump_only=True, many=True)
    tags = ma.Nested('TagSchema', many=True)
    class Meta(BaseSchema.Meta):
        model = Device

    all_instances_count = ma.Method("get_all_instances_count")
    def get_all_instances_count(self, obj):
        return sum(len(inventory.instances) for inventory in obj.inventorys)

class DeviceSchema(ma.ModelSchema):
    inventorys = ma.Nested('InventorySchema', exclude=["device"], dump_only=True, many=True)
    tags = ma.Nested('TagSchema', many=True)
    class Meta(BaseSchema.Meta):
        model = Device
