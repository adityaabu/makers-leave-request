import datetime
from app import db

class Unit(db.Model):
    __tablename__ ='unit'

    unit_code = db.Column(db.String(), primary_key=True)
    unit_name = db.Column(db.String() , nullable=False)
    division_name = db.Column(db.String() , nullable=False)

    def __init__ (self, unit_code, unit_name, division_name):
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.division_name = division_name
    
    def __repr__(self):
        return '<unit_code ()>'.format(self.unit_code)
    
    def serialize(self):
        return{
            'unit_code' : self.unit_code,
            'unit_name' : self.unit_name,
            'division_name' : self.division_name
        }
