$(function () {
    $("#submit").click(function (event) {
        //阻止按钮默认提交表单的事件
        event.preventDefault();

        var oldpwdE = $("input[name=old_password]");
        var newpwdE = $("input[name=new_password]");
        var rnewpwdE = $("input[name=rnew_password]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var rnewpwd = rnewpwdE.val();

        // 1. 要在模板的meta标签中渲染一个csrf-token
        // 2. 在ajax请求的头部中设置x-CSRFToken
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'old_password': oldpwd,
                'new_password': newpwd,
                'rnew_password': rnewpwd
            },
            'success': function (data) {
                if (data["code"] === 200) {
                    xtalert.alertSuccess("修改成功！");

                    oldpwdE.val("");
                    newpwdE.val("");
                    rnewpwdE.val("");

                }
                else {
                    xtalert.alertError(data["message"]);
                }
            },
            'fail': function (error) {
                xtalert.alertError("网络错误！")
            }
        });
    });
});