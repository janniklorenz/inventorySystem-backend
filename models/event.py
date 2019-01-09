from models import db, ma, BaseSchema



class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    startDate = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    endDate = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    description = db.Column(db.Text(), nullable=True)

    def updateFromSchema(self, new):
        self.name = new.name
        self.startDate = new.startDate
        self.endDate = new.endDate
        self.description = new.description

class EventSchema(ma.ModelSchema):
    class Meta(BaseSchema.Meta):
        model = Event
