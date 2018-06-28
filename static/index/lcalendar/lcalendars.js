function chooseCreate(callback) {
    var data = [{
				name: '今天',
				value: 1
			},
			{
				name: '昨天',
				value: 2
			},
			{
				name: '本周',
				value: 3
			},
			{
				name: '上周',
				value: 4
			},
			{
				name: '本月',
				value: 5
			},
			{
				name: '上月',
				value: 6
			}
		];
	document.body.style.position = 'fixed';
	var oBox = document.createElement('div');
	oBox.className = 'choose-box';
	var str = '<div class="choose-data"><ul>';
	for(var i = 0; i < data.length; i++) {
		str += '<li data-value="' + data[i].value + '">' + data[i].name + '</li>'
	}
	str += '</ul><div id="defined-time" class="defined-time">自定义</div><div class="cancel-btn">取消</div></div>';
	oBox.innerHTML = str;
	document.body.appendChild(oBox);
	var oChoose = document.getElementsByClassName('choose-box')[0];
	var aLi = oChoose.getElementsByTagName('li'),
		oCancel = oChoose.getElementsByClassName('cancel-btn')[0];
	var oDefined = document.getElementById("defined-time");
	for(var i = 0; i < aLi.length; i++) {
		aLi[i].onclick = function() {
			removeChoose();
			var val=parseInt(this.getAttribute('data-value'));
			var dates;
			var con=this.innerHTML;
			switch (val){
                case 1:
                    dates=thisDate();
                    break;
                case 2:
                    dates=yesterday();
                    break;
                case 3:
                    dates=thisWeekDate();
                    break;
                case 4:
                    dates=lastWeekDate();
                    break;
                case 5:
                    dates=thisMonthDate();
                    break;
                case 6:
                    dates=lastMonthDate();
                    break;
            }
			callback(con,dates);
		}
	}
	oDefined.onclick = function() {
	    var con=this.innerHTML;
		removeChoose();
		defineddates(con,callback);
	}
	oCancel.onclick = removeChoose;

	function removeChoose() {
		document.body.removeChild(oChoose);
		document.body.style.position = 'static';
	}
	/*自定义日期选择*/
	function defineddates(con,callback) {
		var dates = document.createElement('div');
		document.body.appendChild(dates);
		document.body.style.position = 'fixed';
		dates.id = 'definedBox';
		var ht = '<div class="select_date">';
		ht += '<div class="date_tit">开始时间</div>';
		ht += '<div class="date_right"><input type="text" id="start_date" placeholder="选择开始日期" readonly="readonly" /></div></div>';
		ht += '<div class="select_date"><div class="date_tit">结束时间</div><div class="date_right"><input type="text" id="end_date" placeholder="选择结束日期" readonly="readonly" /></div></div>';
		ht += '<div class="select_date"><a id="sele_cancel" href="javascript:;">取消</a><a id="sele_confirm" href="javascript:;">确认</a></div>';
		ht += '</div>';
		dates.innerHTML = ht;
		sele_lCalendar({
			id: 'start_date',
			min: 2017 + '-' + 8 + '-' + 29,
			max: new Date().getFullYear() + '-' + (new Date().getMonth() + 1) + '-' + new Date().getDate()
		});
		sele_lCalendar({
			id: 'end_date',
			min: 2017 + '-' + 8 + '-' + 29,
			max: new Date().getFullYear() + '-' + (new Date().getMonth() + 1) + '-' + new Date().getDate()
		});
		var cancel_ = document.getElementById("sele_cancel");
		/*取消*/
		cancel_.onclick = function() {
			cancels();
		}
		var dateStart = document.getElementById('start_date'),
			dateEnd = document.getElementById('end_date');
		var conf = document.getElementById("sele_confirm");
		/*确定*/
		conf.onclick = function() {
			if(dateStart.value && dateEnd.value) {
				var s = dateStart.value.split('-');
				var end = dateEnd.value.split('-');
				if(new Date(s[0] * 1, s[1] * 1, s[2] * 1).getTime() > new Date(end[0] * 1, end[1] * 1, end[2] * 1).getTime()) {
					alert('请选择正确时间段！');
					return;
				}
				cancels();
				var dates = {
					start: dateStart.value,
					end: dateEnd.value
				}
				callback(con,dates);
			} else {
				alert('请选择好开始时间与结束时间！');
			}
		}

		/*取消*/
		function cancels() {
			document.body.removeChild(dates);
			document.body.style.position = 'static';
		}

		/*激活日期选择*/
		function sele_lCalendar(obj) {
			var calendar = new LCalendar();
			calendar.init({
				'trigger': '#' + obj.id, //标签id
				'type': 'date', //date 调出日期选择 datetime 调出日期时间选择 time 调出时间选择 ym 调出年月选择,
				'minDate': obj.min, //最小日期
				'maxDate': obj.max //最大日期
			});
		}
	}
}




