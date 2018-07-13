var index = sessionStorage.tabIndex || 0;
navIndex(index);
var baseUrls='http://10.10.10.100:8000/score/';


$('#myCarousel').carousel({
	interval: 2000
});

$(function() {
	$('#myTab li:eq(0) a').tab('show');
});

var myDate = new Date();
myDate = myDate.getDate();
var i = parseInt(myDate / 30 * 100);
var content = "恭喜完成任务！！！"

var a_1 = 24777 / 100000 * 100;
if(a_1 >= 100) {
	$("#barOne").width(100 + "%");
	$("#barOne").css("background-color", 'yellow');
	$("#barOne").html(content).css('color', 'black');
	$("#barOneOne").css('display', 'none');
} else {
	$("#barOne").width(i + "%");
	$("#barOneOne").animate({
		left: a_1 + "%"
	});
}

var a_2 = 3045 / 100000 * 100;
if(a_2 >= 100) {
	$("#barTwo").width(100 + "%");
	$("#barTwo").css("background-color", 'yellow');
	$("#barTwo").html(content).css('color', 'black');
	$("#barTwoTwo").css('display', 'none');
} else {
	$("#barTwo").width(i + "%");
	$("#barTwoTwo").animate({
		left: a_2 + "%"
	});
}

var a_3 = 2919 / 100000 * 100;
if(a_3 >= 100) {
	$("#barThree").width(100 + "%");
	$("#barThree").css("background-color", 'yellow');
	$("#barThree").html(content).css('color', 'black');
	$("#barThreeThree").css('display', 'none');
} else {
	$("#barThree").width(i + "%");
	$("#barThreeThree").animate({
		left: a_3 + "%"
	});
}

var a_4 = 1566 / 100000 * 100;
if(a_4 >= 100) {
	$("#barFour").width(100 + "%");
	$("#barFour").css("background-color", 'yellow');
	$("#barFour").html(content).css('color', 'black');
	$("#barFourFour").css('display', 'none');
} else {
	$("#barFour").width(i + "%");
	$("#barFourFour").animate({
		left: a_4 + "%"
	});
}

var a_5 = 523 / 100000 * 100;
if(a_5 >= 100) {
	$("#barFive").width(100 + "%");
	$("#barFive").css("background-color", 'yellow');
	$("#barFive").html(content).css('color', 'black');
	$("#barFiveFive").css('display', 'none');
} else {
	$("#barFive").width(i + "%");
	$("#barFiveFive").animate({
		left: a_5 + "%"
	});
}

var a_6 = 0 / 100000 * 100;
if(a_6 >= 100) {
	$("#barSix").width(100 + "%");
	$("#barSix").css("background-color", 'yellow');
	$("#barSix").html(content).css('color', 'black');
	$("#barSixSix").css('display', 'none');
} else {
	$("#barSix").width(i + "%");
	$("#barSixSix").animate({
		left: a_6 + "%"
	});
}

var a_7 = 0 / 100000 * 100;
if(a_7 >= 100) {
	$("#barSeven").width(100 + "%");
	$("#barSeven").css("background-color", 'yellow');
	$("#barSeven").html(content).css('color', 'black');
	$("#barSevenSeven").css('display', 'none');
} else {
	$("#barSeven").width(i + "%");
	$("#barSevenSeven").animate({
		left: a_7 + "%"
	});
}

