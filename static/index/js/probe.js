navIndex(1);

var oBtn = document.getElementById("time-btn"),
	oShow = document.getElementById("time-show");
var dataValue = new Date();
var currentYear = dataValue.getFullYear();
var currentMonth = dataValue.getMonth() + 1;
var currentDate = dataValue.getDate();
oBtn.innerHTML = '本月';
oShow.innerHTML = currentYear + '-' + currentMonth + '-1~' + currentYear + '-' + currentMonth + '-' + currentDate;

var lyear = ryear = currentYear,
	lmonth = rmonth = currentMonth,
	lday = 1,
	rday = currentDate;
var channal = '全部渠道', // 渠道
	region = '全部区域', // 区域
	depot = '全部配送中心'; // 配送中心
! function() {
	var $target = $('#J_flilters');
	$target.citySelect({
		country: '本月',
		provance: '全部渠道',
		city: '全部区域',
		area: '全部配送中心'
	});
	$target.on('click', function(event) {
		event.stopPropagation();
		$target.citySelect('open');
	});
	$target.on('done.ydui.cityselect', function(ret) {
		console.log(ret);
		$(this).val(ret.country + ' ' + ret.provance + ' ' + ret.city + ' ' + ret.area);
		channal=ret.provance;
		region=ret.city;
		depot=ret.area;
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
	});
}();


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
		oBtn.innerHTML = con;
		oShow.innerHTML = res.start + '~' + res.end;
		lyear=res.start.split('-')[0];
		lmonth=res.start.split('-')[1];
		lday=res.start.split('-')[2];
		ryear=res.end.split('-')[0];
		rmonth=res.end.split('-')[1];
		rday=res.end.split('-')[2];
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
	})
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
			var echartsData={
				x:[],
				y:[]
			}
			for (var i=0; i<data2.length; i++) {
				for(var attr in data2[i]){
					var xData= endFilter==='h'?attr.split('-')[2]:attr;
					echartsData.x.push(xData + endFilter);
					echartsData.y.push(data2[i][attr]);
				}
			}
			lineChart(salesTrend, echartsData, '#38A7F0');
			/*商品统计*/
			var data3 = res.part4['商品分类销售额'];
			var categoryPieData = [],
				legends=[],
				sum=0;
			for (var attr in data3) {
				sum+=data3[attr];
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
	var dataZoom=[];
	if (data.x.length>=10) {
		dataZoom=[{ // 滑动
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
		tooltip:{
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
			data:legends
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
	categoryPie.on('click', function (params) {
		sessionStorage.tabIndex=0;
		localStorage.categoryPieName = params.name;
		location.href="../views/goodscount/";
	});
}
