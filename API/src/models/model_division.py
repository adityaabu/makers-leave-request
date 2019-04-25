import datetime
from app import db

class Division(db.Model):
    __tablename__ ='division'

    division_code =db.Column(db.String(), primary_key=True)
    division_name = db.Column(db.String() , nullable=False)

    def __init__ (self, division_code, division_name):
        self.division_code = division_code
        self.division_name = division_name
    
    def __repr__(self):
        return '<division_code ()>'.format(self.division_code)
    
    def serialize(self):
        return{
            'division_code' : self.division_code,
            'division_name' : self.division_name
        }