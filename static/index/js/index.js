
navIndex(0);


ajax('GET', './views/incometoday/', null, function (res) {
	var data = JSON.parse(res);
	var order_amount=document.getElementById("order_amount"), // 订单金额
		ordered_cust_count=document.getElementById("ordered_cust_count"), // 下单客户数
		order_count=document.getElementById("order_count"), // 订单数量
		newreg_count=document.getElementById("newreg_count"), // 新增客户数
		revenueToday=document.getElementById("revenueToday"); // 今日营收echarts dom
	order_amount.innerHTML=outputdollars(data.order_amount);
	ordered_cust_count.innerHTML=outputdollars(data.ordered_cust_count);
	order_count.innerHTML=outputdollars(data.order_count);
	newreg_count.innerHTML=outputdollars(data.newreg_count);

	var arr={
		x:[],
		y:[]
	}
	var len=data.hours_data.length;
	for(var i=0; i<len; i++){
		arr.x.push(i);
		arr.y.push(data.hours_data[i]);
	}
	if (arr.x.length>7){
		var start,end;
		var h=new Date().getHours();
		if (h>8){
			if (h<15){
				start=h-7;
				end=h;
			}else {
				start=8;
				end=15;
			}
		}else {
			start=0;
			end=h;
		}
		arr.dataZoom={
						start:start,
						end:end
					}
	}
	lineChart(revenueToday, arr, '#C66E6B');
});
ajax('GET', './views/salesamount/', null, function (res) {
	var data =JSON.parse(res);
	var sale = document.getElementById("sale"),
		order_amount_month = document.getElementById("sale_order_amount_month"),
		order_amount_lastmonth = document.getElementById("sale_order_amount_lastmonth"),
		month_ratio = document.getElementById("sale_month_ratio"),
		order_amount_year = document.getElementById("sale_order_amount_year"),
		year_ratio = document.getElementById("sale_year_ratio");
	gauge(sale, parseFloat(data.ratio));
	order_amount_month.innerHTML=outputdollars(data.order_amount_month);
	order_amount_lastmonth.innerHTML=outputdollars(data.order_amount_lastmonth);
	month_ratio.innerHTML=data.month_ratio;
	order_amount_year.innerHTML=outputdollars(data.order_amount_year);
	year_ratio.innerHTML=data.year_ratio;
});
ajax('GET', './views/storecount/', null, function (res) {
	var data =JSON.parse(res);
	var clientAdd = document.getElementById("clientAdd"),
		store_reg_month = document.getElementById("store_reg_month"),
		store_reg_lastmonth = document.getElementById("store_reg_lastmonth"),
		month_ratio = document.getElementById("month_ratio"),
		store_reg_year = document.getElementById("store_reg_year"),
		year_ratio = document.getElementById("year_ratio");
	gauge(clientAdd, parseFloat(data.ratio));
	store_reg_month.innerHTML=outputdollars(data.store_reg_month);
	store_reg_lastmonth.innerHTML=outputdollars(data.store_reg_lastmonth);
	month_ratio.innerHTML=data.month_ratio;
	store_reg_year.innerHTML=outputdollars(data.store_reg_year);
	year_ratio.innerHTML=data.year_ratio;
});
ajax('GET', './views/orderstorecount/', null, function (res) {
	var data =JSON.parse(res);
	var orderClientCounts = document.getElementById("orderClientCounts"),
		orderClient_odstore_count_month = document.getElementById("orderClient_odstore_count_month"),
		orderClient_odstore_count_lastmonth = document.getElementById("orderClient_odstore_count_lastmonth"),
		orderClient_month_ratio = document.getElementById("orderClient_month_ratio"),
		orderClient_odstore_count_year = document.getElementById("orderClient_odstore_count_year"),
		orderClient_year_ratio = document.getElementById("orderClient_year_ratio");
	gauge(orderClientCounts, parseFloat(data.ratio));
	orderClient_odstore_count_month.innerHTML=outputdollars(data.odstore_count_month);
	orderClient_odstore_count_lastmonth.innerHTML=outputdollars(data.odstore_count_lastmonth);
	orderClient_month_ratio.innerHTML=data.month_ratio;
	orderClient_odstore_count_year.innerHTML=outputdollars(data.odstore_count_year);
	orderClient_year_ratio.innerHTML=data.year_ratio;
});
ajax('GET', './views/ordercount/', null, function (res) {
	var data =JSON.parse(res);
	var orderCounts = document.getElementById("orderCounts"),
		orderCounts_order_month = document.getElementById("orderCounts_order_month"),
		orderCounts_order_lastmonth = document.getElementById("orderCounts_order_lastmonth"),
		orderCounts_month_ratio = document.getElementById("orderCounts_month_ratio"),
		orderCounts_order_year = document.getElementById("orderCounts_order_year"),
		orderCounts_year_ratio = document.getElementById("orderCounts_year_ratio");
	gauge(orderCounts, parseFloat(data.ratio));
	orderCounts_order_month.innerHTML=outputdollars(data.order_month);
	orderCounts_order_lastmonth.innerHTML=outputdollars(data.order_lastmonth);
	orderCounts_month_ratio.innerHTML=data.month_ratio;
	orderCounts_order_year.innerHTML=outputdollars(data.order_year);
	orderCounts_year_ratio.innerHTML=data.year_ratio;
});
ajax('GET', './views/channal_salesamount_month/', null, function (res) {
	var data=JSON.parse(res);
	var channels=document.getElementById("channelOrder");
	var datas={
		x:[],
		y:[]
	};
	function switchs(data){
			switch (data){
				case 'b2b':
					return 'B2B';
					break;
				case 'agriculture':
					return '农业';
					break;
				case 'online':
					return '线上';
					break;
				case 'television':
					return '电视';
					break;
				case 'taste':
					return '禾中味道';
					break;
				default:
					return data;
					break;
			}
	}
	for (var item in data){
		datas.x.push(switchs(item));
		datas.y.push(data[item]);
	}
	channelOrder(channels,datas);
});

