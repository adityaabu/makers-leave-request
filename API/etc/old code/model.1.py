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
    job_code = db.Column (db.String(), nullable=False)
    division_code = db.Column (db.String(), nullable=False)
    unit_code = db.Column (db.String(), nullable=False)
    location = db.Column (db.String(), nullable=False)
    staff_level = db.Column (db.String(), nullable=False)
    job_family = db.Column (db.String(), nullable=False)
    job_title = db.Column (db.String(), nullable=False)
    joined_date = db.Column(db.DateTime , nullable=True, default=datetime.date.today)
    expat =  db.Column (db.Integer, nullable=False)
    contract = db.Column (db.Integer, nullable=False)
    balance = db.Column (db.Float, nullable=False) # Nanti di cek lagi bisa float atau tidak
    

    def __init__ (self, staff_id, staff_name, user_id, email, password, supervisor_user_id, sex, job_code, division_code, unit_code, location, staff_level, job_family, job_title , expat, contract, balance):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.user_id = user_id
        self.email = email
        self.password = password
        self.supervisor_user_id = supervisor_user_id
        self.sex = sex
        self.job_code = job_code
        self.division_code = division_code
        self.unit_code = unit_code
        self.location = location
        self.staff_level = staff_level
        self.job_family = job_family
        self.job_title = job_title
        self.expat = expat
        self.contract = contract
        self.balance = balance

     
    
    def __repr__(self):
        return '<staff_id ()>'.format(self.staff_id)
    
    def serialize(self):
        return{
            'staff_id' : self.staff_id,
            'staff_name' : self.staff_name,
            'user_id' : self.user_id,
            'email' : self.email,
            'password' : self.password,
            'supervisor_user_id' : self.supervisor_user_id,
            'sex' : self.sex,
            'job_code' : self.job_code,
            'division_code' : self.division_code,
            'unit_code' : self.unit_code,
            'location' : self.location,
            'staff_level' : self.staff_level,
            'job_family' : self.job_family,
            'job_title' : self.job_title,
            'joined_date' : self.joined_date,
            'expat' : self.expat,
            'contract' : self.contract,
            'balance' : self.balance
        }

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

class Leave(db.Model):
    __tablename__ ='leave'

    leave_code =db.Column(db.String(), primary_key=True)
    leave_name = db.Column (db.String(), nullable=False)
    entitlement = db.Column (db.Integer, nullable=False)
    sex = db.Column (db.String(), nullable=True)

    def __init__ (self, leave_code, leave_name, entitlement, sex):
        self.leave_code = leave_code
        self.leave_name = leave_name
        self.entitlement = entitlement
        self.sex = sex
    
    def __repr__(self):
        return '<leave_code ()>'.format(self.leave_code)
    
    def serialize(self):
        return{
            'leave_code' : self.leave_code,
            'leave_name' : self.leave_name,
            'entitlement' : self.entitlement,
            'sex' : self.sex
        }

class Leave_history(db.Model):
    __tablename__ ='leave_history'

    leave_id =db.Column(db.Integer, primary_key=True)
    staff_id = db.Column (db.String(), nullable=False)
    supervisor_user_id = db.Column (db.String(), nullable=False)
    leave_type = db.Column (db.String(), nullable=False)
    start_date = db.Column(db.DateTime , nullable=False)
    start_date_length = db.Column (db.Float, nullable=False)
    end_date = db.Column(db.DateTime , nullable=False)
    end_date_length = db.Column (db.Float, nullable=False)
    number_of_leave_days = db.Column (db.Float, nullable=False)
    requestor_remarks = db.Column (db.String(), nullable=False)
    approval_status = db.Column (db.Integer, nullable=True)
    approval_remarks = db.Column (db.String(), nullable=True)
    approval_date = db.Column(db.DateTime , nullable=True)

    def __init__ (self, leave_id, staff_id, supervisor_user_id, leave_type, start_date, start_date_length, end_date, end_date_length, number_of_leave_days, requestor_remarks, approval_status, approval_remarks, approval_date):
        self.leave_id = leave_id
        self.staff_id = staff_id
        self.supervisor_user_id = supervisor_user_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.start_date_length = start_date_length
        self.end_date = end_date
        self.end_date_length = end_date_length
        self.number_of_leave_days = number_of_leave_days
        self.requestor_remarks = requestor_remarks
        self.approval_status = approval_status
        self.approval_remarks = approval_remarks
        self.approval_date = approval_date

    def __repr__(self):
        return '<leave_id ()>'.format(self.leave_id)
    
    def serialize(self):
        
        return{
            'leave_id' : self.leave_id,
            'staff_id' : self.staff_id,
            'supervisor_user_id' : self.supervisor_user_id,
            'leave_type' : self.leave_type,
            'start_date' : self.start_date,
            'start_date_length' : self.start_date_length,
            'end_date' : self.end_date,
            'end_date_length' : self.end_date_length,
            'number_of_leave_days' : self.number_of_leave_days,
            'requestor_remarks' : self.requestor_remarks,
            'approval_status' : self.approval_status,
            'approval_remarks' : self.approval_remarks,
            'approval_date' : self.approval_date
        }    
        
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