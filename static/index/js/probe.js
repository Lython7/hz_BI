navIndex(1);

function formatter(params) {
	var temRes = params.split('&');
	var res = {}
	for(var i = 0; i < temRes.length; i++) {
		var tems = temRes[i].split('=');
		res[tems[0]] = tems[1];
	}
	return res;
}
var oBtn = document.getElementById("time-btn"),
	oShow = document.getElementById("time-show");
var $target = $('#J_flilters'); // 筛选
var dates, lyear, lmonth, lday, ryear, rmonth, rday, channal, region, depot;
var params = location.href.split("?")[1];

function trueOn(params) {
	var temRes = formatter(params);
	dates = decodeURI(temRes.dates);
	lyear = decodeURI(temRes.lyear);
	lmonth = decodeURI(temRes.lmonth);
	lday = decodeURI(temRes.lday);
	ryear = decodeURI(temRes.ryear);
	rmonth = decodeURI(temRes.rmonth);
	rday = decodeURI(temRes.rday);
	channal = decodeURI(temRes.channal);
	region = decodeURI(temRes.region);
	depot = decodeURI(temRes.depot);
}

function falseOff() {
	dates = '本月';
	lyear = ryear = new Date().getFullYear();
	lmonth = rmonth = new Date().getMonth() + 1;
	lday = 1;
	rday = new Date().getDate();
	channal = '全部渠道'; // 渠道
	region = '全部区域'; // 区域
	depot = '全部配送中心'; // 配送中心
}
if(params) {
	trueOn(params);
} else {
	falseOff();
}

oBtn.innerHTML = dates;
YDUI_CITYS[0].CountryName = dates;
oShow.innerHTML = lyear + '-' + lmonth + '-' + lday + '~' + ryear + '-' + rmonth + '-' + rday;
$target.val(dates + ' ' + channal + ' ' + region + ' ' + depot);

$target.citySelect({
	country: dates,
	provance: channal,
	city: region,
	area: depot
});
$target.on('click', function(event) {
	event.stopPropagation();
	$target.citySelect('open');
});
$target.on('done.ydui.cityselect', function(ret) {
	channal = ret.provance;
	region = ret.city;
	depot = ret.area;
	initLink();
});


var orderAmount = document.getElementById("order-amount"), // 订单金额
	manCounts = document.getElementById("manCounts"), // 下单客户数
	orderCounts = document.getElementById("orderCounts"), // 订单数量
	addManCounts = document.getElementById("addManCounts"); // 新增客户数
var channel = echarts.init(document.getElementById("channelSaleroom")); // 各渠道销售额
var salesTrend = echarts.init(document.getElementById("salesTrend")); // 销售趋势
var categoryPie = echarts.init(document.getElementById("categoryPie")); // 商品统计

init({
	lyear: lyear,
	lmonth: lmonth,
	lday: lday,
	ryear: ryear,
	rmonth: rmonth,
	rday: rday,
	channal: channal,
	region: region,
	depot: depot
})

oBtn.onclick = function() {
	chooseCreate(function(con, res) {
		/*oBtn.innerHTML = con;
		YDUI_CITYS[0].CountryName = con;
		var temValue = $target.val().split(' ');
		temValue[0] = con;
		$target.val(temValue.join(' '));
		oShow.innerHTML = res.start + '~' + res.end;*/
		dates=con;
		lyear = res.start.split('-')[0];
		lmonth = res.start.split('-')[1];
		lday = res.start.split('-')[2];
		ryear = res.end.split('-')[0];
		rmonth = res.end.split('-')[1];
		rday = res.end.split('-')[2];
		initLink();
		/*init({
			lyear: lyear,
			lmonth: lmonth,
			lday: lday,
			ryear: ryear,
			rmonth: rmonth,
			rday: rday,
			channal: channal,
			region: region,
			depot: depot
		})*/
	})
}
function initLink() {
	location.href='../explore/?'+'lyear=' + encodeURI(lyear) + '&lmonth=' + encodeURI(lmonth) + '&lday=' + encodeURI(lday) + '&ryear=' + encodeURI(ryear) + '&rmonth=' + encodeURI(rmonth) + '&rday=' + encodeURI(rday) + '&dates=' + encodeURI(dates) + '&channal=' + encodeURI(channal) + '&region=' + encodeURI(region) + '&depot=' + encodeURI(depot);
}
function init(data, callback) {
	$.ajax({
		type: "get",
		url: "./exploreAPI",
		data: {
			lyear: data.lyear,
			lmonth: data.lmonth,
			lday: data.lday,
			ryear: data.ryear,
			rmonth: data.rmonth,
			rday: data.rday,
			channal: data.channal,
			region: data.region,
			depot: data.depot
		},
		success: function(res) {
			console.log(res);
			orderAmount.innerHTML = res.part1['订单金额'];
			manCounts.innerHTML = res.part1['下单客户数'];
			orderCounts.innerHTML = res.part1['订单数量'];
			addManCounts.innerHTML = res.part1['新增客户数'];
			/*各渠道销售额*/
			var data1 = res.part2,
				channelData = {
					x: [],
					y: []
				}
			for(var attr in data1) {
				channelData.x.push(attr);
				channelData.y.push(data1[attr]);
			}
			channelSaleroom(channel, channelData);
			/*销售趋势*/
			var data2 = res.part3['销售趋势'];
			var endFilter = switchs(res.part3['类型']);
			var echartsData = {
				x: [],
				y: []
			}
			for(var i = 0; i < data2.length; i++) {
				for(var attr in data2[i]) {
					var xData = endFilter === 'h' ? attr.split('-')[2] : attr;
					echartsData.x.push(xData + endFilter);
					echartsData.y.push(data2[i][attr]);
				}
			}
			lineChart(salesTrend, echartsData, '#38A7F0');
			/*商品统计*/
			var data3 = res.part4['商品分类销售额'];
			var categoryPieData = [],
				legends = [],
				sum = 0;
			for(var attr in data3) {
				sum += data3[attr];
				legends.push(attr);
				categoryPieData.push({
					name: attr,
					value: data3[attr]
				})
			}
			categoryPieEcharts(categoryPie, categoryPieData, sum, legends);
		}
	});
}

