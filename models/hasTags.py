from models import db, ma, BaseSchema



class HasTags(db.Model):
    __tablename__ = 'has_tags'
    tagID = db.Column(db.Integer, db.ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)
    deviceID = db.Column(db.Integer, db.ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
