$(function () {
    var ue = UE.getEditor('editor');

    $('#submit-btn').click(function (event) {
        event.preventDefault();

        var titleInput = $("input[name='title']");
        var selectB = $("select[name='board_id']");

        var title = titleInput.val();
        var board_id = selectB.val();

        var content = ue.getContent();

        if (!title || !board_id || !content){
            xtalert.alertInfoToast('请完善相关信息！');
            return;
        }

        zlajax.post({
            'url': '/front/post/',
            'data': {
                'title': title,
                'content': content,
                'board_id': board_id
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    xtalert.alertConfirm({
                        'msg': '帖子发送成功，是否再发一篇？',
                        'confirmText': '再发一篇',
                        'cancelText': '返回首页',
                        'confirmCallback': function () {
                            titleInput.val('');
                            ue.clean();
                            selectB.selectByIndex(0);
                        },
                        'cancelCallback': function () {
                            window.location = '/front/index/'
                        }
                    });
                }
                else {
                    xtalert.alertErrorToast(data['message']);
                }
            },
            'fail': function (error) {
                xtalert.alertNetworkError();
            }
        });
    });
});