function switchs(data) {
	switch(data) {
		case 'week':
			return '周';
			break;
		case 'day':
			return '日';
			break;
		case 'month':
			return '月';
			break;
		case 'hour':
			return 'h';
			break;
		default:
			return data;
			break;
	}
}

function channelSaleroom(dom, data, dataZoomData) {
	var channelSaleroom = dom;
	channelSaleroom.setOption({
		xAxis: {
			type: 'category',
			axisLabel: {
				rotate: 30
			},
			data: data.x
		},
		yAxis: {
			type: 'value',
			axisLabel: {
				formatter: function(val) {
					return val >= 10000 ? (parseInt(val / 100) / 100 + 'W') : val;
				}
			}
		},
		series: [{
			data: data.y,
			label: {
				show: true,
				position: 'top'
			},
			type: 'bar'
		}]
	})
}

function lineChart(dom, data, col) {
	//	var lineChart = echarts.init(dom);
	var lineChart = dom;
	var dataZoom = [];
	if(data.x.length >= 10) {
		dataZoom = [{ // 滑动
			type: 'inside',
			zoomLock: true,
			startValue: data.x[0],
			endValue: data.x[9]
		}]
	}
	lineChart.setOption({
		grid: {
			left: 50
		},
		xAxis: {
			type: 'category',
			boundaryGap: false,
			data: data.x
		},
		tooltip: {
			show: true,
			trigger: 'axis'
		},
		yAxis: {
			type: 'value',
			axisLabel: {
				formatter: function(val) {
					return val >= 10000 ? (parseInt(val / 100) / 100 + 'W') : val;
				}
			}
		},
		dataZoom: dataZoom,
		series: [{
			smooth: true, // 曲线平滑
			itemStyle: { // 让折线图的每个折点都显示对应数值
				normal: {
					label: {
						show: true
					},
					color: col
				}
			},
			data: data.y,
			type: 'line',
			areaStyle: {}
		}]
	})
}

function categoryPieEcharts(dom, datas, sum, legends) {
	//	var categoryPie = echarts.init(dom);
	var categoryPie = dom;
	categoryPie.setOption({
		title: {
			text: sum,
			// subtext: '2000000.00',
			x: 'center',
			y: 'center'
		},
		legend: {
			type: 'scroll',
			orient: 'vertical',
			x: 'left',
			data: legends
		},
		series: [{
			name: '本月商品分类销售额',
			type: 'pie',
			radius: ['50%', '70%'],
			avoidLabelOverlap: false,
			hoverAnimation: false, // 悬浮动画效果
			label: {
				show: false,
				formatter: "{b}：{c}({d}%)"
			},
			labelLine: {
				show: false
			},
			data: datas
		}]
	});
	categoryPie.on('click', function(params) {
		sessionStorage.tabIndex = 1;
		localStorage.categoryPieName = params.name;
		var params = '?lyear=' + encodeURI(lyear) + '&lmonth=' + encodeURI(lmonth) + '&lday=' + encodeURI(lday) + '&ryear=' + encodeURI(ryear) + '&rmonth=' + encodeURI(rmonth) + '&rday=' + encodeURI(rday) + '&channal=' + encodeURI(channal) + '&region=' + encodeURI(region) + '&depot=' + encodeURI(depot) + '&classify=' + encodeURI(params.name);
// 		var params = '?lyear=' + lyear + '&lmonth=' + lmonth + '&lday=' + lday + '&ryear=' + ryear + '&rmonth=' + rmonth + '&rday=' + rday + '&channal=' + channal + '&region=' + region + '&depot=' + depot + '&classify=' + params.name;
		location.href = "goodscount/" + params;
	});
}