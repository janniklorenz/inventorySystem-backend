from models import db, ma, BaseSchema



class Instance(db.Model):
    __tablename__ = 'instances'
    id = db.Column(db.Integer, primary_key=True)
    inventoryID = db.Column(db.Integer, db.ForeignKey('inventorys.id', ondelete="CASCADE"), nullable=False)
    description = db.Column(db.String(2500), nullable=True)

    def updateFromSchema(self, new):
        self.description = new.description

class InstanceSchema(ma.ModelSchema):
    class Meta(BaseSchema.Meta):
        model = Instance
