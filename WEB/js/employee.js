function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie() {
  document.cookie = 'staff id=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;'
  document.cookie = 'position=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;'
  document.cookie = 'user id=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;'
  document.cookie = 'sex=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;'
}

function logout(){
    window.location.href = 'index.html'
    eraseCookie()
    
}

var staff_id = "http://127.0.0.1:5000/getProfil/"+getCookie("staff id")
var history_leave = "http://127.0.0.1:5000/getLeave_history/"+getCookie("staff id")

$.ajax({
    url: staff_id,
    method: "GET",
        
    success: function (profil) {
            
        console.log(profil.joined_date)
        var employeePage_staff_name = profil.staff_name
        var employeePage_staff_id = profil. staff_id
        var manager =
            `
            <a class="dropdown-item" href="employeePage.html">Employee</a>
            <a class="dropdown-item" href="managerPage.html">Manager</a>
            <div class="dropdown-divider"></div>
            `
        var employee =
            `
            <a class="dropdown-item" href="#">Employee</a>
            <div class="dropdown-divider"></div>
            `

        $('#employeePage_staff_name').append(employeePage_staff_name)
        $('#employeePage_staff_id').append(employeePage_staff_id)
        if ((getCookie("position") == "Manager") || (getCookie("position") == "Direktur")){
            $('#user_akses').append(manager)
          } else {
            $('#user_akses').append(employee)
          }
            
            
    },
    error: function (error) {
        //error handling

    },
    complete: function () {

    }
})

function getProfil(){
    
    $.ajax({
        url: staff_id,
        method: "GET",
        
        
        success: function (profil) {
            $('#get_profil').empty()
            // console.log(profil.joined_date)
            var profilInfo =
                    `
                    <form class="form-horizontal" action="/examples/actions/confirmation.php" method="post" >
                        <div class="form-group" style="display:flex; margin-top: 30px; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Staff ID</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.staff_id}</li>
                        </div>
                        
                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">User ID</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.user_id}</li>
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Staff Name</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.staff_name}</li>
                                
                        </div>
                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Email</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.email}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Password</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.password}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Supervisor User ID</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.supervisor_user_id}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Gender</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.sex}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Division </label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.division}</li>       
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Unit Code</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.unit_code}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Location</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.location}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Staff position</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.position}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Joined Date</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.joined_date}</li>            
                        </div>

                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Balance</label>
                            <li class="list-group-item d-flex flex-row align-items-center"  style="width:800px;">${profil.balance}</li> 
                        </div>
                    </form>
                    `
                
            
            $('#get_profil').append(profilInfo)
            
            
        },
        error: function (error) {
            //error handling

        },
        complete: function () {

        }
    })
}

function getHistory(){
    
    $.ajax({
        url: history_leave,
        method: "GET",
       
        success: function (history) {
            $('#get_profil').empty()
            for (var i = 0; i < history.length; i++) {
                if (history[i].approval_status == "0"){
                    approval_status="Rejected"
                } else if (history[i].approval_status == "1"){
                    approval_status="Approve"
                } else if (history[i].approval_status == null){
                    approval_status=null
                }
                var historyInfo =
                    `
                    <li class="list-group-item align-items-center"  style="width:1010px; justify-content: space-between; margin: 20px;">
                        <h4 class="panel-title">
                            <h5>Date       : ${history[i].submission_date}</h5>
                            <h5>Leave Type : ${history[i].leave_type}</h5>
                            <a data-toggle="collapse" href="#collapse-${i}" style="text-decoration:none; color: gray;">Detail</a>
                        </h4>
                    </li>
                    <div class="panel-collapse collapse" id="collapse-${i}">
                        <form class="shadow-lg p-3 m-3 bg-white rounded">
                            <form class="form-horizontal" action="/examples/actions/confirmation.php" method="post">
                                <div class="form-group" style="display:flex; margin-top: 30px; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Staff ID</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].staff_id}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Supervisor User ID</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].supervisor_user_id}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Leave Type</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].leave_type}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Start Date</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:300px;">${history[i].start_date}</li>
                                    <label class="control-label col-xs-2" style="margin:13px;">Start Date Length</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:300px;">${history[i].start_date_length}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">End Date</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:300px;">${history[i].end_date}</li>
                                    <label class="control-label col-xs-2" style="margin:13px;">End Date Length</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:300px;">${history[i].end_date_length}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Number of Leave Days</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].number_of_leave_days}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Requestor Remarks</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].requestor_remarks}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Submission Date</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].submission_date}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Approval Status</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${approval_status}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Approval Remarks</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].approval_remarks}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Approval Date</label>
                                    <li class="list-group-item d-flex flex-row align-items-center"  style="width:700px;">${history[i].approval_date}</li>
                                </div>
                            </form>
                        </form>
                    </div>
                    `
                
            
                $('#get_profil').append(historyInfo)
            }
            
        },
        error: function (error) {
            //error handling

        },
        complete: function () {

        }
    })
}

