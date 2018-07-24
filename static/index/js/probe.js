navIndex(1);

$(function(){
	(function() {
		var $target = $('#J_flilters');
		$target.citySelect();
		$target.on('click', function(event) {
			event.stopPropagation();
			$target.citySelect({
					country: '本月',
					provance: 'B2B',
					city: '全部区域',
					area: '全部配送中心',
					id: '1-31-330-3033'
				});
		});
		$target.on('done.ydui.cityselect', function(ret) {
			console.log(ret)
			$(this).val(ret.country + ' ' + ret.provance + ' ' + ret.city + ' ' + ret.area);
		});
	})();
})

var oBtn = document.getElementById("time-btn"),
	oShow = document.getElementById("time-show");
var dataValue = new Date();
var currentYear = dataValue.getFullYear();
var currentMonth = dataValue.getMonth() + 1;
var currentDate = dataValue.getDate();
oBtn.innerHTML = '本月';
oShow.innerHTML = currentYear + '-' + currentMonth + '-1~' + currentYear + '-' + currentMonth + '-' + currentDate;
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

var channel = document.getElementById("channelSaleroom");

function channelSaleroom(dom, data, dataZoomData) {
	var channelSaleroom = echarts.init(dom);
	channelSaleroom.setOption({
		xAxis: {
			type: 'category',
			data: data.x
		},
		yAxis: {
			type: 'value'
		},
		series: [{
			data: data.y,
			itemStyle: { // 让折线图的每个折点都显示对应数值
				normal: {
					label: {
						show: true
					}
				}
			},
			type: 'bar'
		}]
	})
}
channelSaleroom(channel, {
	x: ['B2B', '电商', '电视'],
	y: [120, 200, 150]
});

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
			type: 'value'
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
var todayData = {
	x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
	y: [820, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330]

}
var salesTrend = document.getElementById("salesTrend");
lineChart(salesTrend, todayData, '#38A7F0');

var categoryPie = echarts.init(document.getElementById("categoryPie"));
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
		data: [{
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
		]
	}]
});

var saleBar = document.getElementById("saleBar");
channelSaleroom(saleBar, {
	x: ['北京', '华北区', '东北区', '北方区', '西北区', '西南区', '华南区', '华东区', '中原区'],
	y: [120, 200, 150, 80, 70, 90, 110, 130, 356]
});