/*历史数据及请求ajax*/
var hisDatas = {
	'2017-11': [{
		'no': 1.0,
		'name': '苏朝阳',
		'count': 35.0,
		'sum': 44336.0
	}, {
		'no': 2.0,
		'name': '陈登凯',
		'count': 57.0,
		'sum': 30744.0
	}, {
		'no': 3.0,
		'name': '张伟',
		'count': 27.0,
		'sum': 30694.0
	}, {
		'no': 4.0,
		'name': '石可心',
		'count': 8.0,
		'sum': 8868.0
	}, {
		'no': 5.0,
		'name': '刘来僧',
		'count': 12.0,
		'sum': 7002.0
	}, {
		'no': 6.0,
		'name': '陶钰',
		'count': 12.0,
		'sum': 6278.0
	}, {
		'no': 7.0,
		'name': '蔡志涛',
		'count': 9.0,
		'sum': 4998.0
	}, {
		'no': 8.0,
		'name': '赵辉',
		'count': 9.0,
		'sum': 4854.0
	}, {
		'no': 9.0,
		'name': '王珍',
		'count': 2.0,
		'sum': 3617.0
	}, {
		'no': 10.0,
		'name': '何志强',
		'count': 2.0,
		'sum': 1499.46
	}, {
		'no': 11.0,
		'name': '王文杰',
		'count': 2.0,
		'sum': 2202.0
	}, {
		'no': 12.0,
		'name': '郭宇',
		'count': 4.0,
		'sum': 1989.0
	}, {
		'no': 13.0,
		'name': '李雪飞',
		'count': 2.0,
		'sum': 1647.0
	}, {
		'no': 14.0,
		'name': '刘仁鹏',
		'count': 2.0,
		'sum': 1110.0
	}, {
		'no': 15.0,
		'name': '田志浩',
		'count': 2.0,
		'sum': 1062.0
	}, {
		'no': 16.0,
		'name': '张振',
		'count': 2.0,
		'sum': 1036.0
	}],
	'2017-12': [{
		'no': 1.0,
		'name': '张伟',
		'count': 87.0,
		'sum': 71228.47
	}, {
		'no': 2.0,
		'name': '陈京兴',
		'count': 103.0,
		'sum': 61307.23
	}, {
		'no': 3.0,
		'name': '苏朝阳',
		'count': 48.0,
		'sum': 41579.72
	}, {
		'no': 4.0,
		'name': '李雪飞',
		'count': 27.0,
		'sum': 16446.37
	}, {
		'no': 5.0,
		'name': '刘来僧',
		'count': 16.0,
		'sum': 13266.37
	}, {
		'no': 6.0,
		'name': '孙冬',
		'count': 10.0,
		'sum': 5128.29
	}, {
		'no': 7.0,
		'name': '蔡志涛',
		'count': 5.0,
		'sum': 3700.66
	}, {
		'no': 8.0,
		'name': '陶钰',
		'count': 5.0,
		'sum': 2810.56
	}, {
		'no': 9.0,
		'name': '赵辉',
		'count': 3.0,
		'sum': 1725.98
	}, {
		'no': 10.0,
		'name': '石可心',
		'count': 2.0,
		'sum': 1668.71
	}, {
		'no': 11.0,
		'name': '王文杰',
		'count': 3.0,
		'sum': 1529.45
	}, {
		'no': 12.0,
		'name': '张振',
		'count': 2.0,
		'sum': 1165.0
	}, {
		'no': 13.0,
		'name': '刘仁鹏',
		'count': 2.0,
		'sum': 1115.76
	}, {
		'no': 14.0,
		'name': '何英',
		'count': 1.0,
		'sum': 940.92
	}, {
		'no': 15.0,
		'name': '何志强',
		'count': 1.0,
		'sum': 638.81
	}, {
		'no': 16.0,
		'name': '张博\xa0',
		'count': 0.0,
		'sum': 0.0
	}, {
		'no': 17.0,
		'name': '张金勇',
		'count': 0.0,
		'sum': 0.0
	}],
	'2018-01': [{
		'no': 1.0,
		'name': '陈京兴',
		'count': 58.0,
		'sum': 91694.37
	}, {
		'no': 2.0,
		'name': '张博',
		'count': 100.0,
		'sum': 84684.13
	}, {
		'no': 3.0,
		'name': '苏朝阳',
		'count': 53.0,
		'sum': 46797.42
	}, {
		'no': 4.0,
		'name': '张金勇',
		'count': 52.0,
		'sum': 45430.76
	}, {
		'no': 5.0,
		'name': '张伟',
		'count': 49.0,
		'sum': 42062.38
	}, {
		'no': 6.0,
		'name': '柳杰',
		'count': 26.0,
		'sum': 28908.6712
	}, {
		'no': 7.0,
		'name': '孙冬',
		'count': 30.0,
		'sum': 21683.29
	}, {
		'no': 8.0,
		'name': '秦亮',
		'count': 21.0,
		'sum': 18496.0
	}, {
		'no': 9.0,
		'name': '陶钰',
		'count': 7.0,
		'sum': 4962.53
	}, {
		'no': 10.0,
		'name': '蔡志涛',
		'count': 3.0,
		'sum': 3278.95
	}],
	'2018-02': [{
		'no': 1.0,
		'name': '柳杰',
		'count': 134.0,
		'sum': 84541.98
	}, {
		'no': 2.0,
		'name': '张伟',
		'count': 5.0,
		'sum': 4166.97
	}, {
		'no': 3.0,
		'name': '蔡志涛',
		'count': 5.0,
		'sum': 3651.83
	}, {
		'no': 4.0,
		'name': '张博',
		'count': 5.0,
		'sum': 3326.25
	}, {
		'no': 5.0,
		'name': '苏朝阳',
		'count': 2.0,
		'sum': 2240.52
	}, {
		'no': 6.0,
		'name': '陶钰',
		'count': 2.0,
		'sum': 1725.0
	}, {
		'no': 7.0,
		'name': '张金勇',
		'count': 2.0,
		'sum': 1565.58
	}, {
		'no': 8.0,
		'name': '孙冬',
		'count': 1.0,
		'sum': 565.0
	}, {
		'no': 9.0,
		'name': '秦亮',
		'count': 0.0,
		'sum': 0.0
	}]
}

var selY = document.getElementById("datesYear"),
	selM = document.getElementById("datesMonth"),
	oBtn = document.getElementById("dateBtn"),
	oSho = document.getElementById("conDateShow");
/*now日期数据*/
var nowY = new Date().getFullYear(),
	nowM = new Date().getMonth() + 1;
for(var i = 2017; i <= nowY; i++) {
	selY.innerHTML += '<option value="' + i + '">' + i + '</option>';
}
selY.value = nowY;
for(var i = 1; i <= nowM; i++) {
	selM.innerHTML += '<option value="' + i + '">' + i + '</option>';
}
selM.value = nowM;

