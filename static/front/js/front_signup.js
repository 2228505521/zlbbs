// 随机变化图形验证码
$(function () {
    $('#captcha_img').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var src = self.attr('src');
        var imgTag = $(this).children('img');
        var oldSrc = imgTag.attr('src');
        var href = xtparam.setParam(oldSrc, 'xx', Math.random());
        imgTag.attr('src', href);
    });
});

/*
$(function () {
    $('#sms-captcha-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var telephone = $("input[name='telephone']").val();
        if (!(/^1[345789]\d{9}$/.test(telephone))) {
            xtalert.alertErrorToast('请输入正确的手机号码');
            return;
        }
        var timestamp = (new Date).getTime();
        var sign = md5(timestamp+telephone+'sdfskdflskfjslaseir');
        zlajax.post({
            'url': "/com/sms_captcha/",
            'data': {
                'telephone': telephone,
                'timestamp': timestamp,
                'sign': sign
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    xtalert.alertSuccess('验证码发送成功');
                    //禁止按钮点击
                    self.attr('disabled', 'disabled');
                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;
                        self.text(timeCount);
                        if (timeCount<=0) {
                            self.removeAttr('disabled');
                            clearInterval(timer);
                            self.text('发送验证码');
                        }
                    }, 1000);
                }
                else {
                    xtalert.alertInfoWithTitle('提示', data['message']);
                }
            },
            'fail': function (error) {
                xtalert.alertError(error.des);
            }
        });
    });
});

*/

// 发送短信验证码给后台
// js代码加密和混淆
$(function () {
    window["\x65\x76\x61\x6c"](function (sKctiJrpL1, gpQzbs$s2, bZAksMPPc3, kW4, z$L5, WGhstFNh6) {
        z$L5 = function (bZAksMPPc3) {
            return bZAksMPPc3['\x74\x6f\x53\x74\x72\x69\x6e\x67'](36)
        };
        if ('\x30'['\x72\x65\x70\x6c\x61\x63\x65'](0, z$L5) == 0) {
            while (bZAksMPPc3--) WGhstFNh6[z$L5(bZAksMPPc3)] = kW4[bZAksMPPc3];
            kW4 = [function (z$L5) {
                return WGhstFNh6[z$L5] || z$L5
            }];
            z$L5 = function () {
                return '\x5b\x32\x2d\x38\x61\x2d\x63\x65\x2d\x69\x5d'
            };
            bZAksMPPc3 = 1
        }
        ;
        while (bZAksMPPc3--) if (kW4[bZAksMPPc3]) sKctiJrpL1 = sKctiJrpL1['\x72\x65\x70\x6c\x61\x63\x65'](new window["\x52\x65\x67\x45\x78\x70"]('\\\x62' + z$L5(bZAksMPPc3) + '\\\x62', '\x67'), kW4[bZAksMPPc3]);
        return sKctiJrpL1
    }('\x24\x28\x34\x28\x29\x7b\x24\x28\'\x23\x73\x6d\x73\x2d\x63\x61\x70\x74\x63\x68\x61\x2d\x62\x74\x6e\'\x29\x2e\x63\x6c\x69\x63\x6b\x28\x34\x28\x66\x29\x7b\x66\x2e\x70\x72\x65\x76\x65\x6e\x74\x44\x65\x66\x61\x75\x6c\x74\x28\x29\x3b\x32 \x35\x3d\x24\x28\x74\x68\x69\x73\x29\x3b\x32 \x33\x3d\x24\x28\x22\x69\x6e\x70\x75\x74\x5b\x6e\x61\x6d\x65\x3d\'\x33\'\x5d\x22\x29\x2e\x76\x61\x6c\x28\x29\x3b\x62\x28\x21\x28\x2f\x5e\x31\x5b\x33\x34\x35\x37\x38\x39\x5d\\\x64\x7b\x39\x7d\x24\x2f\x2e\x74\x65\x73\x74\x28\x33\x29\x29\x29\x7b\x36\x2e\x61\x6c\x65\x72\x74\x45\x72\x72\x6f\x72\x54\x6f\x61\x73\x74\x28\'\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u624b\u673a\u53f7\u7801\'\x29\x3b\x72\x65\x74\x75\x72\x6e\x7d\x32 \x37\x3d\x28\x6e\x65\x77 \x44\x61\x74\x65\x29\x2e\x67\x65\x74\x54\x69\x6d\x65\x28\x29\x3b\x32 \x63\x3d\x6d\x64\x35\x28\x37\x2b\x33\x2b\'\x73\x64\x66\x73\x6b\x64\x66\x6c\x73\x6b\x66\x6a\x73\x6c\x61\x73\x65\x69\x72\'\x29\x3b\x7a\x6c\x61\x6a\x61\x78\x2e\x70\x6f\x73\x74\x28\x7b\'\x75\x72\x6c\'\x3a\x22\x2f\x63\x6f\x6d\x2f\x73\x6d\x73\x5f\x63\x61\x70\x74\x63\x68\x61\x2f\x22\x2c\'\x38\'\x3a\x7b\'\x33\'\x3a\x33\x2c\'\x37\'\x3a\x37\x2c\'\x63\'\x3a\x63\x7d\x2c\'\x73\x75\x63\x63\x65\x73\x73\'\x3a\x34\x28\x38\x29\x7b\x62\x28\x38\x5b\'\x63\x6f\x64\x65\'\x5d\x3d\x3d\x3d\x32\x30\x30\x29\x7b\x36\x2e\x61\x6c\x65\x72\x74\x53\x75\x63\x63\x65\x73\x73\x28\'\u9a8c\u8bc1\u7801\u53d1\u9001\u6210\u529f\'\x29\x3b\x35\x2e\x61\x74\x74\x72\x28\'\x65\'\x2c\'\x65\'\x29\x3b\x32 \x61\x3d\x36\x30\x3b\x32 \x67\x3d\x73\x65\x74\x49\x6e\x74\x65\x72\x76\x61\x6c\x28\x34\x28\x29\x7b\x61\x2d\x2d\x3b\x35\x2e\x68\x28\x61\x29\x3b\x62\x28\x61\x3c\x3d\x30\x29\x7b\x35\x2e\x72\x65\x6d\x6f\x76\x65\x41\x74\x74\x72\x28\'\x65\'\x29\x3b\x63\x6c\x65\x61\x72\x49\x6e\x74\x65\x72\x76\x61\x6c\x28\x67\x29\x3b\x35\x2e\x68\x28\'\u53d1\u9001\u9a8c\u8bc1\u7801\'\x29\x7d\x7d\x2c\x31\x30\x30\x30\x29\x7d\x65\x6c\x73\x65\x7b\x36\x2e\x61\x6c\x65\x72\x74\x49\x6e\x66\x6f\x57\x69\x74\x68\x54\x69\x74\x6c\x65\x28\'\u63d0\u793a\'\x2c\x38\x5b\'\x6d\x65\x73\x73\x61\x67\x65\'\x5d\x29\x7d\x7d\x2c\'\x66\x61\x69\x6c\'\x3a\x34\x28\x69\x29\x7b\x36\x2e\x61\x6c\x65\x72\x74\x45\x72\x72\x6f\x72\x28\x69\x2e\x64\x65\x73\x29\x7d\x7d\x29\x7d\x29\x7d\x29\x3b', [], 19, '\x7c\x7c\x76\x61\x72\x7c\x74\x65\x6c\x65\x70\x68\x6f\x6e\x65\x7c\x66\x75\x6e\x63\x74\x69\x6f\x6e\x7c\x73\x65\x6c\x66\x7c\x78\x74\x61\x6c\x65\x72\x74\x7c\x74\x69\x6d\x65\x73\x74\x61\x6d\x70\x7c\x64\x61\x74\x61\x7c\x7c\x74\x69\x6d\x65\x43\x6f\x75\x6e\x74\x7c\x69\x66\x7c\x73\x69\x67\x6e\x7c\x7c\x64\x69\x73\x61\x62\x6c\x65\x64\x7c\x65\x76\x65\x6e\x74\x7c\x74\x69\x6d\x65\x72\x7c\x74\x65\x78\x74\x7c\x65\x72\x72\x6f\x72'['\x73\x70\x6c\x69\x74']('\x7c'), 0, {}))
});

