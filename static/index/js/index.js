navIndex(0);


var revenueToday = document.getElementById("revenueToday"),
	salesTrend = document.getElementById("salesTrend");

function lineChart(dom, data, col) {
	var dataZoomData = {
		type: 'inside',
		zoomLock: true
	}
	if (data.dataZoom) {
		dataZoomData.startValue = data.dataZoom.start;
		dataZoomData.endValue = data.dataZoom.end;
	}
	var lineChart = echarts.init(dom);
	lineChart.setOption({
		xAxis: {
			type: 'category',
			boundaryGap: false,
			data: data.x
		},
		yAxis: {
			type: 'value'
		},
		grid: {
			left: 50
		},
		dataZoom: [
		dataZoomData // 滑动
		],
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
	y: [820, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330],
	dataZoom: {
		start:0,
		end:7
	}
}
var towData = {
	x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
	y: [820, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330, 1320, 932, 901, 934, 1290, 1330],
	dataZoom: {
		start:0,
		end:5
	}
}
lineChart(revenueToday, todayData, '#C66E6B');
lineChart(salesTrend, towData, '#8DB9BE');

var channelOrder = echarts.init(document.getElementById("channelOrder"));
var option = {
	xAxis: {
		type: 'category',
		data: ['B2B', '电商', '电视']
	},
	yAxis: {
		type: 'value'
	},
	series: [{
		data: [120, 200, 150],
		itemStyle: { // 让折线图的每个折点都显示对应数值
			normal: {
				label: {
					show: true
				}
			}
		},
		type: 'bar'
	}]
};
channelOrder.setOption(option);

function gauge(dom, data) {
	var mychart = echarts.init(dom);
	mychart.setOption({
		series: [{
			name: '',
			type: 'gauge',
			radius: '100%',
			axisLine: {
				lineStyle: {
					color: [
						[data / 100, '#5DC776'],
						[1, '#E8E8E8']
					],
					width: '5'
				}
			},
			splitLine: {
				show: false,
				length: '5'
			},
			axisTick: {
				show: false
			},
			axisLabel: {
				show: false
			},
			pointer: {
				show: false
			},
			detail: {
				color: 'green',
				fontSize: '12',
				formatter: '{value}%',
				offsetCenter: [0, '0%']
			},
			data: [{
				value: data
			}]
		}]
	})
}
var sale = document.getElementById("sale"),
	clientAdd = document.getElementById("clientAdd"),
	orderClientCounts = document.getElementById("orderClientCounts"),
	orderCounts = document.getElementById("orderCounts");
gauge(sale, 50);
gauge(clientAdd, 60);
gauge(orderClientCounts, 45);
gauge(orderCounts, 72);

function rowBar(dom, data) {
	var chart = echarts.init(dom);
	chart.setOption({
		yAxis: {
//			show: false,
			type: 'category',
			data: data.y
		},
		xAxis: {
			type: 'value',
			show: false
		},
		grid: {
			left: 50
		},
		series: [{
			data: data.x,
			label: { // 让折线图的每个折点都显示对应数值
				show: true,
				position: 'right'
			},
			itemStyle: {
				color: '#4B6F9E'
			},
			type: 'bar'
		}]
	})
}
var saleBar = document.getElementById("saleBar"),
	salesRank = document.getElementById("salesRank");
rowBar(saleBar, {
	x: [120, 200, 150, 80, 70, 90, 110, 130, 356],
	y: ['北京', '华北区', '东北区', '北方区', '西北区', '西南区', '华南区', '华东区', '中原区']
})
rowBar(salesRank, {
	x: [120, 200, 150],
	y: ['张金勇', '赵子龙', '秦亮']
})

var categoryPie = echarts.init(document.getElementById("categoryPie"));
categoryPie.setOption({
	title: {
		text: '总资产',
		subtext: '2000000.00',
		x: 'center',
		y: '40%'
	},
	//  tooltip: {
	//      trigger: 'item',
	//      formatter: "{a} <br/>{b}: {c} ({d}%)"
	//  },
	//  legend: {
	//      orient: 'vertical',
	//      x: 'left',
	//      data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
	//  },
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
		//          labelLine: {
		//              show: true
		// normal: {
		// show: false
		// }
		//          },
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
})