function resetMonth(min, max) {
	selM.innerHTML = '';
	for(var i = min; i <= max; i++) {
		selM.innerHTML += '<option value="' + i + '">' + i + '</option>';
	}
}
selY.onchange = function() {
	var tem = selM.value;
	if(parseInt(selY.value) < nowY && parseInt(selY.value) > 2017) {
		resetMonth(1, 12);
	} else if(parseInt(selY.value) == 2017) {
		resetMonth(11, 12);
	} else {
		resetMonth(1, nowM);
	}
}
var oTbody = document.getElementById("contentData"),
	oList = document.getElementById("panel_body");

function sortList(data) {

	var tem = '',
		tem2 = '',
		num = 1,
		sumCount = 0,
		sumSum = 0;
	/*红色日期占月份的进度*/
	var jd = (nowY == selY.value && nowM == selM.value) ? (new Date().getDate()) * 100 / calcDays(nowY, (nowM - 1)) : 100;
	var len = data.length;
	for(var i = 0; i < len; i++) {
		tem += '<tr><td>' + (i + 1) + '</td><td>' + data[i].name + '</td><td>' + data[i].count + '</td><td>' + Math.round(data[i].sum * 1) + '</td></tr>';
		sumCount += (data[i].count * 1);
		sumSum += Math.round(data[i].sum * 1);
		tem2 += '<div class="row"><div class="col-xs-3"><h5>' + data[i].name + '</h5></div><div class="col-xs-9" style="padding-top:3%;"><div class="progress progress-striped" style="position:relative;overflow:visible;"><img id="barOneOne" src="/static/index/images/6.png" alt="" style="position:absolute;top:-50%;left:' + ((Math.round(data[i].sum * 1) / 1000) > 100 ? 100 : (Math.round(data[i].sum * 1) / 1000)) + '%;" /><span id="barOne" class="progress-bar progress-bar-danger" style="width: ' + jd + '%;"></span></div></div></div>'
	}
	tem += '<tr class="final"><td>总计</td><td>-</td><td>' + sumCount + '</td><td>' + sumSum + '</td></tr>';
	oTbody.innerHTML = tem;
	oList.innerHTML = tem2;
}
/*初始化请求月份数据*/
monthData(nowY, nowM);

function monthData(nowY, nowM) {
	oSho.innerHTML = '(' + nowY + '-' + nowM + ')';
	var jd = (nowY == new Date().getFullYear() && nowM == new Date().getMonth() + 1) ? (new Date().getDate()) * 100 / calcDays(nowY, (nowM - 1)) : 100;
	if(nowY > 2018 || (nowY == 2018 && nowM > 2)) {
		var m = ((nowM + '').length == 1) ? ('/0' + nowM) : nowM;
		var url_ = baseUrls + nowY + m;
		ajaxDatas(url_, sortList);
	} else {
		var m = ((nowM + '').length == 1) ? ('0' + nowM) : nowM;
		var key_ = nowY + '-' + m;
		var data = hisDatas[key_];
		var tem = '',
			tem2 = '',
			sumCount = 0,
			sumSum = 0;
		for(var i in data) {
			tem += '<tr><td>' + data[i].no + '</td><td>' + data[i].name + '</td><td>' + data[i].count + '</td><td>' + Math.round(data[i].sum * 1) + '</td></tr>';
			sumCount += (data[i].count * 1);
			sumSum += Math.round(data[i].sum * 1);
			tem2 += '<div class="row"><div class="col-xs-3"><h5>' + data[i].name + '</h5></div><div class="col-xs-9" style="padding-top:3%;"><div class="progress progress-striped" style="position:relative;overflow:visible;"><img id="barOneOne" src="img/6.png" alt="" style="position:absolute;top:-50%;left:' + Math.round(data[i].sum * 1) / 1000 + '%;" /><span id="barOne" class="progress-bar progress-bar-danger" style="width: ' + jd + '%;"></span></div></div></div>'
		}
		tem += '<tr class="final"><td>总计</td><td>-</td><td>' + sumCount + '</td><td>' + sumSum + '</td></tr>';
		oTbody.innerHTML = tem;
		oList.innerHTML = tem2;
	}
}

oBtn.onclick = function() {
	var Y = selY.value,
		M = selM.value;
	monthData(Y, M);
}

function ajaxDatas(url_, callback) {
	$.ajax({
		url: url_,
		type: 'GET',
		success: function(data, textStatus, jqXHR) {
			callback(data);
		},
		error: function(xhr, textStatus) {
			console.log('错误');
			console.log(xhr);
			console.log(textStatus);
		}
	});
}
/*当月的天数*/
function calcDays(year, month) {
	if(month == 1) {
		if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0 && year % 4000 != 0)) {
			return 29;
		} else {
			return 28;
		}
	} else {
		if(month == 3 || month == 5 || month == 8 || month == 10) {
			return 30;
		} else {
			return 31;
		}
	}
}