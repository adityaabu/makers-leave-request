from app import app, db
from flask import request, jsonify


db.init_app(app)
from src.models.model_holiday import *
from src.models.model_leave import *

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

@app.route('/getAllLeave', methods=["GET"])
def getAllLeave():
    try:
        leave = Leave.query.all()
        return jsonify([emstr.serialize()for emstr in leave]),200
    except Exception as e:
        return (str(e)),400