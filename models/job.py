from models import db, ma, BaseSchema


class Job_HasEvents(db.Model):
    __tablename__ = 'job_hasEvents'
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete="CASCADE"), primary_key=True)
    eventID = db.Column(db.Integer, db.ForeignKey('events.id', ondelete="CASCADE"), primary_key=True)




class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    locationID = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete="CASCADE"), nullable=True)
    location = db.relationship('Location', backref='jobs')
    events = db.relationship('Event', secondary = "job_hasEvents", backref = db.backref("jobs"))
    description = db.Column(db.Text(), nullable=True)

    def updateFromSchema(self, new):
        self.name = new.name
        self.location = new.location
        self.events = new.events
        self.description = new.description

class JobSchema(ma.ModelSchema):
    location = ma.Nested('LocationSchema', allow_none=True)
    events = ma.Nested('EventSchema', many=True)
    class Meta(BaseSchema.Meta):
        model = Job







# - Job_HasUser
