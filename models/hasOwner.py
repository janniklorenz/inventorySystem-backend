from models import db, ma, BaseSchema



class HasOwner(db.Model):
    __tablename__ = 'has_owner'
    inventoryID = db.Column(db.Integer, db.ForeignKey('inventorys.id', ondelete="CASCADE"), primary_key=True)
    ownerID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), primary_key=True)
