import datetime
from app import db

class Leave_history(db.Model):
    __tablename__ ='history_leave'

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
    submission_date = db.Column(db.DateTime , nullable=True)
    approval_status = db.Column (db.Integer, nullable=True)
    approval_remarks = db.Column (db.String(), nullable=True)
    approval_date = db.Column(db.DateTime , nullable=True)

    def __init__ (self, staff_id, supervisor_user_id, leave_type, start_date, start_date_length, end_date, end_date_length, number_of_leave_days, requestor_remarks, submission_date, approval_status, approval_remarks, approval_date):
        self.staff_id = staff_id
        self.supervisor_user_id = supervisor_user_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.start_date_length = start_date_length
        self.end_date = end_date
        self.end_date_length = end_date_length
        self.number_of_leave_days = number_of_leave_days
        self.requestor_remarks = requestor_remarks
        self.submission_date = submission_date
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
            'submission_date' : self.submission_date,
            'approval_status' : self.approval_status,
            'approval_remarks' : self.approval_remarks,
            'approval_date' : self.approval_date,
        } 