from models import db, ma, BaseSchema



class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def updateFromSchema(self, new):
        self.name = new.name

class GroupSchema(ma.ModelSchema):
    items = ma.Nested('InventorySchema', exclude=["group"], many=True)
    class Meta(BaseSchema.Meta):
        model = Group
