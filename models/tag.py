from models import db, ma, BaseSchema



class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    color = db.Column(db.String(7), nullable=False, default="#000000")

    def updateFromSchema(self, new):
        self.name = new.name
        self.color = new.color

class TagSchema(ma.ModelSchema):
    class Meta(BaseSchema.Meta):
        model = Tag
