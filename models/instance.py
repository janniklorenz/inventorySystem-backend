from models import db, ma, BaseSchema



class Instance(db.Model):
    __tablename__ = 'instances'
    id = db.Column(db.Integer, primary_key=True)
    inventoryID = db.Column(db.Integer, db.ForeignKey('inventorys.id', ondelete="CASCADE"), nullable=False)
    description = db.Column(db.String(2500), nullable=True)
    status = db.Column(db.String(250), nullable=True)
    locationID = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete="CASCADE"), nullable=True)
    location = db.relationship('Location', backref='instances')

    def updateFromSchema(self, new):
        self.description = new.description
        self.status = new.status
        self.location = new.location

class InstanceSchema(ma.ModelSchema):
    location = ma.Nested('LocationSchema', allow_none=True)
    class Meta(BaseSchema.Meta):
        model = Instance
