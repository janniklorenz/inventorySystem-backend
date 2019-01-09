from models import db, ma, BaseSchema



class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    street = db.Column(db.String(250), nullable=True)
    streetNumber = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(250), nullable=True)
    postCode = db.Column(db.String(250), nullable=True)
    latitude = db.Column(db.String(20), nullable=True)
    longitude = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(2500), nullable=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def updateFromSchema(self, new):
        self.name = new.name
        self.street = new.street
        self.streetNumber = new.streetNumber
        self.city = new.city
        self.postCode = new.postCode
        self.latitude = new.latitude
        self.longitude = new.longitude
        self.description = new.description

class LocationSchema(ma.ModelSchema):
    class Meta(BaseSchema.Meta):
        model = Location
