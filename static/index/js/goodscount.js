var index = sessionStorage.tabIndex || 0;
navIndex(index);
var oBtn = document.getElementById("time-btn"),
	oShow = document.getElementById("time-show");
var dataValue = new Date();
var currentYear = dataValue.getFullYear();
var currentMonth = dataValue.getMonth()+1;
var currentDate = dataValue.getDate();
oBtn.innerHTML='本月';
oShow.innerHTML=currentYear+'-'+currentMonth+'-1~'+currentYear+'-'+currentMonth+'-'+currentDate;
var pieChart = document.getElementById("categoryPie");
var categoryPie = echarts.init(pieChart);
var classifyName = localStorage.categoryPieName || '饮料';
ajax('GET','../goodscount_2/','classify=' + classifyName + '&lyear=' + currentYear + '&lmonth=' + currentMonth + '&lday=1&ryear=' + currentYear + '&rmonth=' + currentMonth + '&rday=' + currentDate,function (res) {
    var data = JSON.parse(res);
	var sum = data.amount;
	var datas = [];
	for(var item in data.data){
		datas.push({
			name: item,
			value: data.data[item]
		})
	}
	datas.sort(function (a, b) {
		return b.value - a.value;
    });
	console.log(datas);
	init(sum, datas);
});


oBtn.onclick = function() {
	chooseCreate(function(con, res) {
        console.log(res);
        oBtn.innerHTML=con;
        oShow.innerHTML=res.start+'~'+res.end;
        var start = res.start.split('-');
        var end = res.end.split('-');
        var params = 'classify=' + classifyName + '&lyear=' + start[0] + '&lmonth=' + start[1] + '&lday=' + start[2] +'&ryear=' + end[0] + '&rmonth=' + end[1] + '&rday=' + end[2];
        ajax('GET','../goodscount_2/',params,function (res){
        	var data = JSON.parse(res);
			var sum = data.amount;
			var datas = [];
			for(var item in data.data){
				datas.push({
					name: item,
					value: data.data[item]
				})
			}
			datas.sort(function (a, b) {
				return b.value - a.value;
			});
			console.log(datas);
			init(sum, datas);
		})
    })
}

// var data = [
// 	{
// 		value: 335,
// 		name: '直接访问'
// 	},
// 	{
// 		value: 310,
// 		name: '邮件营销'
// 	},
// 	{
// 		value: 234,
// 		name: '联盟广告'
// 	},
// 	{
// 		value: 135,
// 		name: '视频广告'
// 	},
// 	{
// 		value: 1548,
// 		name: '搜索引擎'
// 	}
// ];
// categoryPieEcharts(data);

function init(sum, data) {
	categoryPieEcharts(sum, data); // 绘制echarts饼图
	sortList(data); // 排名
}
function categoryPieEcharts(sum, data) {

	var legends=[];
	for (var i=0; i<data.length; i++){
	    sum+=data[i].value;
	    legends.push(data[i].name);
    }
	categoryPie.setOption({
		title: {
			text: sum,
			// subtext: '2000000.00',
			x: 'center',
			y: 'center'
		},
		 tooltip: {
		     trigger: 'item',
		     formatter: "{b}:<br /> {c}"
		 },
		legend: {
			type: 'scroll',
			orient: 'vertical',
			left: '0',
			data: legends,
			formatter: function (name) {
				return name.substring(0,7);
			}
		},
		series: [{
			name: '访问来源',
			type: 'pie',
			radius: ['40%', '68%'],
			avoidLabelOverlap: false,
			hoverAnimation: true, // 悬浮动画效果
			label: {
				show: false,
				formatter: "{b}：{c}({d}%)"
			},
			data: data
		}]
	});
}
function sortList(data) {
	var other;
	for (var i=0; i<data.length; i++){
		if (data[i].name=='其它'){
			other=data[i];
			data.splice(i,1);
			i--;
		}
	}
	data.push(other);
	var ranking = document.getElementById("ranking");
	var str='';
	for (var i=0; i<data.length; i++){
		var val = data[i].value>=10000 ? parseInt(data[i].value/100)/100 + 'W' : data[i].value;
		str += '<li class="clearfix"><span class="sale-index">' + (i+1) + '</span><span class="sale-name">' + data[i].name + '</span><span class="sale-counts">' + val + '</span></li>'
	}
	ranking.innerHTML=str;
}