
ajax('GET','./',null,function (res) {
    var data = JSON.parse(res);

});
function categoryPieEcharts() {
    var categoryPie = echarts.init(document.getElementById("categoryPie"));
    categoryPie.setOption({
        title: {
            text: sum,
            // subtext: '2000000.00',
            x: 'center',
            y: 'center'
        },
        //  tooltip: {
        //      trigger: 'item',
        //      formatter: "{b}: {c} ({d}%)"
        //  },
        legend: {
                type: 'scroll',
                orient: 'vertical',
                x: 'left',
                data:legends
            },
        series: [{
            name: '访问来源',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            hoverAnimation: false, // 悬浮动画效果
            label: {
                show: false,
                formatter: "{b}：{c}({d}%)"
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
}
