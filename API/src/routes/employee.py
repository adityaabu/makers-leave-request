from flask import jsonify, request
from app import app, db

db.init_app(app)
from src.models.model_employee import *
from src.models.model_division import *

@app.route('/login', methods=['POST'])
def login():
    body=request.json
    try:
        employee = Employee.query.filter_by(user_id = body['user_id']).first()
        body['position'] = (employee.position.split(' ')[0])
        body['staff_id'] = employee.staff_id
        body['sex'] = employee.sex
        if employee.password == body['password']:
            return (jsonify(body), 200)
        else: 
            return ("Password Salah",404)
    except Exception as e:
        print (str(e))
        return ("Username Tidak Terdaftar"), 400

@app.route('/getProfil/<staff_id_>', methods=["GET"])
def getProfil(staff_id_):
    try:
        employee = Employee.query.filter_by(staff_id = staff_id_).first()
        division = Division.query.filter_by(division_code = employee.division_code).first()
        output=employee.serialize()
        output['division']=division.division_name
        return (jsonify(output),200)
    except Exception as e:
        return (str(e)),400 

@app.route('/createEmployee',methods=['POST'])
def createEmployee():
    body = request.json

    try:
        employee = Employee(
            staff_id=body['staff_id'],
            staff_name = body['staff_name'],
            user_id = body['user_id'],
            email = body['email'],
            password =  body['password'],
            sex = body['sex'],
            supervisor_user_id = body['supervisor_user_id'],
            division_code = body['division_code'],
            unit_code = body['unit_code'],
            location = body['location'],
            position = body['position'],
            expat = body['expat'],
            contract = body['contract'],
            balance = body['balance'] #,
            # joined_date = body['joined_date']
        )
        db.session.add(employee)
        db.session.commit()
        return ("Berhasil menambahkan pegawai"),200
    except Exception as e:
        return (str(e)),400