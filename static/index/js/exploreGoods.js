var index = sessionStorage.tabIndex || 0;
navIndex(index);
var oCategoryName = document.getElementById("categoryName");
var pieChart = document.getElementById("categoryPie");
var categoryPie = echarts.init(pieChart);
var classifyName = localStorage.categoryPieName || '饮料';
oCategoryName.innerHTML=classifyName;
var params = location.href.split('?')[1];
var paramsArr = params.split('&');
var res=[];
for (var i=0; i<paramsArr.length; i++){
	var tem = paramsArr[i].split('=');
	res.push(tem[0] + '=' +decodeURI(tem[1]))
}
var params_=res.join('&');
ajax('GET','../goodscount_2/',params_,function (res) {
    var data = JSON.parse(res);
    if (data.data&&data.amount){
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
	}
});


function init(sum, data) {
	categoryPieEcharts(sum, data); // 绘制echarts饼图
	sortList(data); // 排名
}
function categoryPieEcharts(sum, data) {
	var legends=[];
	for (var i=0; i<data.length; i++){
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
		     formatter: "{b}: {c}"
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