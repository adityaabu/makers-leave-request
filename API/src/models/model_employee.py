import datetime
from app import db

class Employee(db.Model):
    __tablename__ ='employee'

    staff_id = db.Column(db.String(), primary_key=True)
    staff_name = db.Column (db.String(), nullable=False)
    user_id = db.Column (db.String(), unique=True, nullable=False)
    email = db.Column (db.String(),unique=True, nullable=False)
    password = db.Column (db.String(), nullable=False)
    supervisor_user_id = db.Column (db.String(), nullable=False)
    sex  = db.Column (db.String(), nullable=False)
    division_code = db.Column (db.String(), nullable=False)
    unit_code = db.Column (db.String(), nullable=False)
    location = db.Column (db.String(), nullable=False)
    position = db.Column (db.String(), nullable=False)
    joined_date = db.Column(db.DateTime , nullable=True, default=datetime.date.today)
    expat =  db.Column (db.Integer, nullable=False)
    contract = db.Column (db.Integer, nullable=False)
    balance = db.Column (db.Float, nullable=False) # Nanti di cek lagi bisa float atau tidak
    

    def __init__ (self, staff_id, staff_name, user_id, email, password, supervisor_user_id, sex, division_code, unit_code, location, position , expat, contract, balance): #, joined_date):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.user_id = user_id
        self.email = email
        self.password = password
        self.supervisor_user_id = supervisor_user_id
        self.sex = sex
        self.division_code = division_code
        self.unit_code = unit_code
        self.location = location
        self.position = position
        self.expat = expat
        self.contract = contract
        self.balance = balance
        #self.joined_date =joined_date
    
    def __repr__(self):
        return '<staff_id ()>'.format(self.staff_id)
    
    def serialize(self):
        if (self.sex == "P"):
            sex = "Pria"
        else:
            sex = "Wanita"
        return{
            'staff_id' : self.staff_id,
            'staff_name' : self.staff_name,
            'user_id' : self.user_id,
            'email' : self.email,
            'password' : self.password,
            'supervisor_user_id' : self.supervisor_user_id,
            'sex' : sex,
            'division_code' : self.division_code,
            'unit_code' : self.unit_code,
            'location' : self.location,
            'position' : self.position,
            'joined_date' : self.joined_date.strftime('%d %B %Y'),
            'expat' : self.expat,
            'contract' : self.contract,
            'balance' : self.balance
        }