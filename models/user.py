from models import db, ma, BaseSchema



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)

    def updateFromSchema(self, new):
        self.firstName = new.firstName
        self.lastName = new.lastName

class UserSchema(ma.ModelSchema):
    class Meta(BaseSchema.Meta):
        model = User
