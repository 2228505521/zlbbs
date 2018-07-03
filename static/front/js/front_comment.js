$(function () {
    var ue = UE.getEditor('editor', {
        'serverUrl': '/ueditor/upload/',
        'toolbars': [
            [
                'undo', //撤销
                'bold', //加粗
                'snapscreen', //截图
                'italic', //斜体
                'source', //源代码
                'blockquote', //引用
                'simpleupload', //单图上传
                'insertimage', //多图上传
                'emotion' //表情
            ]
        ]
    });
    ue.ready(function () {
        ue.setHeight(200);
    });
    window.ue = ue;
});

$(function () {
    $('#submit-btn').click(function (event) {
        event.preventDefault();

        var loginTag = $('#login-tag').attr('data-is-login');
        if (!loginTag) {
            window.location = '/front/login/'
        }
        else {
            var content = window.ue.getContent();
            var post_id = $('article[id="post-content"]').attr('data-id');

            zlajax.post({
                'url': '/front/addcomment/',
                'data': {
                    'content': content,
                    'post_id': post_id
                },
                'success': function (data) {
                    if (data['code'] === 200) {
                        xtalert.alertSuccess(data['message']);
                        ue.setContent('');
                        window.location.reload();
                    }
                    else {
                        xtalert.alertErrorToast(data['message']);
                    }
                },
                'fail': function (error) {
                    xtalert.alertNetworkError();
                }
            });
        }
    });
});