/*
 * @Author        : uiuing
 * @Date          : 2021-05-14 17:26:22
 * @LastEditTime  : 2021-05-17 21:30:05
 * @LastEditors   : uiuing
 * @Description   : 交互
 * ©️ uiuing.com
 */

var baby;
var time_num = 0;
var isDisable = true;

$.ajaxSetup({
    async: false
});

function getBabyData() {
    var address = returnCitySN["cid"];
    if (address.length != 6) {
        address = String(Math.ceil(Math.random() * 8));
    }
    $.ajax({
        type: 'POST',
        dataType: 'text',
        url: 'http://404.uiuing.com/find/start_calculating',
        contentType: 'application/json; charset=utf-8',
        data: address,
        success: function (result) {
            baby = JSON.parse(result)
        },
        error: function () {
            alert('接口异常，请联系管理员！');
        },
    });
}


var Main = {
    methods: {
        msg_re() {
            if (!isDisable) {
                this.$message({
                    message: "后台的程序猿休息去啦～ 请待会再刷新吧～",
                    type: "warning"
                });
            }
            if (isDisable) {
                isDisable = false;
                this.fullscreenLoading = true;
                const loading = this.$loading({
                    lock: true,
                    text: '刷新中...',
                    spinner: 'el-icon-loading',
                    background: 'rgba(255, 255, 255, 0.7)'
                });
                remake();
                setTimeout(() => {
                    loading.close();
                }, 700);
                this.$message({
                    message: "刷新成功",
                    type: "success"
                });
            }
            setTimeout(() => {
                isDisable = true;
            }, 120000);
        },
    },
};

var Ctor = Vue.extend(Main);
new Ctor().$mount("#wrapper");

function check_autoplay() {
    var size = document.getElementById("move_icon").style.marginTop;
    if (size == "64px") {
        baby2();
        return;
    }
    if (size == "164px") {
        baby3();
        return;
    }
    if (size == "270px") {
        baby4();
        return;
    }
    if (size == "380px") {
        baby5();
        return;
    }
    if (size == "481px") {
        baby6();
        return;
    }
    if (size == "564px") {
        baby1();
        return;
    }
}

function autoplay_on() {
    setInterval(() => {
        time_num += 1;
        if (time_num == 6) {
            check_autoplay();
        }
    }, 1000);
}

function baby1() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(0);
    document.getElementById("baby1").style.background = "#82c8a0";
    document.getElementById("baby1").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "46px";
}

function baby2() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(1);
    document.getElementById("baby2").style.background = "#82c8a0";
    document.getElementById("baby2").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "100px";
}

function baby3() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(2);
    document.getElementById("baby3").style.background = "#82c8a0";
    document.getElementById("baby3").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "190px";
}

function baby4() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(3);
    document.getElementById("baby4").style.background = "#82c8a0";
    document.getElementById("baby4").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "270px";
}

function baby5() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(4);
    document.getElementById("baby5").style.background = "#82c8a0";
    document.getElementById("baby5").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "370px";
}

function baby6() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(5);
    document.getElementById("baby6").style.background = "#82c8a0";
    document.getElementById("baby6").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "405px";
}

function all_baby_image_remove() {
    document.getElementById("baby1").style.transform = "";
    document.getElementById("baby2").style.transform = "";
    document.getElementById("baby3").style.transform = "";
    document.getElementById("baby4").style.transform = "";
    document.getElementById("baby5").style.transform = "";
    document.getElementById("baby6").style.transform = "";
    document.getElementById("baby1").style.background = "#fff";
    document.getElementById("baby2").style.background = "#fff";
    document.getElementById("baby3").style.background = "#fff";
    document.getElementById("baby4").style.background = "#fff";
    document.getElementById("baby5").style.background = "#fff";
    document.getElementById("baby6").style.background = "#fff";
}

function set_infodata(index) {
    document.getElementById("baby_name").innerText = baby[index]['name'];
    document.getElementById("baby_sex").innerText = baby[index]['sex'];
    document.getElementById("baby_birth").innerText = baby[index]['birth'];
    document.getElementById("baby_missing_time").innerText = baby[index]['missing_time'];
    document.getElementById("baby_address").innerText = baby[index]['address'];
    document.getElementById("baby_person").innerText = baby[index]['person'];
    document.getElementById("baby_other").innerText = baby[index]['after'];
    document.getElementById("baby_callback").href = baby[index]['url'];
    document.getElementById("baby_img_vi").src = baby[index]['image'];
}

function setbaby_init() {
    document.getElementById("baby_name1").innerText = baby[0]['name'];
    document.getElementById("baby_name2").innerText = baby[1]['name'];
    document.getElementById("baby_name3").innerText = baby[2]['name'];
    document.getElementById("baby_name4").innerText = baby[3]['name'];
    document.getElementById("baby_name5").innerText = baby[4]['name'];
    document.getElementById("baby_name6").innerText = baby[5]['name'];
    document.getElementById("baby1").src = baby[0]['image'];
    document.getElementById("baby2").src = baby[1]['image'];
    document.getElementById("baby3").src = baby[2]['image'];
    document.getElementById("baby4").src = baby[3]['image'];
    document.getElementById("baby5").src = baby[4]['image'];
    document.getElementById("baby6").src = baby[5]['image'];
    for (var i = 0; i < 6; i++) {
        if (baby[i]['sex'] == "男") {
            var id = "baby_li" + (i + 1).toString();
            document.getElementById(id).setAttribute("class", "tooltip_m")
        }
        if (baby[i]['sex'] == "女") {
            var id = "baby_li" + (i + 1).toString();
            document.getElementById(id).setAttribute("class", "tooltip_w")
        }
    }
}


function remake() {
    getBabyData()
    setbaby_init();
    baby1();
    sessionStorage.setItem('baby_json', JSON.stringify(baby))
}

function on() {
    if (window.sessionStorage.getItem("baby_json")) {
        baby = JSON.parse(window.sessionStorage.getItem("baby_json"));
    } else {
        getBabyData();
        sessionStorage.setItem('baby_json', JSON.stringify(baby));
    }
    setbaby_init();
    baby1();
    autoplay_on();
}

on()