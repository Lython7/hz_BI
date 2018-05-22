var index = sessionStorage.tabIndex || 0;
navIndex(index);

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
});