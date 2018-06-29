
$(function () {
   $('#captcha_btn').click(function (event) {
       event.preventDefault();

       var inputEmail = $("input[name=email]").val();
       if (!inputEmail){
           xtalert.alertError('请输入邮箱')
       }
       else {
           zlajax.get({
               'url': '/cms/email_captcha/',
               'data': {
                   'email': inputEmail
               },
               'success': function (data) {
                   if (data['code'] === 200) {
                       xtalert.alertSuccess('验证码发送成功！')
                   }
                   else {
                       xtalert.alertError(data['message'])
                   }
               },
               'fail': function (error) {
                   xtalert.alertError('请求失败:'+error)
               }
           });
       }
   });
});

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();

        var emailE = $("input[name=email]");
        var captchaE = $("input[name=captcha]");

        console.log(emailE.val());
        console.log(captchaE.val());
        zlajax.post({
            'url': '/cms/resetemail/',
            'data': {
                'email': emailE.val(),
                'captcha': captchaE.val()
            },
            'success': function (data) {
                if (data['code'] === 200){
                    xtalert.alertSuccess('邮箱修改成功！');

                    emailE.val('');
                    captchaE.val('');
                }
                else {
                    xtalert.alertError(data['message']);
                }
            },
            'fail': function (error) {
                xtalert.alertError('请求失败：'+error);
            }
        });
    });
});