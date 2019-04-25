import datetime
from app import db 
        
class Holiday(db.Model):
    __tablename__ ='holiday'
    holiday_id =db.Column(db.Integer, primary_key=True)
    holiday_name =db.Column(db.String(), primary_key=True)
    holiday_date = db.Column(db.DateTime , nullable=False)

    def __init__ (self, holiday_name, holiday_date):
        self.holiday_name = holiday_name
        self.holiday_date = holiday_date
    
    def __repr__(self):
        return '<holiday_id ()>'.format(self.holiday_id)
    
    def serialize(self):
        return{
            'holiday_id' : self.holiday_id,
            'holiday_name' : self.holiday_name,
            'holiday_date' : self.holiday_date
        }