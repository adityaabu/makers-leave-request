import datetime
from app import db

class Leave(db.Model):
    __tablename__ ='leave'

    leave_id =db.Column(db.String(), primary_key=True)
    leave_name = db.Column (db.String(), nullable=False)
    entitlement = db.Column (db.Integer, nullable=False)
    sex = db.Column (db.String(), nullable=True)

    def __init__ (self, leave_id, leave_name, entitlement, sex):
        self.leave_id = leave_id
        self.leave_name = leave_name
        self.entitlement = entitlement
        self.sex = sex
    
    def __repr__(self):
        return '<leave_id ()>'.format(self.leave_id)
    
    def serialize(self):
        return{
            'leave_id' : self.leave_id,
            'leave_name' : self.leave_name,
            'entitlement' : self.entitlement,
            'sex' : self.sex
        }  