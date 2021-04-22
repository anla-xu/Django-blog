//登录操作
$(document).ready(function(){
if(screen.width < 780 && $(window).width() < 780)
{
	$(".content_list").hide();

}else{
	$(".content_list").show();
}
     $(window).resize(function(){	
	 $(".content_list").show();
	 });
});
//登录操作
var validCode=true;
function cliLogin() {
	var txtUser = $.trim($("#username").val());
	var txtPwd = $("#password").val();

	if ($.trim(txtUser) == "") {

		Tip('请输入用户名');
		$("#txtUser").focus();
		return;

	}
	if ($.trim(txtPwd) == "") {
		Tip('请输入密码！');
		$("#Userpwd").focus();
		return;
	}

	$('#form_login').submit();
	return false;
}
//注册操作
function Sendpwd() {
	var txtUser = $.trim($("#username").val());
	var txtPwd = $("#password").val();
	var txtPwd1 = $("#password1").val();
	var txtemail = $("#email").val();

	if ($.trim(txtUser) == "") {

		Tip('请输入用户名');
		$("#txtUser").focus();
		return;

	}
	if ($.trim(txtPwd) == "") {
		Tip('请输入密码！');
		$("#password").focus();
		return;
	}
	else if($.trim(txtPwd).length <6 || $.trim(txtPwd).length>16) {
		Tip('密码允许长度为6-14！');
		$("#password").focus();
		return;
	}
	else if($.trim(txtPwd).indexOf(" ") != -1){
		Tip('密码不允许有空格！');
		$("#password").focus();
		return;
	}
    if ($.trim(txtPwd1) == "") {

        Tip('请再次输入密码！');
        $("#txtPwd1").focus();
        return;

    }
    if ($.trim(txtPwd1) != $.trim(txtPwd)) {

        Tip('密码不一致，请重新输入！');
        $("#txtPwd1").focus();
        return;
    }
    if ($.trim(txtemail) == "") {

        Tip('请输入邮箱！');

		$("#txtemail").focus();
        return;

    }
    var reg = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
	if(!reg.test(txtemail)){
		Tip('邮箱格式不正确！');
		$("#email").focus();
        return;
	}

	$('#form_login').submit();
	return false;
}

// 重置密码
function Findpwd1(val) {
	var txtUser = $.trim($("#username").val());
	if ($.trim(txtUser) == "") {

		Tip('请输入用户名');
		$("#username").focus();
		return;
	}
	sessionStorage.setItem('send','True');
	$('#form_login').submit();
	return false;

}



function Findpwd2() {
	var txtUser = $.trim($("#username").val());
	var txtPwd = $("#password").val();
	var txtPwd1 = $("#password1").val();
	var txtcode = $("#auth_code").val();
	if ($.trim(txtUser) == "") {

		Tip('请输入用户名');
		$("#username").focus();
		return;
	}
	if ($.trim(txtPwd) == "") {
		Tip('请输入密码！');
		$("#Userpwd").focus();
		return;
	}
    if ($.trim(txtPwd1) == "") {

        Tip('请再次输入密码！');
        $("#txtPwd1").focus();
        return;

    }
    if ($.trim(txtPwd1) != $.trim(txtPwd)) {

        Tip('密码不一致，请重新输入！');
        $("#txtPwd1").focus();
        return;
    }
	if ($.trim(txtcode) == "") {

        Tip('请输入验证码！');
        $("#txtPwd1").focus();
        return;
    }
	$('#form_login').submit();
	return false;

}




// function Tip(msg) {
// 	$(".tishi").show().html("<div class='prompt'><i class='tishi_icon'></i>"+msg+"</div>");
// }
function Tip(msg) {
	$(".tishi").show().html("<div class='prompt'><i class='tishi_icon'></i>"+msg+"</div>");
}

