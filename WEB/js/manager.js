var history_leave_request = "http://127.0.0.1:5000/getLeave_request/"+getCookie("staff id")
function LeaveRequestList(){
    
    $.ajax({
        url: history_leave_request,
        method: "GET",
       
        success: function (history) {
            $('#get_profil').empty()
            for (var i = 0; i < history.length; i++) {
                if (history[i].approval_status==null){
                    var historyInfo =
                    `
                    <li class="list-group-item align-items-center"  style="width:1010px; justify-content: space-between; margin: 20px;">
                        <h4 class="panel-title">
                            <h6>Date       : ${history[i].submission_date}</h6>
                            <h6>Leave Type : ${history[i].leave_type}</h6>
                            <a data-toggle="collapse" href="#collapse-${i}" style="text-decoration:none; color: gray;">Detail</a>
                        </h4>
                    </li>
                    <div class="panel-collapse collapse" id="collapse-${i}">
                        <form class="shadow-lg p-3 m-3 bg-white rounded">
                            <form class="form-horizontal" action="/examples/actions/confirmation.php" method="post">
                                <div class="form-group" style="display:flex; margin-top: 30px; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin:13px; margin-left:50px;">Leave ID</label>
                                    <li class="list-group-item d-flex flex-row align-items-center" style="width:700px;">${history[i].leave_id}</li>
                                </div>
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
                                    <label for="sel3" class="control-label col-xs-2" style="margin: 0px 50px;">Approval Status</label>
                                    <select class="form-control" id="approval_option">
                                        <option value=1>Approve</option>
                                        <option value=0>Reject</option>
                                    </select>
                                </div>
                                <div class="form-group" style="display:flex; justify-content: space-between;">
                                    <label class="control-label col-xs-2" style="margin: 0px 50px;">Approval Remarks</label>
                                    <input type="text" class="form-control" id="approval_remarks">
                                </div>
                                <a class="btn btn-success" onclick="submit_leave_request(${history[i].leave_id})">Submit</a> 
                            </form>
                        </form>
                    </div>
                    `
                }
            
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

function submit_leave_request(leave_id_){
    var approveLeaveRequest = "http://127.0.0.1:5000/approveLeaveRequest/"+leave_id_
    console.log(approveLeaveRequest)
    var approval_status = document.getElementById("approval_option")
    var approval_selected = approval_status.options[approval_status.selectedIndex].value;
    var approval_remarks = $('input#approval_remarks').val()
    console.log(approval_remarks)
    if (approval_remarks == null) {
        console.log("requestor_remarks is empty")
    } else{
        $.ajax({
            url: approveLeaveRequest,
            method: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify({
                approval_status : approval_selected,
                approval_remarks : approval_remarks
            }),

            success: function (response) {
                alert("Proses Approval Cuti Berhasil") //400
                LeaveRequestList()
            },
            error: function (error) {},
            complete: function () {}
        })
    }
    
}