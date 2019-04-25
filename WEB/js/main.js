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
            setCookie("user id",response.user_id,1)
            setCookie("position",response.position,1)
            setCookie("sex",response.sex,1)
            console.log(response.staff_id)
            console.log(response.position)
            var x = document.cookie;
            var y = getCookie("staff id")
            window.location.href = 'employeePage.html'
        },
        error: function (error) {
            alert("User or password is not found") //400
        },
        complete: function () {
            

        }
    })
}



// cookies
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
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


