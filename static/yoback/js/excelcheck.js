function gets() {
    $.ajax({
    url:'/yoback/upload',
    type:'GET', //GET
    /*data:{
        name:'yang',age:25
    },*/
    success:function(data,textStatus,jqXHR){
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    },
    error:function(xhr,textStatus){
        console.log('错误');
        console.log(xhr);
        console.log(textStatus);
    }
});
}