//今天
function thisDate() {
	return {
	    start:formatDate(new Date()),
        end:formatDate(new Date())
    }
}
//昨天
function yesterday() {
    var d=formatDate(new Date(new Date().getTime()-86400000));
	return {
	    start:d,
        end:d
    }
}
//上周
function lastWeekDate() {
	var dataValue = new Date();
	var year = dataValue.getFullYear();
	var month = dataValue.getMonth() + 1;
	var day = dataValue.getDate();
	var thisWeekStart; //本周周一的时间
	if(dataValue.getDay() == 0) { //周天的情况；
		thisWeekStart = (new Date(year + '/' + month + '/' + day)).getTime() - ((dataValue.getDay()) + 6) * 86400000;
	} else {
		thisWeekStart = (new Date(year + '/' + month + '/' + day)).getTime() - ((dataValue.getDay()) - 1) * 86400000;
	}
	//获得上周时间
	var prevWeekStart = thisWeekStart - 7 * 86400000; //上周周一的时间
	var prevWeekEnd = thisWeekStart - 1 * 86400000; //上周周日的时间
	var stime = formatDate(new Date(prevWeekStart)); //开始时间
	var etime = formatDate(new Date(prevWeekEnd)); //结束时间
	return {
	    start:stime,
        end:etime
    }
}
//本周
function thisWeekDate() {
	var dataValue = new Date();
	var year = dataValue.getFullYear();
	var month = dataValue.getMonth() + 1;
	var day = dataValue.getDate();
	var thisWeekStart; //本周周一的时间
	if(dataValue.getDay() == 0) { //周天的情况；
		thisWeekStart = (new Date(year + '/' + month + '/' + day)).getTime() - ((dataValue.getDay()) + 6) * 86400000;
	} else {
		thisWeekStart = (new Date(year + '/' + month + '/' + day)).getTime() - ((dataValue.getDay()) - 1) * 86400000;
	}
	var stime = formatDate(new Date(thisWeekStart)); //开始时间
	var etime = formatDate(new Date()); //结束时间，今天
	return {
	    start:stime,
        end:etime
    }
}
//上月
function lastMonthDate() {
	var dataValue = new Date();
	var currentYear = dataValue.getFullYear();
	var currentMonth = dataValue.getMonth();
	var prevCurrentYear = 0,
		prevCurrentMonth = 0;
	if(currentMonth == 0) {
		prevCurrentYear = currentYear - 1;
		prevCurrentMonth = 12;
	} else {
		prevCurrentYear = currentYear;
		prevCurrentMonth = currentMonth - 1;
	}
	var prevmonthLastday = (new Date(currentYear, currentMonth, 1)).getTime() - 86400000;

	var stime = formatDate(new Date(prevCurrentYear, prevCurrentMonth, 1)); //开始时间
	var etime = formatDate(new Date(prevmonthLastday)); //结束时间
	return {
	    start:stime,
        end:etime
    }
}
//本月
function thisMonthDate() {
	var dataValue = new Date();
    var currentYear = dataValue.getFullYear();
    var currentMonth = dataValue.getMonth();
    var stime = formatDate(new Date(currentYear, currentMonth, 1)); //开始时间
    var etime = formatDate(new Date()); //结束时间
    return {
	    start:stime,
        end:etime
    }
}
//格式化日期：yyyy/MM/dd
function formatDate(date) {
	var myyear = date.getFullYear();
	var mymonth = date.getMonth() + 1;
	var myweekday = date.getDate();
	if(mymonth < 10) {
		mymonth = "0" + mymonth;
	}
	if(myweekday < 10) {
		myweekday = "0" + myweekday;
	}
	return(myyear + "-" + mymonth + "-" + myweekday);
}