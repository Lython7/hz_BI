! function() {
	var citys = [{
		"CountryId": 1,
		"CountryName": "本月",
		"Province": [
			{
				"ProvinceId": 1,
				"ProvinceName": "全部渠道",
				"City": [
					{
						"CityId": 1,
						"CityName": "全部区域",
						"CountyList": [
							{
								"CountyId": 1,
								"CountyName": "全部配送中心"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "B2B",
				"City": [
					{
						"CityId": 2,
						"CityName": "全部区域",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							}
						]
					},
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 3,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 1,
								"CountyName": "北京仓库"
							},
							{
								"CountyId": 2,
								"CountyName": "北京分仓"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "天津仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "双鸭山分公司",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "双鸭山仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "东北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "沈阳仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华南大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "深圳仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "西南大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "成都仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "北方大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "呼和浩特仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华东大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "上海仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "西北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "兰州仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "中原大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "郑州仓库"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "B2C",
				"City": [
					{
						"CityId": 2,
						"CityName": "全部区域",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							}
						]
					},
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 3,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 1,
								"CountyName": "北京仓库"
							},
							{
								"CountyId": 2,
								"CountyName": "北京分仓门店"
							},
							{
								"CountyId": 2,
								"CountyName": "直营门店"
							},
							{
								"CountyId": 2,
								"CountyName": "北京分仓"
							},
							{
								"CountyId": 2,
								"CountyName": "禾中便利店0001"
							},
							{
								"CountyId": 2,
								"CountyName": "禾中便利店0002"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 4,
								"CountyName": "天津仓库"
							},
							{
								"CountyId": 4,
								"CountyName": "天津分仓门店"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "双鸭山分公司",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 4,
								"CountyName": "双鸭山仓库"
							},
							{
								"CountyId": 4,
								"CountyName": "双鸭山分仓门店"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "东北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 4,
								"CountyName": "沈阳仓库"
							},
							{
								"CountyId": 4,
								"CountyName": "沈阳分仓门店"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华南大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 4,
								"CountyName": "深圳仓库"
							},
							{
								"CountyId": 4,
								"CountyName": "深圳分仓门店"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "西南大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "成都仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "北方大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "呼和浩特仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "华东大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "上海仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "西北大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "兰州仓库"
							}
						]
					},
					{
						"CityId": 2,
						"CityName": "中原大区",
						"CountyList": [
							{
								"CountyId": 4,
								"CountyName": "郑州仓库"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "电商渠道",
				"City": [
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 3,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 1,
								"CountyName": "京东官方直营店"
							},
							{
								"CountyId": 2,
								"CountyName": "京东九河泉仓库"
							},
							{
								"CountyId": 2,
								"CountyName": "民生银行仓库"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "电视购物",
				"City": [
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 1,
								"CountyName": "电视购物仓库"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "禾中农业",
				"City": [
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 1,
								"CountyName": "全部配送中心"
							},
							{
								"CountyId": 1,
								"CountyName": "禾中农业仓库"
							},
							{
								"CountyId": 1,
								"CountyName": "农业订单"
							}
						]
					}
				]
			},
			{
				"ProvinceId": 1,
				"ProvinceName": "产品部",
				"City": [
					{
						"CityId": 1,
						"CityName": "总部机构",
						"CountyList": [
							{
								"CountyId": 1,
								"CountyName": "产品部仓库"
							}
						]
					}
				]
			}
		]
	}];

	if(typeof define === "function") {
		define(citys)
	} else {
		window.YDUI_CITYS = citys
	}
}();