function outputdollars(number) {
	number+='';
	if(number.length <= 3){ // 不足3位数
		return number === '' ? '0' : number;
	}else {
		var mod = number.length % 3; // 有多少位非3倍数的
		var output = (mod === 0 ? '' : (number.substring(0, mod))); // 前面非3倍数的数位金钱
		var len = Math.floor(number.length / 3); // 有几个3的倍数
		for(i = 0; i < len; i++) {
			if(mod===0 && i === 0){ // 第一次拼接且number是3的整数倍
				output += number.substring(mod + 3 * i, mod + 3 * i + 3);
			}else{
				output += ',' + number.substring(mod + 3 * i, mod + 3 * i + 3);
			}
		}
		return(output);
	}
}


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
			type: 'value',
			axisLabel: {
				formatter: function(val){
					return val>=10000?(parseInt(val/100)/100+'W'):val;
				}
			}
		},
		grid: {
			left: 60
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

ajax('GET', './views/salestrend/', null, function (res) {
	var data = JSON.parse(res);
	var salesTrend = document.getElementById("salesTrend");
	var datas = {
		x:data.date,
		y:data.data,
		dataZoom:{
			start:0,
			end:50
		}
	}
	lineChart2(salesTrend, datas, '#8DB9BE');
});
function lineChart2(dom, data, col) {
	var dataZoomData = {
		type: 'inside',
		zoomLock: true
	}
	if (data.dataZoom) {
		dataZoomData.start = data.dataZoom.start;
		dataZoomData.end = data.dataZoom.end;
	}
	var lineChart = echarts.init(dom);
	lineChart.setOption({
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
		grid: {
			left: 40
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
ajax('GET', './views/classify_amount_month/', null, function (res) {
	var data = JSON.parse(res).data;
	var datas = [],
		legends=[],
		sum=0;
	for (var item in data) {
		sum+=data[item];
		legends.push(item);
		datas.push({
			value: data[item],
			name: item
		})
	}
	categoryPieEcharts(datas, sum, legends);
});
function categoryPieEcharts(datas, sum, legends) {
	var categoryPie = echarts.init(document.getElementById("categoryPie"));
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
		location.href="views/goodscount/";
	});
}
function channelOrder(dom, data) {
	var channelOrder = echarts.init(dom);
	channelOrder.setOption({
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
			label: { // 让折线图的每个折点都显示对应数值
				show: true,
				position: 'top'
			},
			type: 'bar'
		}]
	});
}
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
function rowBar(dom, data) {
	var chart = echarts.init(dom);
	chart.setOption({
		yAxis: {
			type: 'category',
			data: data.y
		},
		xAxis: {
			type: 'value',
			show: false,
			boundaryGap: ['0%', '6%']
		},
		grid: {
			left: 80
		},
		series: [{
			data: data.x,
			label: { // 让折线图的每个折点都显示对应数值
				show: true,
				position: 'right'/*,
				formatter: function (params) {
					return (parseInt(params.data/100)/100).toFixed(2) + 'W';
                }*/
			},
			itemStyle: {
				color: '#4B6F9E'
			},
			type: 'bar'
		}]
	})
}
ajax('GET', './views/region_amount_month/', null, function (res) {
	var data = JSON.parse(res);
	var saleBar = document.getElementById("saleBar");
	if(res != '{}'){
		var datas={
			x:[],
			y:[]
		}
		for (var item in data){
			datas.x.push(data[item]);
			datas.y.push(item);
		}
		rowBar(saleBar, datas);
	}else {
		saleBar.innerHTML='<p style="font-size: 26px;text-align: center">暂无数据</p>';
	}
});




var dateNow = new Date();
var year_=dateNow.getFullYear(),month_=dateNow.getMonth()+1;
ajax('GET', './views/score/'+year_+'/'+month_, null, function (res) {
	// var data = JSON.parse(res).splice(0,3); // 返回删除的数组项目
	var data = JSON.parse(res);
	var salesRank = document.getElementById("salesRank");
	if(data.length){
		var datas={
			x:[],
			y:[]
		}
		var len = data.length<3?data.length:3;
		for (var i=0; i<len; i++){
			datas.x.push(parseInt(data[i].sum));
			datas.y.push(data[i].name);
		}
		datas.x.reverse();
		datas.y.reverse();
		rowBar(salesRank, datas);
	}else {
		salesRank.innerHTML='<p style="font-size: 26px;text-align: center">暂无数据</p>';
	}
});