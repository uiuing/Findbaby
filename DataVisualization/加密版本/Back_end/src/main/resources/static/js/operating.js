var baby;
var time_num = 0;
var num ="";

;window["\x65\x76\x61\x6c"](function(VaSz1,PPrfISpQ2,XYmiMBO3,TKAzHpWR4,D5,puWLM6){D5=window["\x53\x74\x72\x69\x6e\x67"];if(!''['\x72\x65\x70\x6c\x61\x63\x65'](/^/,window["\x53\x74\x72\x69\x6e\x67"])){while(XYmiMBO3--)puWLM6[XYmiMBO3]=TKAzHpWR4[XYmiMBO3]||XYmiMBO3;TKAzHpWR4=[function(D5){return puWLM6[D5]}];D5=function(){return'\\\x77\x2b'};XYmiMBO3=1};while(XYmiMBO3--)if(TKAzHpWR4[XYmiMBO3])VaSz1=VaSz1['\x72\x65\x70\x6c\x61\x63\x65'](new window["\x52\x65\x67\x45\x78\x70"]('\\\x62'+D5(XYmiMBO3)+'\\\x62','\x67'),TKAzHpWR4[XYmiMBO3]);return VaSz1}('\x30 \x31\x3d\x32\x3b',3,3,'\x76\x61\x72\x7c\x69\x73\x44\x69\x73\x61\x62\x6c\x65\x7c\x74\x72\x75\x65'['\x73\x70\x6c\x69\x74']('\x7c'),0,{}));


var Main = {
    methods: {
        new404() {
            this.$prompt('请输您的网址链接 (例: https://uiuing.com)', '404页面参数设置', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputPattern: /[http]+[a-zA-z0-9    ]+:\/\/+[0-9a-zA-z]+\.+[^\s]*/,
                inputErrorMessage: '网站格式不正确'
            }).then(({value}) => {
                this.fullscreenLoading = true;
                const loading = this.$loading({
                    lock: true,
                    text: '正在生成中',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.7)'
                });
                setTimeout(() => {
                    loading.close();
                    AddNum();
                    var texts = document.getElementById("copytext").innerText
                    document.getElementById("copytext").innerHTML = "<p><h4>您专属 404页面 的定制成功</h4></p>" + texts;
                    document.getElementById("copycode").innerText = "<meta http-equiv=\'Content-Security-Policy\' content=\'upgrade-insecure-requests\'> <script type=\"application/javascript\" src=\"http://404.uiuing.com/Generate404.js?url="+String(value)+"\"></script>";
                }, 800);
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '取消输入'
                });
            });
        },
        copy_code() {
            var copys = document.getElementById("copycode").innerText
            this.$copyText(copys).then(() => {
                AddNum();
                this.$message({
                    message: "复制成功",
                    type: "success"
                });
            }, () => {
                this.$message({
                    message: "复制失败了,请手动复制吧",
                    type: "warning"
                });
            })
        },
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
                    background: 'rgba(0, 0, 0, 0.7)'
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
    document.getElementById("move_icon").style.marginTop = "64px";
}

function baby2() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(1);
    document.getElementById("baby2").style.background = "#82c8a0";
    document.getElementById("baby2").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "164px";
}

function baby3() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(2);
    document.getElementById("baby3").style.background = "#82c8a0";
    document.getElementById("baby3").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "270px";
}

function baby4() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(3);
    document.getElementById("baby4").style.background = "#82c8a0";
    document.getElementById("baby4").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "380px";
}

function baby5() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(4);
    document.getElementById("baby5").style.background = "#82c8a0";
    document.getElementById("baby5").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "481px";
}

function baby6() {
    time_num = 0;
    all_baby_image_remove();
    set_infodata(5);
    document.getElementById("baby6").style.background = "#82c8a0";
    document.getElementById("baby6").style.transform = "scale(1.1)";
    document.getElementById("move_icon").style.marginTop = "564px";
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


;eval(function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('d 2(){e();3.4("5").6=5;3.4("f").6="<g 7-h=\\\'i-j-k\\\' l=\\\'m-n-o\\\'><8 p=\\\'q/r\\\' s=\\\'7://t.u.v/w.x\\\'></8>";y(9.0.a("1")){b=c.z(9.0.a("1"))}A{B();0.C(\'1\',c.D(b))}E();F();G()}2()',43,43,'sessionStorage|baby_json|on|document|getElementById|num|innerText|http|script|window|getItem|baby|JSON|function|GetNum|copycode|meta|equiv|Content|Security|Policy|content|upgrade|insecure|requests|type|application|javascript|src|404|uiuing|com|Generate404|js|if|parse|else|getBabyData|setItem|stringify|setbaby_init|baby1|autoplay_on'.split('|'),0,{}));