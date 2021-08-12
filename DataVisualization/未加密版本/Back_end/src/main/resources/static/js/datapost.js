$.ajaxSetup({
    async: false
});

function getBabyData() {
    var address = returnCitySN["cid"];
    if(address.length!=6){
        address=String(Math.ceil(Math.random()*8)); 
    }
    $.ajax({
        type: 'POST',
        dataType: 'text',
        url: '/find/start_calculating',
        contentType: 'application/json; charset=utf-8',
        data: address,
        success: function (result) {
            baby = JSON.parse(result)
        },
        error: function () {
            alert('接口异常，请联系管理员！001 cooluiu@qq.com');
        },
    });
}

function GetNum(){
    $.ajax({
        type: 'POST',
        dataType: 'text',
        url: '/GetDeveloper',
        success: function (result) {
            num = result;
        },
        error: function () {
            alert('接口异常，请联系管理员！002 cooluiu@qq.com');
        },
    });
}

function AddNum(){
    $.ajax({
        type: 'POST',
        url: '/AddDeveloper',
        error: function () {
            alert('接口异常，请联系管理员！003 cooluiu@qq.com');
        },
    });
}