// 点击立即注册按钮
$(function () {
    $('#submit-btn').click(function (event) {
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var sms_captcha_input = $("input[name='sms_captcha']");
        var username_input = $("input[name='username']");
        var password1_input = $("input[name='password1']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']");

        var telephone = telephone_input.val();
        var sms_captcha = sms_captcha_input.val();
        var username = username_input.val();
        var password1 = password1_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        if (!(/^1[345789]\d{9}$/.test(telephone))) {
            xtalert.alertErrorToast('手机号码不正确');
            return;
        }
        if (!(/\w{4}/.test(sms_captcha))) {
            xtalert.alertErrorToast('短信验证码格式不正确');
            return;
        }
        if (!username) {
            xtalert.alertErrorToast('用户名不能为空');
            return;
        }
        if (!password1) {
            xtalert.alertErrorToast('密码不能为空');
            return;
        }
        if (password1 !== password2) {
            xtalert.alertErrorToast('密码不一致');
            return;
        }
        if (!(/\w{4}/.test(graph_captcha)) && !graph_captcha) {
            xtalert.alertErrorToast('图形验证码格式不正确');
            return;
        }

        zlajax.post({
            'url': '/front/signup/',
            'data': {
                'telephone': telephone,
                'sms_captcha': sms_captcha,
                'username': username,
                'password1': password1,
                'password2': password2,
                'graph_captcha': graph_captcha
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    xtalert.alertSuccess('注册成功');

                    var return_to_url = $('#return-to-url').text();
                    if (return_to_url) {
                        window.location = return_to_url
                    }
                    else {
                        window.location = '/front/index/';
                    }
                }
                else {
                    xtalert.alertInfoWithTitle('提示', data['message'])
                }
            },
            'fail': function () {
                xtalert.alertNetworkError();
            }
        });

    });
});