jQuery(function(){
	"use strict";
		$(".navList .navLi").hover(function(){
		$(this).addClass("active");
		$(this).find(".navSub").stop().slideDown();	
	},function(){
		$(this).removeClass("active");
		$(this).find(".navSub").stop().slideUp();
		$(".navThrList").slideUp();
		$(".navFouList").slideUp();
	});
	function scro(){
			if($(document).scrollTop()>50){$(".headerbg").addClass("active");}else{$(".headerbg").removeClass("active");}
		}
		scro();
		$(window).scroll(function(){
			scro();
		});
			$(".benefits_name").hover(function(){
			$(this).addClass("hover");
			$(this).stop().animate({bottom: "0px", opacity:1 , height:"400px"}, "fast");
		},function(){
			$(this).removeClass("hover");
			$(this).stop().animate({bottom: "0px", opacity:1 , height:"400px"}, "fast") ; 			
		}
	);
		$(".Program_name ").hover(function() {
	    $(this).addClass("hover");
		$(this).find(".Program_title").stop()
		.animate({ opacity:1 , height:"100%"}, "fast")
		.css("display","block");

	}, function() {
	    $(this).removeClass("hover");  
		$(this).find(".Program_title").stop()
		.animate({ opacity: 1,height:"40px"}, "fast")
		.css("display","block");
	});
		$(".user_casestyle").hover(function(){
			$(this).addClass("hover");
			$(this).find(".hd a").css("display","block");
			//$(this).stop().animate({bottom: "0px", opacity:1 , height:""}, "fast")
		},function(){
			$(this).removeClass("hover");
			$(this).find(".hd a").css("display","none");
			//$(this).stop().animate({bottom: "0px", opacity:1 , height:""}, "fast")  			
		}
	);
	//置顶图标显示
$('#top-back').hide();
$(window).scroll(function(){
	 if($(this).scrollTop() > 350){
		$("#top-back").fadeIn();
	 }
	 else{
		$("#top-back").fadeOut();
	 }
  });
$(".bannerNimg").css("background-image", "url(" + $(".bannerNimg").find("img").attr("src") + ")");
//置顶事件
function topBack(){
  $('body,html').animate({scrollTop:0},300);
}
});

$.fn.countTo = function (options) {
	"use strict";
	options = options || {};	
	return $(this).each(function () {
		// set options for current element
		var settings = $.extend({}, $.fn.countTo.defaults, {
			from:            $(this).data('from'),
			to:              $(this).data('to'),
			speed:           $(this).data('speed'),
			refreshInterval: $(this).data('refresh-interval'),
			decimals:        $(this).data('decimals')
		}, options);
		
		// how many times to update the value, and how much to increment the value on each update
		var loops = Math.ceil(settings.speed / settings.refreshInterval),
			increment = (settings.to - settings.from) / loops;
		
		// references & variables that will change with each update
		var self = this,
			$self = $(this),
			loopCount = 0,
			value = settings.from,
			data = $self.data('countTo') || {};
		
		$self.data('countTo', data);
		
		// if an existing interval can be found, clear it first
		if (data.interval) {
			clearInterval(data.interval);
		}
		data.interval = setInterval(updateTimer, settings.refreshInterval);
		
		// initialize the element with the starting value
		render(value);
		
		function updateTimer() {
			value += increment;
			loopCount++;
			
			render(value);
			
			if (typeof(settings.onUpdate) == 'function') {
				settings.onUpdate.call(self, value);
			}
			
			if (loopCount >= loops) {
				// remove the interval
				$self.removeData('countTo');
				clearInterval(data.interval);
				value = settings.to;
				
				if (typeof(settings.onComplete) == 'function') {
					settings.onComplete.call(self, value);
				}
			}
		}
		
		function render(value) {
			var formattedValue = settings.formatter.call(self, value, settings);
			$self.html(formattedValue);
		}
	});
};

$.fn.countTo.defaults = {
	from: 0,               // the number the element should start at
	to: 0,                 // the number the element should end at
	speed: 300,           // how long it should take to count between the target numbers
	refreshInterval: 100,  // how often the element should be updated
	decimals: 0,           // the number of decimal places to show
	formatter: formatter,  // handler for formatting the value before rendering
	onUpdate: null,        // callback method for every time the element is updated
	onComplete: null       // callback method for when the element finishes updating
};

function formatter(value, settings) {
	return value.toFixed(settings.decimals);
}


