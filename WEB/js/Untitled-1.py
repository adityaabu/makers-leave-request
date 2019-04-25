@app.route('/employee/submit-request', methods=['POST'])
def createRecord():
    body = request.json
    
    if request.method == 'POST':
        try:
            employees = Employees.query.filter_by(id = body['id']).first()
            manager = Employees.query.filter(Employees.position == 'Web Developer').first()
            createRecordInstance = {
                "data": {
                    "definition": {
                    "id": os.getenv('DEFINITION_ID')
                    }
                }
            }
        
            createRecord = requests.post(os.getenv("URL_RECORD"), data=json.dumps(createRecordInstance), headers={"Content-Type": "application/json", "Authorization": "Bearer %s" % employees.token})
            
            convertRecordCreate = json.loads(createRecord.text)
            recordId = convertRecordCreate['data']['id']

            submitRecord = submitRequest(recordId, employees.token, employees.name, employees.email, employees.position, manager.email)
            
            body['message'] = "Record has Submitted"   
            return jsonify(submitRecord)
           
        except Exception as a:
            return (str(a))     

def submitRequest(recordId, employee_token, requesterName, requesterEmail, requesterPosition, approvalEmail):
    body = request.json
    try:
        employees = Employees.query.filter_by(id = body['id']).first()

        submitRecordInstance = {
            "data": {
                "form_data": {
                    "requesterName": requesterName,
                    "requesterEmail":requesterEmail,
                    "requesterPosition": requesterPosition,
                    "approverEmail": approvalEmail,
                    "purchaseId": "1"
                },
                    "comment": "Mohon Approvalnya dari Mang Ipon"
            }
        }
        
        convertRecordSubmit = json.dumps(submitRecordInstance)
        # submit ke nextflow untuk dapetin process_id tiap pesanan masuk/flow
        submitRecord = requests.post(os.getenv('URL_RECORD') + "/"+recordId+"/submit", data=convertRecordSubmit, headers={"Content-Type": "application/json", "Authorization": "Bearer %s" % employees.token})

        submitRecordResult = json.loads(submitRecord.text)
        # print("INI RESULT SUBMIT RECORD", result)
        return submitRecordResult  

    except Exception as a:
        return (str(a))   

@app.route('/employee/manager-task/', methods=['POST'])
def submitTask():
    body = request.json
    
    if request.method == 'POST':
        try:
            employees = Employees.query.filter_by(id = body['id']).first()
            query = "?folder=app:task:all&page[number]=1&page[size]=10"
            urlGetTask = os.getenv("URL_TASK") + query

            requestGetTask = requests.get(urlGetTask, headers={
                "Content-Type": "application/json", 
                "Authorization": "Bearer %s" % employees.token
                })
            
            res = json.loads(requestGetTask.text)
            if res['data'] is None or len(res['data']) == 0:
                body['message'] = "No task list"
                return jsonify(body)
            else:                
                taskId = res['data'][0]['id' ]

                submitTaskInstance = {
                    "data": {
                        "form_data":{
                            "action":"approve",
                            "requesterEmail":"imamhawari19@gmail.com"
                        },
                        "comment": "approve mantap cuy requestnya, lanjutkan"
                    }
                }
                submitTaskConverted = json.dumps(submitTaskInstance)
                
                submitTask = requests.post(os.getenv('URL_TASK') + "/"+taskId+"/submit", data=submitTaskConverted, headers={"Content-Type": "application/json", "Authorization": "Bearer %s" % employees.token})

                # submitTaskResult = json.loads(submitTask.text)
                statusCode = 200
                
                body['message'] = "Task has Submitted"
return jsonify(body), statusCode

        except Exception as a:
            statusCode = 400
            return (str(a)), statusCode


@app.route('/list-task/<id_>', methods=['GET'])
def getTaskList(id_):
    try:
        employees = Employees.query.filter_by(id = id_).first()
        query = "?folder=app:task:all&page[number]=1&page[size]=10"
        urlGetTask = os.getenv("URL_TASK") + query

        requestGetTask = requests.get(urlGetTask, headers = {
            "Content-Type": "application/json", 
            "Authorization": "Bearer %s" % employees.token
        })

        res = json.loads(requestGetTask.text)

        return jsonify(res)
        
    except Exception as a:
        statusCode = 400
        return (str(a))`
`DATABASE_URI = postgresql://postgres:123@localhost:5432/pr
SECRET=squad
API_KEY=makansate


URL_RECORD = https://mosaic.nextflow.navcore.com/nextapi/api/records
URL_TASK = https://mosaic.nextflow.navcore.com/nextapi/api/tasks
DEFINITION_ID = definitions:bpmn:f4500aa2-4f3a-4752-992f-f37cc2718613

DATABASE_URI = 