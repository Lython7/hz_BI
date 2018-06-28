navIndex(2);


ajax('GET','profile/',null,function (res) {
    var data = JSON.parse(res);
    var oUser = document.getElementById("username"),
        oTel = document.getElementById("tel"),
        oPost = document.getElementById("position"),
        oStatus = document.getElementById("status");
    oUser.innerHTML=data.uname;
    oTel.innerHTML=data.ucellphone;
    oPost.innerHTML=data.uposition;
    oStatus.innerHTML=data.ustatus;
});