function getAllLeaveType(){
    $.ajax({
        url: "http://127.0.0.1:5000/getAllLeave",
        method: "GET",
            
        success: function (leaves) {
            $('#leave_type_options').empty()
            // console.table(leaves)
            for (var i = 0; i < leaves.length; i++) {
                if (leaves[i].sex == getCookie("sex") || leaves[i].sex == null){
                    var leavetype =
                        `
                        <option id=leave_option_${i} value="${leaves[i].leave_name}">${leaves[i].leave_name}</option>
                        `
                    $('#leave_type_options').append(leavetype)
                }
            }
        },
        error: function (error) {},
        complete: function () {}
    })
}
function submit_leave_request(){
    var leave_type_ = document.getElementById("leave_type_options")
    var leave_type_selected = leave_type_.options[leave_type_.selectedIndex].value;
    console.log(leave_type_selected)
    var today = new Date()
    var current_date_getTime= new Date(today.getFullYear(), today.getMonth(), today.getDay(),7).getTime()
    console.log(current_date_getTime)
    var start_date = document.getElementById("start_date").value
    var start_date_getTime = new Date(start_date).getTime()
    console.log(start_date)
    console.log(start_date)
    var start_date_length = document.getElementById("start_date_Length")
    var start_date_length_selected = start_date_length.options[start_date_length.selectedIndex].value;
    console.log(start_date_length_selected)

    var end_date = document.getElementById("end_date").value
    var end_date_getTime = new Date(end_date).getTime()
    console.log(end_date)
    var end_date_length = document.getElementById("end_date_length")
    var end_date_length_selected = end_date_length.options[end_date_length.selectedIndex].value;
    console.log(end_date_length_selected)


    var requestor_remarks = $('input#requestor_remarks').val()
    console.log(requestor_remarks)
    console.log(current_date_getTime)
    console.log('ads')
    console.log(start_date_getTime)
    console.log(end_date)
    console.log(end_date_getTime)
    if (start_date == '' && end_date == ''){
        alert("start date and end date is empty")
    } else if (end_date == '') {
        alert("end date is empty")
    } else if (start_date == '') {
        alert("start date is empty")
    }else if (requestor_remarks == '') {
        alert("requestor_remarks is empty")
    } else if (start_date_getTime > end_date_getTime) {
        alert("End Date must after Start Date")
    } else if (current_date_getTime > start_date_getTime) {
        alert("Start Date must start at current Date")
    } else{
        $.ajax({
            url: 'http://127.0.0.1:5000/createdLeaveRequest',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                user_id : getCookie("user id"),
                leave_type : leave_type_selected,
                start_date : start_date.toString(),
                start_date_length : start_date_length_selected,
                end_date : end_date.toString(),
                end_date_length : end_date_length_selected,
                requestor_remarks : requestor_remarks
            }),

            success: function (response) {
                alert("Berhasil mengajukan cuti.") //400
                // getHistory()
            },
            error: function (error) {},
            complete: function () {}
        })
    }
    
}
function leaveRequest(){
    $.ajax({
        url: staff_id,
        method: "GET",
       
        success: function (profil) {
            $('#get_profil').empty()
            var leaveRequestInfo =
                `
                <div class="container">
                    <form class="shadow-lg p-3 m-3 bg-white rounded">
                    <h3>Leave Request</h3>
                    </form>
                </div>
                <div class="container">
                    <form class="shadow-lg p-3 m-3 bg-white rounded">
                        <div class="row">
                            <div class="col">
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin-left: 50px;margin-right: 68px;">Name</label>
                                    <li type="text" class="form-control" id="usr">${profil.staff_name}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin-left: 50px;margin-right: 36px;">Supervisor</label>
                                    <li type="text" class="form-control" id="usr">${profil.supervisor_user_id}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin: 0px 50px;">Location</label>
                                    <li type="text" class="form-control" id="usr">${profil.location}</li>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin-left: 50px;margin-right: 62px; width: 80px;">Staff ID</label>
                                    <li type="text" class="form-control" id="usr">${profil.staff_id}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin-left: 50px;margin-right: 78px;">Email</label>
                                    <li type="text" class="form-control" id="usr">${profil.email}</li>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin: 0px 50px; width: 100px;">Join Date</label>
                                    <li type="text" class="form-control" id="usr">${profil.joined_date}</li>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="container">
                    <form class="shadow-lg p-3 m-3 bg-white rounded">
                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label for="sel1" class="control-label col-xs-2" style="margin: 0px 50px;">Leave Type</label>
                            <select class="form-control" id="leave_type_options">
                                
                            </select>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin: 0px 50px;">Start Date</label>
                                    <input class="form-control" type="date" name="start_date_name" id="start_date">
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label for="sel2" class="control-label col-xs-2" style="margin: 0px 50px;">Start Date Length</label>
                                    <select class="form-control" id="start_date_Length">
                                        <option value=0.25>0.25</option>
                                        <option value=0.5>0.5</option>
                                        <option value=1>1</option>
                                    </select>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin: 0px 50px;">End Date</label>
                                    <input class="form-control" type="date" name="end_date_name" id="end_date">
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label for="sel3" class="control-label col-xs-2" style="margin: 0px 50px;">End Date Length</label>
                                    <select class="form-control" id="end_date_length">
                                        <option value=0.25>0.25</option>
                                        <option value=0.5>0.5</option>
                                        <option value=1>1</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="form-group" style="display:flex; justify-content: space-between;">
                            <label class="control-label col-xs-2" style="margin: 0px 50px;">Requestor Remarks</label>
                            <input type="text" class="form-control" id="requestor_remarks">
                        </div>
                        <a class="btn btn-success" onclick="submit_leave_request()">Submit</a>        
                    </form>
                </div>   
                `         
            $('#get_profil').append(leaveRequestInfo)
            getAllLeaveType()
        },
        error: function (error) {},
        complete: function () {}
    })
}

function login() {

    var username = $('input#username-form').val()
    var password = $('input#password-form').val()

    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            user_id: username,
            password: password
        }),

        success: function (response) {
            alert("Sign In "+username+" berhasil") //400
            setCookie("staff id",response.staff_id,1)
            setCookie("position",response.position,1)
            setCookie("sex",response.sex,1)
            console.log(response.staff_id)
            console.log(response.position)
            var x = document.cookie;
            var y = getCookie("staff id")
            window.location.href = 'employeePage.html'
        },
        error: function (error) {},
        complete: function () {}
    })
}
