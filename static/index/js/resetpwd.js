    var baseUrl = 'http://127.0.0.1:8000/';
    var verification=document.getElementById("verification"),
        newPwd=document.getElementById("newPwd"),
        newConfirm=document.getElementById("newConfirm"),
        errInfo=document.getElementById("error");
    function errorInfo(ht) {
        errInfo.innerHTML=ht;
    }
    function sub() {
        if (!verification.value){
            errorInfo('请填写验证码！');
            return;
        }
        if (!newPwd.value){
            errorInfo('请填写密码！');
            return;
        }
        if (!newConfirm.value){
            errorInfo('请填写确认密码！');
            return;
        }
        if (newPwd.value!==newConfirm.value){
            errorInfo('2次输入的密码不一致，请重新输入！');
            return;
        }
        $.ajax({
            url: baseUrl + 'profile/resetpwd/',
            type: 'POST',
            data: {
                code: verification.value,
                passwd: newPwd.value,
                timeflag: '' +  Math.floor(new Date().getTime() / 1000)
            },
            success: function(data) {
                console.log(data);
            },
            error: function(xhr, textStatus) {
                alert('加载失败，请稍后再试！');
                console.log(xhr);
                console.log(textStatus);
            }
        });
    }