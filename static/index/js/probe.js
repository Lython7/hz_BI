navIndex(1);

var oBtn = document.getElementById("time-btn"),
	oShow = document.getElementById("time-show");
var dataValue = new Date();
var currentYear = dataValue.getFullYear();
var currentMonth = dataValue.getMonth() + 1;
var currentDate = dataValue.getDate();
oBtn.innerHTML = '本月';
oShow.innerHTML = currentYear + '-' + currentMonth + '-1~' + currentYear + '-' + currentMonth + '-' + currentDate;

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
	});
}();

var lyear = ryear = currentYear,
	lmonth = rmonth = currentMonth,
	lday = 1,
	rday = currentDate;
var channal = '全部渠道', // 渠道
	region = '全部区域', // 区域
	depot = '全部配送中心'; // 配送中心
var orderAmount= document.getElementById("order-amount"), // 订单金额
	manCounts = document.getElementById("manCounts"), // 下单客户数
	orderCounts = document.getElementById("orderCounts"), // 订单数量
	addManCounts = document.getElementById("addManCounts"); // 新增客户数
var channel = document.getElementById("channelSaleroom"); // 各渠道销售额
var salesTrend = document.getElementById("salesTrend"); // 销售趋势
var categoryPie = document.getElementById("categoryPie"); // 商品统计
/*channelSaleroom(channel, {
	x: ['B2B', '电商', '电视'],
	y: [120, 200, 150]
});*/
var todayData = {
	x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
	y: [820, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330]
}
lineChart(salesTrend, todayData, '#38A7F0');
var categoryPieData=[{
					value: 335,
					name: '直接访问'
				},
				{
					value: 310,
					name: '邮件营销'
				},
				{
					value: 234,
					name: '联盟广告'
				},
				{
					value: 135,
					name: '视频广告'
				},
				{
					value: 1548,
					name: '搜索引擎'
				}
			];
categoryPieEcharts(categoryPie, categoryPieData);


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
		console.log(res);
		oBtn.innerHTML = con;
		oShow.innerHTML = res.start + '~' + res.end;
		var start = res.start.split('-');
		var end = res.end.split('-');
		/*var params = 'classify=' + classifyName + '&lyear=' + start[0] + '&lmonth=' + start[1] + '&lday=' + start[2] +'&ryear=' + end[0] + '&rmonth=' + end[1] + '&rday=' + end[2];
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
		})*/
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
			orderAmount.innerHTML=res.part1['订单金额'];
			manCounts.innerHTML=res.part1['下单客户数'];
			orderCounts.innerHTML=res.part1['订单数量'];
			addManCounts.innerHTML=res.part1['新增客户数'];
			/*各渠道销售额*/
			var data1=res.part2,
				channelData={
					x: [],
					y: []
				}
			for (var attr in data1) {
				channelData.x.push(attr);
				channelData.y.push(data1[attr]);
			}
			channelSaleroom(channel, channelData);
			/*销售趋势*/
			var data2=res.part3['销售趋势'];
			
		}
	});
}






function channelSaleroom(dom, data, dataZoomData) {
	var channelSaleroom = echarts.init(dom);
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
				formatter: function(val){
					return val>=10000?(parseInt(val/100)/100+'W'):val;
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
	var lineChart = echarts.init(dom);
	lineChart.setOption({
		grid: {
			left: 50
		},
		xAxis: {
			type: 'category',
			boundaryGap: false,
			data: data.x
		},
		yAxis: {
			type: 'value',
			axisLabel: {
				formatter: function(val){
					return val>=10000?(parseInt(val/100)/100+'W'):val;
				}
			}
		},
		dataZoom: [{ // 滑动
			type: 'inside',
			zoomLock: true,
			start: 0,
			end: 30
		}],
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

function categoryPieEcharts (dom, data) {
	var categoryPie = echarts.init(dom);
	categoryPie.setOption({
		title: {
			text: '总资产',
			subtext: '2000000.00',
			x: 'center',
			y: '40%'
		},
		series: [{
			name: '访问来源',
			type: 'pie',
			radius: ['50%', '70%'],
			avoidLabelOverlap: false,
			hoverAnimation: false, // 悬浮动画效果
			label: {
				normal: {
					show: false,
					position: 'center'
				},
				emphasis: {
					show: true,
					textStyle: {
						fontSize: '30',
						fontWeight: 'bold'
					}
				}
			},
			label: {

			},
			itemStyle: {

			},
			data: data
		}]
	});
}

/*var saleBar = document.getElementById("saleBar");
channelSaleroom(saleBar, {
	x: ['北京', '华北区', '东北区', '北方区', '西北区', '西南区', '华南区', '华东区', '中原区'],
	y: [120, 200, 150, 80, 70, 90, 110, 130, 356]
});*/