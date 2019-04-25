from flask import Flask, json,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS

db=SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS']=False

POSTGRES = {
    'user' : 'postgres',
    'pw' : 'M0ku8un51n',
    'db' : 'leave_request',
    'host' : 'localhost',
    'port' : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
from models.model import *

@app.route('/login', methods=['POST'])
def login():
    body=request.json
    try:
        employee = Employee.query.filter_by(user_id = body['user_id']).first()
        if employee.password == body['password']:
            return (jsonify(body), 200)
        else: 
            return ("Password Salah",404)
    except Exception as e:
        print (str(e))
        return ("Username Tidak Terdaftar"), 400

@app.route('/getProfil', methods=["GET"])
def getProfil():
    body=request.json
    try:
        employee = Employee.query.filter_by(user_id = body['user_id']).first()
        return (jsonify(employee.serialize()),200)
    except Exception as e:
        return (str(e)),400

@app.route('/getLeave_history', methods=["GET"])
def getLeave_history():
    body = request.json
    try:
        leave_history = Leave_history.query.filter_by(staff_id = body['staff_id']).all()
        return jsonify([emstr.serialize()for emstr in leave_history]),200
    except Exception as e:
        return (str(e)),400

@app.route('/createdLeaveRequest',methods=['POST'])
def createdLeaveRequest():
    body = request.json

    try:
        leaveRequest = Leave_history(
            leave_id = body['leave_id'],
            staff_id = body['staff_id'],
            supervisor_user_id = body['supervisor_user_id'],
            leave_type = body['leave_type'],
            start_date = body['start_date'],
            start_date_length = body['start_date_length'],
            end_date = body['end_date'],
            end_date_length = body['end_date_length'],
            number_of_leave_days = body['number_of_leave_days'],
            requestor_remarks = body['requestor_remarks'],
            approval_status = None,
            approval_remarks = None,
            approval_date = None
        )
        db.session.add(leaveRequest)
        db.session.commit()
        return ("Berhasil mengajukan cuti"),200
    except Exception as e:
        return (str(e)),400

@app.route('/updateLeaveRequest/<leave_id_>', methods=['PUT'])
def updateLeaveRequest(leave_id_):
    body=request.json
    
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
            
        db.session.commit()
        return "Pengajuan cuti anda berhasil di update",200
    except Exception as e:
        return (str(e)),400

@app.route('/approveLeaveRequest/<leave_id_>', methods=['PUT'])
def approveLeaveRequest(leave_id_):

    body=request.json
    try:
        leaveRequest = Leave_history.query.filter_by(leave_id = leave_id_).first()
        for key, value in body.items():
            if key == "approval_status" :
                leaveRequest.approval_status = value
            elif key == "approval_remarks" :
                leaveRequest.approval_remarks = value
            elif key == "approval_date" :
                leaveRequest.approval_date = value 
            
        db.session.commit()
        return "Pengajuan cuti anda berhasil di update",200
    except Exception as e:
        return (str(e)),400

@app.route('/createEmployee',methods=['POST'])
def createEmployee():
    body = request.json

    try:
        employee = Employee(
            staff_id = body['staff_id'],
            staff_name = body['staff_name'],
            user_id = body['user_id'],
            email = body['email'],
            password =  body['password'],
            sex = body['sex'],
            supervisor_user_id = body['supervisor_user_id'],
            job_code = body['job_code'],
            division_code = body['division_code'],
            unit_code = body['unit_code'],
            location = body['location'],
            staff_level = body['staff_level'],
            job_family = body['job_family'],
            job_title = body['job_title'],
            expat = body['expat'],
            contract = body['contract'],
            balance = body['balance']
        )
        db.session.add(employee)
        db.session.commit()
        return ("Berhasil menambahkan pegawai"),200
    except Exception as e:
        return (str(e)),400

@app.route('/addHoliday',methods=['POST'])
def addHoliday():
    body = request.json

    try:
        holiday = Holiday(
            holiday_name = body['holiday_name'],
            holiday_date = body['holiday_date']
        )
        db.session.add(holiday)
        db.session.commit()
        return ("Berhasil menaambahkan hari libur "+body['holiday_name']+" Tanggal : "+body['holiday_date']),200
    except Exception as e:
        return (str(e)),400