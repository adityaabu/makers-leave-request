from app import app, db
from flask import jsonify, request
import datetime


db.init_app(app)
from src.models.model_leave import *
from src.models.model_employee import *
from src.models.model_leave_history import *

@app.route('/getLeave_history/<staff_id_>', methods=["GET"])
def getLeave_history(staff_id_):
    try:
        leave_history = Leave_history.query.filter_by(staff_id = staff_id_).all()
        return jsonify([emstr.serialize()for emstr in leave_history]),200
    except Exception as e:
        return (str(e)),400

@app.route('/getLeave_request/<supervisor_user_id_>', methods=["GET"])
def getLeave_request(supervisor_user_id_):
    try:
        leave_history = Leave_history.query.filter_by(supervisor_user_id = supervisor_user_id_).all()
        return jsonify([emstr.serialize()for emstr in leave_history]),200
    except Exception as e:
        return (str(e)),400

def leaveDayCount(start,end):
    sl = list(map(int,start.split('-')))
    el = list(map(int,end.split('-')))
    start_date =datetime.date(sl[0], sl[1], sl[2])
    end_date = datetime.date(el[0], el[1], el[2])
    d = start_date
    delta = datetime.timedelta(days=1)
    weekday=0
    weekend=0
    while d <= end_date:
        hari = (str(d.strftime("%A")))
        print(hari)
        if (hari == "Saturday") or (hari == "Sunday"):
            weekend+=1
        else:
            weekday+=1
        d += delta
    return weekday
    
@app.route('/createdLeaveRequest',methods=['POST'])
def createdLeaveRequest():
    body = request.json
    i=datetime.datetime.now()
    dateNow = ("%s-%s-%s %s:%s:%s" % (i.year, i.month, i.day, i.hour, i.minute, i.second) )
    employee = Employee.query.filter_by(user_id = body['user_id']).first()
    leave = Leave.query.filter_by(leave_name = body['leave_type']).first()
    print ("entitlement = " + str(leave.entitlement))
    start = body['start_date']
    end = body['end_date']
    print (body['start_date_length'])
    number_of_leave_days = float(leaveDayCount(start,end)) - ((1-float(body['start_date_length'])) + (1-float(body['end_date_length'])))
    print ("number_of_leave_days = " + str(number_of_leave_days))
    if leave.entitlement != None:
        if leave.entitlement < float(number_of_leave_days):
            
            leave_day_count = float(number_of_leave_days) - leave.entitlement
            print ("leave_day_count = " + str(leave_day_count))
        else:
            leave_day_count = 0
            print ("leave_day_count = " + str(leave_day_count))
    else : 
        leave_day_count = 0
        print ("leave_day_count = " + str(leave_day_count))

    print ("employee.balance = " + str(employee.balance))
    print (employee.staff_id)
    
    try:
        if employee.balance >= leave_day_count :
            leaveRequest = Leave_history(
                staff_id = employee.staff_id,
                supervisor_user_id = employee.supervisor_user_id,
                leave_type = body['leave_type'],
                start_date = body['start_date'],
                start_date_length = body['start_date_length'],
                end_date = body['end_date'],
                end_date_length = body['end_date_length'],
                number_of_leave_days =number_of_leave_days,
                requestor_remarks = body['requestor_remarks'],
                submission_date = dateNow,
                approval_status = None,
                approval_remarks = None,
                approval_date = None
            )
            
            db.session.add(leaveRequest)
            db.session.commit()
            print ("employee.balance = " + str(employee.balance))
            return ("Berhasil mengajukan cuti"),200
        else:
            print ("employee.balance = " + str(employee.balance))
            return ("Jatah cuti anda tidak cukup"),200
    except Exception as e:
        return (str(e)),400

@app.route('/updateLeaveRequest/<leave_id_>', methods=['PUT'])
def updateLeaveRequest(leave_id_):
    body=request.json
    i=datetime.datetime.now()
    dateNow = ("%s-%s-%s %s:%s:%s" % (i.year, i.month, i.day, i.hour, i.minute, i.second) )
    try:
        leaveRequest = Leave_history.query.filter_by(leave_id = leave_id_).first()
        for key, value in body.items():
            if key == "leave_type" :
                leaveRequest.leave_type = value
            elif key == "start_date" :
                leaveRequest.start_date = value
            elif key == "end_date" :
                leaveRequest.end_date = value 
            elif key == "end_date_length" :
                leaveRequest.end_date_length = value
            elif key == "number_of_leave_days" :
                leaveRequest.number_of_leave_days = value
            elif key == "requestor_remarks" :
                leaveRequest.requestor_remarks = value
        leaveRequest.submission_date = dateNow
        db.session.commit()
        return "Pengajuan cuti anda berhasil di update",200
    except Exception as e:
        return (str(e)),400

@app.route('/approveLeaveRequest/<leave_id_>', methods=['PUT'])
def approveLeaveRequest(leave_id_):

    body=request.json
    try:
        i=datetime.datetime.now()
        approveDate = ("%s-%s-%s" % (i.year, i.month, i.day) )
        leaveRequest = Leave_history.query.filter_by(leave_id = leave_id_).first()
        employee = Employee.query.filter_by(staff_id  = leaveRequest.staff_id ).first()
        leave = Leave.query.filter_by(leave_name = leaveRequest.leave_type).first()
        leaveRequest.approval_status = body['approval_status']
        leaveRequest.approval_remarks = body['approval_remarks']
        leaveRequest.approval_date = approveDate
        print (employee.staff_name)
        print (employee.balance)
        print (leaveRequest.number_of_leave_days)
        if (body['approval_status'] == "1") and (leave.entitlement is not None):
            print (employee.balance)
            employee.balance -= leaveRequest.number_of_leave_days
            print (employee.balance)
        print (approveDate)
        db.session.commit()
        return "Pengajuan cuti anda berhasil di update",200
    except Exception as e:
        return (str(e)),400
