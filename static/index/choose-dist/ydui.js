! function(window) {
	"use strict";
	var doc = window.document,
		ydui = {};
	$(window).on('load', function() {
		typeof FastClick == 'function' && FastClick.attach(doc.body);
	});
	var util = ydui.util = {
		parseOptions: function(string) {
			if($.isPlainObject(string)) {
				return string;
			}
			var start = (string ? string.indexOf('{') : -1),
				options = {};
			if(start != -1) {
				try {
					options = (new Function('', 'var json = ' + string.substr(start) + '; return JSON.parse(JSON.stringify(json));'))();
				} catch(e) {}
			}
			return options;
		},
		pageScroll: function() {
			var fn = function(e) {
				e.preventDefault();
				e.stopPropagation();
			};
			var islock = false;
			return {
				lock: function() {
					if(islock) return;
					islock = true;
					doc.addEventListener('touchmove', fn);
				},
				unlock: function() {
					islock = false;
					doc.removeEventListener('touchmove', fn);
				}
			};
		}(),
		localStorage: function() {
			return storage(window.localStorage);
		}(),
		sessionStorage: function() {
			return storage(window.sessionStorage);
		}(),
		serialize: function(value) {
			if(typeof value === 'string') return value;
			return JSON.stringify(value);
		},
		deserialize: function(value) {
			if(typeof value !== 'string') return undefined;
			try {
				return JSON.parse(value);
			} catch(e) {
				return value || undefined;
			}
		}
	};

	function storage(ls) {
		return {
			set: function(key, value) {
				ls.setItem(key, util.serialize(value));
			},
			get: function(key) {
				return util.deserialize(ls.getItem(key));
			},
			remove: function(key) {
				ls.removeItem(key);
			},
			clear: function() {
				ls.clear();
			}
		};
	}
	$.fn.emulateTransitionEnd = function(duration) {
		var called = false,
			$el = this;
		$(this).one('webkitTransitionEnd', function() {
			called = true;
		});
		var callback = function() {
			if(!called) $($el).trigger('webkitTransitionEnd');
		};
		setTimeout(callback, duration);
	};
	if(typeof define === 'function') {
		define(ydui);
	} else {
		window.YDUI = ydui;
	}
}(window);
! function(window) {
	var doc = window.document,
		ydui = window.YDUI,
		ua = window.navigator && window.navigator.userAgent || '';
	var ipad = !!ua.match(/(iPad).*OS\s([\d_]+)/),
		ipod = !!ua.match(/(iPod)(.*OS\s([\d_]+))?/),
		iphone = !ipad && !!ua.match(/(iPhone\sOS)\s([\d_]+)/);
	ydui.device = {
		isMobile: !!ua.match(/AppleWebKit.*Mobile.*/) || 'ontouchstart' in doc.documentElement,
		isIOS: !!ua.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),
		isAndroid: !!ua.match(/(Android);?[\s\/]+([\d.]+)?/),
		isIpad: ipad,
		isIpod: ipod,
		isIphone: iphone,
		isWebView: (iphone || ipad || ipod) && !!ua.match(/.*AppleWebKit(?!.*Safari)/i),
		isWeixin: ua.indexOf('MicroMessenger') > -1,
		isMozilla: /firefox/.test(navigator.userAgent.toLowerCase()),
		pixelRatio: window.devicePixelRatio || 1
	};
}(window);
! function(window) {
	window.document.addEventListener('touchstart', function(event) {}, false);
}(window);
! function(window) {
	"use strict";
	var $body = $(window.document.body);

	function CitySelect(element, options) {
		this.$element = $(element);
		this.options = $.extend({}, CitySelect.DEFAULTS, options || {});
		this.init();
	}
	CitySelect.DEFAULTS = {
		country: '',
		provance: '',
		city: '',
		area: '',
		id: ''
	};
	CitySelect.prototype.init = function() {
		var _this = this,
			options = _this.options;
		if(typeof YDUI_CITYS == 'undefined') {
			return;
		}
		_this.citys = YDUI_CITYS;
		_this.createDOM();
		_this.defaultSet = {
			country: options.country,
			provance: options.provance,
			city: options.city,
			area: options.area,
			id: options.id
		};
	};
	CitySelect.prototype.open = function() {
		var _this = this;
		$body.append(_this.$mask);
		YDUI.device.isMozilla && _this.$element.blur();
		_this.$mask.on('click.ydui.cityselect.mask', function() {
			_this.close();
		});
		var $cityElement = _this.$cityElement,
			defaultSet = _this.defaultSet;
		$cityElement.find('.cityselect-content').removeClass('cityselect-move-animate cityselect-next cityselect-prev cityselect-next-two');
		_this.loadCountry();
		_this.loadProvance();
		console.log(defaultSet.id);
		if(defaultSet.country) {
			_this.setNavTxt(0, defaultSet.country, defaultSet.id.split('-')[0]);
		} else {
			$cityElement.find('.cityselect-nav a').eq(0).addClass('crt').html('请选择');
		}
		if(defaultSet.provance) {
			_this.loadProvance();
			_this.setNavTxt(1, defaultSet.provance, defaultSet.id.split('-')[1]);
		}
		if(defaultSet.city) {
			_this.loadCity();
			_this.ForwardViewTwo(true);
			_this.setNavTxt(2, defaultSet.city, defaultSet.id.split('-')[2]);
		}
		if(defaultSet.area) {
			_this.loadArea();
			_this.ForwardViewTwo(true);
			_this.setNavTxt(3, defaultSet.area, defaultSet.id.split('-')[3]);
		}
		$cityElement.addClass('brouce-in');
	};
	CitySelect.prototype.close = function() {
		var _this = this;
		_this.$mask.remove();
		_this.$cityElement.removeClass('brouce-in').find('.cityselect-nav a').removeClass('crt').html('');
		_this.$itemBox.html('');
	};
	CitySelect.prototype.createDOM = function() {
		var _this = this;
		_this.$mask = $('<div class="mask-black"></div>');
		_this.$cityElement = $('' +
			'<div class="m-cityselect">' +
			'    <div class="cityselect-header">' +
			'        <p class="cityselect-title">筛选顺序：时间-渠道-区域-配送中心</p>' +
			'        <div class="cityselect-nav">' +
			'            <a href="javascript:;"></a>' +
			'            <a href="javascript:;"></a>' +
			'            <a href="javascript:;"></a>' +
			'            <a href="javascript:;"></a>' +
			'        </div>' +
			'    </div>' +
			'    <ul class="cityselect-content">' +
			'        <li class="cityselect-item">' +
			'            <div class="cityselect-item-box"></div>' +
			'        </li>' +
			'        <li class="cityselect-item">' +
			'            <div class="cityselect-item-box"></div>' +
			'        </li>' +
			'        <li class="cityselect-item">' +
			'            <div class="cityselect-item-box"></div>' +
			'        </li>' +
			'        <li class="cityselect-item">' +
			'            <div class="cityselect-item-box"></div>' +
			'        </li>' +
			'    </ul>' +
			'</div>');
		$body.append(_this.$cityElement);
		_this.$itemBox = _this.$cityElement.find('.cityselect-item-box');
		_this.$cityElement.on('click.ydui.cityselect', '.cityselect-nav a', function() {
			var $this = $(this);
			$this.addClass('crt').siblings().removeClass('crt');
			$this.index() < 2 ? _this.backOffView() : $this.index() == 2 ? _this.ForwardView(true) : _this.ForwardViewTwo(true);
		});
	};
	CitySelect.prototype.setNavTxt = function(index, txt, id) {
		var $nav = this.$cityElement.find('.cityselect-nav a');
		index < 3 && $nav.removeClass('crt');
		$nav.eq(index).html(txt);
		$nav.eq(index).attr("cid", id);
		$nav.eq(index + 1).addClass('crt').html('请选择');
		$nav.eq(index + 2).removeClass('crt').html('');
		$nav.eq(index + 3).removeClass('crt').html('');
		$nav.eq(index + 1).attr("cid", '');
		$nav.eq(index + 2).attr("cid", '');
		$nav.eq(index + 3).attr("cid", '');
	};
	CitySelect.prototype.backOffView = function() {
		this.$cityElement.find('.cityselect-content').removeClass('cityselect-next cityselect-next-two').addClass('cityselect-move-animate cityselect-prev');
	};
	CitySelect.prototype.ForwardView = function(animate) {
		this.$cityElement.find('.cityselect-content').removeClass('cityselect-move-animate cityselect-prev cityselect-next-two').addClass((animate ? 'cityselect-move-animate' : '') + ' cityselect-next');
	};
	CitySelect.prototype.ForwardViewTwo = function(animate) {
		this.$cityElement.find('.cityselect-content').removeClass('cityselect-move-animate cityselect-prev cityselect-next').addClass((animate ? 'cityselect-move-animate' : '') + ' cityselect-next-two');
	};
	CitySelect.prototype.bindItemEvent = function() {
		var _this = this,
			$cityElement = _this.$cityElement;
		$cityElement.on('click.ydui.cityselect', '.cityselect-item-box a', function() {
			var $this = $(this);
			if($this.hasClass('crt')) return;
			$this.addClass('crt').siblings().removeClass('crt');
			var tag = $this.data('tag');
			var id = $this.attr("cid");
			_this.setNavTxt(tag, $this.text(), id);
			var $nav = $cityElement.find('.cityselect-nav a'),
				defaultSet = _this.defaultSet;
			if(tag == 0) {
				_this.loadProvance();
				$cityElement.find('.cityselect-item-box').eq(1).find('a').removeClass('crt');
			} else if(tag == 1) {
				_this.loadCity();
				_this.ForwardView(true);
				$cityElement.find('.cityselect-item-box').eq(2).find('a').removeClass('crt');
			} else if(tag == 2) {
				_this.loadArea();
				_this.ForwardViewTwo(true);
				$cityElement.find('.cityselect-item-box').eq(3).find('a').removeClass('crt');
			} else {
				defaultSet.country = $nav.eq(0).html();
				defaultSet.provance = $nav.eq(1).html();
				defaultSet.city = $nav.eq(2).html();
				defaultSet.area = $nav.eq(3).html();
				defaultSet.id = $nav.eq(0).attr("cid") + '-' + $nav.eq(1).attr("cid") + '-' + $nav.eq(2).attr("cid") + '-' + $nav.eq(3).attr("cid");
				console.log(defaultSet.id)
				_this.returnValue();
			}
		});
	};
	CitySelect.prototype.returnValue = function() {
		var _this = this,
			defaultSet = _this.defaultSet;
		_this.$element.trigger($.Event('done.ydui.cityselect', {
			country: defaultSet.country,
			provance: defaultSet.provance,
			city: defaultSet.city,
			area: defaultSet.area,
			id: defaultSet.id
		}));
		_this.close();
	};
	CitySelect.prototype.scrollPosition = function(index) {
		var _this = this,
			$itemBox = _this.$itemBox.eq(index),
			itemHeight = $itemBox.find('a.crt').height(),
			itemBoxHeight = $itemBox.parent().height();
		$itemBox.parent().animate({
			scrollTop: $itemBox.find('a.crt').index() * itemHeight - itemBoxHeight / 3
		}, 0, function() {
			_this.bindItemEvent();
		});
	};
	CitySelect.prototype.fillItems = function(index, arr) {
		var _this = this;
		_this.$itemBox.eq(index).html(arr).parent().animate({
			scrollTop: 0
		}, 10);
		_this.scrollPosition(index);
	};
	CitySelect.prototype.loadCountry = function() {
		var _this = this;
		var arr = [];
		$.each(_this.citys, function(k, v) {
			arr.push($('<a cid="' + v.CountryId + '" class="' + (v.CountryName == _this.defaultSet.country ? 'crt' : '') + '" href="javascript:;"><span>' + v.CountryName + '</span></a>').data({
				citys: v.Province,
				tag: 0
			}));
		});
		_this.fillItems(0, arr);
	};
	CitySelect.prototype.loadProvance = function() {
		var _this = this;
		var countryData = _this.$itemBox.eq(0).find('a.crt').data('citys');
		var arr = [];
		if(countryData == undefined) {
			arr.push();
		} else {
			$.each(countryData, function(k, v) {
				arr.push($('<a cid="' + v.ProvinceId + '" class="' + (v.ProvinceName == _this.defaultSet.provance ? 'crt' : '') + '" href="javascript:;"><span>' + v.ProvinceName + '</span></a>').data({
					citys: v.City,
					tag: 1
				}));
			});
		}
		_this.fillItems(1, arr);
	};
	CitySelect.prototype.loadCity = function() {
		var _this = this;
		var cityData = _this.$itemBox.eq(1).find('a.crt').data('citys');
		var arr = [];
		if(cityData == undefined) {
			arr.push();
		} else {
			$.each(cityData, function(k, v) {
				arr.push($('<a cid="' + v.CityId + '" class="' + (v.CityName == _this.defaultSet.city ? 'crt' : '') + '" href="javascript:;"><span>' + v.CityName + '</span></a>').data({
					citys: v.CountyList,
					tag: 2
				}));
			});
		}
		_this.fillItems(2, arr);
	};
	CitySelect.prototype.loadArea = function() {
		var _this = this;
		var areaData = _this.$itemBox.eq(2).find('a.crt').data('citys');
		var arr = [];
		if(areaData == undefined) {
			arr.push();
		} else {
			$.each(areaData, function(k, v) {
				arr.push($('<a cid="' + v.CountyId + '" class="' + (v.CountyName == _this.defaultSet.area ? 'crt' : '') + '" href="javascript:;"><span>' + v.CountyName + '</span></a>').data({
					tag: 3
				}));
			});
		}
		if(arr.length <= 0) {
			arr.push($('<a href="javascript:;"><span>全区</span></a>').data({
				tag: 3
			}));
		}
		_this.fillItems(3, arr);
	};

	function Plugin(option) {
		var args = Array.prototype.slice.call(arguments, 1);
		return this.each(function() {
			var $this = $(this),
				citySelect = $this.data('ydui.cityselect');
			if(!citySelect) {
				$this.data('ydui.cityselect', (citySelect = new CitySelect(this, option)));
			}
			if(typeof option == 'string') {
				citySelect[option] && citySelect[option].apply(citySelect, args);
			}
		});
	}
	$.fn.citySelect = Plugin;
}(window);;
(function() {
	'use strict';

	function FastClick(layer, options) {
		var oldOnClick;
		options = options || {};
		this.trackingClick = false;
		this.trackingClickStart = 0;
		this.targetElement = null;
		this.touchStartX = 0;
		this.touchStartY = 0;
		this.lastTouchIdentifier = 0;
		this.touchBoundary = options.touchBoundary || 10;
		this.layer = layer;
		this.tapDelay = options.tapDelay || 200;
		this.tapTimeout = options.tapTimeout || 700;
		if(FastClick.notNeeded(layer)) {
			return;
		}

		function bind(method, context) {
			return function() {
				return method.apply(context, arguments);
			};
		}
		var methods = ['onMouse', 'onClick', 'onTouchStart', 'onTouchMove', 'onTouchEnd', 'onTouchCancel'];
		var context = this;
		for(var i = 0, l = methods.length; i < l; i++) {
			context[methods[i]] = bind(context[methods[i]], context);
		}
		if(deviceIsAndroid) {
			layer.addEventListener('mouseover', this.onMouse, true);
			layer.addEventListener('mousedown', this.onMouse, true);
			layer.addEventListener('mouseup', this.onMouse, true);
		}
		layer.addEventListener('click', this.onClick, true);
		layer.addEventListener('touchstart', this.onTouchStart, false);
		layer.addEventListener('touchmove', this.onTouchMove, false);
		layer.addEventListener('touchend', this.onTouchEnd, false);
		layer.addEventListener('touchcancel', this.onTouchCancel, false);
		if(!Event.prototype.stopImmediatePropagation) {
			layer.removeEventListener = function(type, callback, capture) {
				var rmv = Node.prototype.removeEventListener;
				if(type === 'click') {
					rmv.call(layer, type, callback.hijacked || callback, capture);
				} else {
					rmv.call(layer, type, callback, capture);
				}
			};
			layer.addEventListener = function(type, callback, capture) {
				var adv = Node.prototype.addEventListener;
				if(type === 'click') {
					adv.call(layer, type, callback.hijacked || (callback.hijacked = function(event) {
						if(!event.propagationStopped) {
							callback(event);
						}
					}), capture);
				} else {
					adv.call(layer, type, callback, capture);
				}
			};
		}
		if(typeof layer.onclick === 'function') {
			oldOnClick = layer.onclick;
			layer.addEventListener('click', function(event) {
				oldOnClick(event);
			}, false);
			layer.onclick = null;
		}
	}
	var deviceIsWindowsPhone = navigator.userAgent.indexOf("Windows Phone") >= 0;
	var deviceIsAndroid = navigator.userAgent.indexOf('Android') > 0 && !deviceIsWindowsPhone;
	var deviceIsIOS = /iP(ad|hone|od)/.test(navigator.userAgent) && !deviceIsWindowsPhone;
	var deviceIsIOS4 = deviceIsIOS && (/OS 4_\d(_\d)?/).test(navigator.userAgent);
	var deviceIsIOSWithBadTarget = deviceIsIOS && (/OS [6-7]_\d/).test(navigator.userAgent);
	var deviceIsBlackBerry10 = navigator.userAgent.indexOf('BB10') > 0;
	FastClick.prototype.needsClick = function(target) {
		switch(target.nodeName.toLowerCase()) {
			case 'button':
			case 'select':
			case 'textarea':
				if(target.disabled) {
					return true;
				}
				break;
			case 'input':
				if((deviceIsIOS && target.type === 'file') || target.disabled) {
					return true;
				}
				break;
			case 'label':
			case 'iframe':
			case 'video':
				return true;
		}
		return(/\bneedsclick\b/).test(target.className);
	};
	FastClick.prototype.needsFocus = function(target) {
		switch(target.nodeName.toLowerCase()) {
			case 'textarea':
				return true;
			case 'select':
				return !deviceIsAndroid;
			case 'input':
				switch(target.type) {
					case 'button':
					case 'checkbox':
					case 'file':
					case 'image':
					case 'radio':
					case 'submit':
						return false;
				}
				return !target.disabled && !target.readOnly;
			default:
				return(/\bneedsfocus\b/).test(target.className);
		}
	};
	FastClick.prototype.sendClick = function(targetElement, event) {
		var clickEvent, touch;
		if(document.activeElement && document.activeElement !== targetElement) {
			document.activeElement.blur();
		}
		touch = event.changedTouches[0];
		clickEvent = document.createEvent('MouseEvents');
		clickEvent.initMouseEvent(this.determineEventType(targetElement), true, true, window, 1, touch.screenX, touch.screenY, touch.clientX, touch.clientY, false, false, false, false, 0, null);
		clickEvent.forwardedTouchEvent = true;
		targetElement.dispatchEvent(clickEvent);
	};
	FastClick.prototype.determineEventType = function(targetElement) {
		if(deviceIsAndroid && targetElement.tagName.toLowerCase() === 'select') {
			return 'mousedown';
		}
		return 'click';
	};
	FastClick.prototype.focus = function(targetElement) {
		var length;
		if(deviceIsIOS && targetElement.setSelectionRange && targetElement.type.indexOf('date') !== 0 && targetElement.type !== 'time' && targetElement.type !== 'month') {
			length = targetElement.value.length;
			targetElement.setSelectionRange(length, length);
		} else {
			targetElement.focus();
		}
	};
	FastClick.prototype.updateScrollParent = function(targetElement) {
		var scrollParent, parentElement;
		scrollParent = targetElement.fastClickScrollParent;
		if(!scrollParent || !scrollParent.contains(targetElement)) {
			parentElement = targetElement;
			do {
				if(parentElement.scrollHeight > parentElement.offsetHeight) {
					scrollParent = parentElement;
					targetElement.fastClickScrollParent = parentElement;
					break;
				}
				parentElement = parentElement.parentElement;
			} while (parentElement);
		}
		if(scrollParent) {
			scrollParent.fastClickLastScrollTop = scrollParent.scrollTop;
		}
	};
	FastClick.prototype.getTargetElementFromEventTarget = function(eventTarget) {
		if(eventTarget.nodeType === Node.TEXT_NODE) {
			return eventTarget.parentNode;
		}
		return eventTarget;
	};
	FastClick.prototype.onTouchStart = function(event) {
		var targetElement, touch, selection;
		if(event.targetTouches.length > 1) {
			return true;
		}
		targetElement = this.getTargetElementFromEventTarget(event.target);
		touch = event.targetTouches[0];
		if(deviceIsIOS) {
			selection = window.getSelection();
			if(selection.rangeCount && !selection.isCollapsed) {
				return true;
			}
			if(!deviceIsIOS4) {
				if(touch.identifier && touch.identifier === this.lastTouchIdentifier) {
					event.preventDefault();
					return false;
				}
				this.lastTouchIdentifier = touch.identifier;
				this.updateScrollParent(targetElement);
			}
		}
		this.trackingClick = true;
		this.trackingClickStart = event.timeStamp;
		this.targetElement = targetElement;
		this.touchStartX = touch.pageX;
		this.touchStartY = touch.pageY;
		if((event.timeStamp - this.lastClickTime) < this.tapDelay) {
			event.preventDefault();
		}
		return true;
	};
	FastClick.prototype.touchHasMoved = function(event) {
		var touch = event.changedTouches[0],
			boundary = this.touchBoundary;
		if(Math.abs(touch.pageX - this.touchStartX) > boundary || Math.abs(touch.pageY - this.touchStartY) > boundary) {
			return true;
		}
		return false;
	};
	FastClick.prototype.onTouchMove = function(event) {
		if(!this.trackingClick) {
			return true;
		}
		if(this.targetElement !== this.getTargetElementFromEventTarget(event.target) || this.touchHasMoved(event)) {
			this.trackingClick = false;
			this.targetElement = null;
		}
		return true;
	};
	FastClick.prototype.findControl = function(labelElement) {
		if(labelElement.control !== undefined) {
			return labelElement.control;
		}
		if(labelElement.htmlFor) {
			return document.getElementById(labelElement.htmlFor);
		}
		return labelElement.querySelector('button, input:not([type=hidden]), keygen, meter, output, progress, select, textarea');
	};
	FastClick.prototype.onTouchEnd = function(event) {
		var forElement, trackingClickStart, targetTagName, scrollParent, touch, targetElement = this.targetElement;
		if(!this.trackingClick) {
			return true;
		}
		if((event.timeStamp - this.lastClickTime) < this.tapDelay) {
			this.cancelNextClick = true;
			return true;
		}
		if((event.timeStamp - this.trackingClickStart) > this.tapTimeout) {
			return true;
		}
		this.cancelNextClick = false;
		this.lastClickTime = event.timeStamp;
		trackingClickStart = this.trackingClickStart;
		this.trackingClick = false;
		this.trackingClickStart = 0;
		if(deviceIsIOSWithBadTarget) {
			touch = event.changedTouches[0];
			targetElement = document.elementFromPoint(touch.pageX - window.pageXOffset, touch.pageY - window.pageYOffset) || targetElement;
			targetElement.fastClickScrollParent = this.targetElement.fastClickScrollParent;
		}
		targetTagName = targetElement.tagName.toLowerCase();
		if(targetTagName === 'label') {
			forElement = this.findControl(targetElement);
			if(forElement) {
				this.focus(targetElement);
				if(deviceIsAndroid) {
					return false;
				}
				targetElement = forElement;
			}
		} else if(this.needsFocus(targetElement)) {
			if((event.timeStamp - trackingClickStart) > 100 || (deviceIsIOS && window.top !== window && targetTagName === 'input')) {
				this.targetElement = null;
				return false;
			}
			this.focus(targetElement);
			this.sendClick(targetElement, event);
			if(!deviceIsIOS || targetTagName !== 'select') {
				this.targetElement = null;
				event.preventDefault();
			}
			return false;
		}
		if(deviceIsIOS && !deviceIsIOS4) {
			scrollParent = targetElement.fastClickScrollParent;
			if(scrollParent && scrollParent.fastClickLastScrollTop !== scrollParent.scrollTop) {
				return true;
			}
		}
		if(!this.needsClick(targetElement)) {
			event.preventDefault();
			this.sendClick(targetElement, event);
		}
		return false;
	};
	FastClick.prototype.onTouchCancel = function() {
		this.trackingClick = false;
		this.targetElement = null;
	};
	FastClick.prototype.onMouse = function(event) {
		if(!this.targetElement) {
			return true;
		}
		if(event.forwardedTouchEvent) {
			return true;
		}
		if(!event.cancelable) {
			return true;
		}
		if(!this.needsClick(this.targetElement) || this.cancelNextClick) {
			if(event.stopImmediatePropagation) {
				event.stopImmediatePropagation();
			} else {
				event.propagationStopped = true;
			}
			event.stopPropagation();
			event.preventDefault();
			return false;
		}
		return true;
	};
	FastClick.prototype.onClick = function(event) {
		var permitted;
		if(this.trackingClick) {
			this.targetElement = null;
			this.trackingClick = false;
			return true;
		}
		if(event.target.type === 'submit' && event.detail === 0) {
			return true;
		}
		permitted = this.onMouse(event);
		if(!permitted) {
			this.targetElement = null;
		}
		return permitted;
	};
	FastClick.prototype.destroy = function() {
		var layer = this.layer;
		if(deviceIsAndroid) {
			layer.removeEventListener('mouseover', this.onMouse, true);
			layer.removeEventListener('mousedown', this.onMouse, true);
			layer.removeEventListener('mouseup', this.onMouse, true);
		}
		layer.removeEventListener('click', this.onClick, true);
		layer.removeEventListener('touchstart', this.onTouchStart, false);
		layer.removeEventListener('touchmove', this.onTouchMove, false);
		layer.removeEventListener('touchend', this.onTouchEnd, false);
		layer.removeEventListener('touchcancel', this.onTouchCancel, false);
	};
	FastClick.notNeeded = function(layer) {
		var metaViewport;
		var chromeVersion;
		var blackberryVersion;
		var firefoxVersion;
		if(typeof window.ontouchstart === 'undefined') {
			return true;
		}
		chromeVersion = +(/Chrome\/([0-9]+)/.exec(navigator.userAgent) || [, 0])[1];
		if(chromeVersion) {
			if(deviceIsAndroid) {
				metaViewport = document.querySelector('meta[name=viewport]');
				if(metaViewport) {
					if(metaViewport.content.indexOf('user-scalable=no') !== -1) {
						return true;
					}
					if(chromeVersion > 31 && document.documentElement.scrollWidth <= window.outerWidth) {
						return true;
					}
				}
			} else {
				return true;
			}
		}
		if(deviceIsBlackBerry10) {
			blackberryVersion = navigator.userAgent.match(/Version\/([0-9]*)\.([0-9]*)/);
			if(blackberryVersion[1] >= 10 && blackberryVersion[2] >= 3) {
				metaViewport = document.querySelector('meta[name=viewport]');
				if(metaViewport) {
					if(metaViewport.content.indexOf('user-scalable=no') !== -1) {
						return true;
					}
					if(document.documentElement.scrollWidth <= window.outerWidth) {
						return true;
					}
				}
			}
		}
		if(layer.style.msTouchAction === 'none' || layer.style.touchAction === 'manipulation') {
			return true;
		}
		firefoxVersion = +(/Firefox\/([0-9]+)/.exec(navigator.userAgent) || [, 0])[1];
		if(firefoxVersion >= 27) {
			metaViewport = document.querySelector('meta[name=viewport]');
			if(metaViewport && (metaViewport.content.indexOf('user-scalable=no') !== -1 || document.documentElement.scrollWidth <= window.outerWidth)) {
				return true;
			}
		}
		if(layer.style.touchAction === 'none' || layer.style.touchAction === 'manipulation') {
			return true;
		}
		return false;
	};
	FastClick.attach = function(layer, options) {
		return new FastClick(layer, options);
	};
	if(typeof define === 'function' && typeof define.amd === 'object' && define.amd) {
		define(function() {
			return FastClick;
		});
	} else if(typeof module !== 'undefined' && module.exports) {
		module.exports = FastClick.attach;
		module.exports.FastClick = FastClick;
	} else {
		window.FastClick = FastClick;
	}
}());