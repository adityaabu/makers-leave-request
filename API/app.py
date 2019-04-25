from flask import Flask, json,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime, requests
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

from src.routes.employee import createEmployee, getProfil, login
from src.routes.leave_request import approveLeaveRequest, getLeave_history, getLeave_request
from src.routes.etc import addHoliday

@app.route('/employee/submit-request', methods=['POST'])
def createRecord():
    token ="Bearer XUOtAGJP2OpaMEpJv6iQf-F71868ELgRmVG5RUSQyGM.xfZAEX_xq0hOAu79R3ABWkgIZF-8FodGG1MZ7yZHmNY"
    url_record = "https://mosaic.nextflow.navcore.com/nextapi/api/records"
    if request.method == 'POST':
        try:
            createRecordInstance = {
                "data": {
                    "definition": {
                    "id": "definitions:bpmn:ef6469ee-b716-4a45-b22d-cc78fb9f7582"
                    }
                }
            }
        
            createRecord = requests.post(url_record, data=json.dumps(createRecordInstance), headers={"Content-Type": "application/json", "Authorization": token})
            
            convertRecordCreate = json.loads(createRecord.text)
            recordId = convertRecordCreate['data']['id']
            print ("record id : "+recordId)
            print ("Token : "+token)
            
            submitRecord=submitRequest(recordId, token)
            
            return jsonify(submitRecord)
           
        except Exception as a:
            return (str(a))     

def submitRequest(recordId, token):
    print ("Masuk fungsi submit request")
    try:
        submitRecordInstance = {
            "data": {
                "form_data": {
                    "email":"saya.ini.adit@gmail.com",
			        "for":"Budiman"
                },
                "comment": "mohon approve nya"
            }
        }
        url_record = "https://mosaic.nextflow.navcore.com/nextapi/api/records/"+recordId+"/submit"
        print (url_record)
        print (submitRecordInstance)
        convertRecordSubmit = json.dumps(submitRecordInstance)
        # submit ke nextflow untuk dapetin process_id tiap pesanan masuk/flow
        submitRecord = requests.post(url_record, data=convertRecordSubmit, headers={"Content-Type": "application/json", "Authorization": token})

        submitRecordResult = json.loads(submitRecord.text)
        # print("INI RESULT SUBMIT RECORD", result)
        return submitRecordResult  

    except Exception as a:
        return (str(a))   