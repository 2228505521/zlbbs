$(function () {
    $('#addboard-btn').click(function (event) {
        event.preventDefault();

        xtalert.alertOneInput({
            'text': '请输入版块名称',
            'placeholder': '版块名称',
            'confirmCallback': function (value) {
                zlajax.post({
                    'url': '/cms/addboard/',
                    'data': {
                        'name': value
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            xtalert.alertSuccess(data['message']);
                            xtalert.close();
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
});

$(function () {
    $('.editboard-btn').click(function (event) {
        event.preventDefault();

        var self = $(this);
        var tr = self.parent().parent();
        var name = tr.attr('data-name');
        var board_id = tr.attr('data-id');

        xtalert.alertOneInput({
            'text': '请修改版块名称',
            'placeholder': name,
            'confirmCallback': function (value) {
                zlajax.post({
                    'url': '/cms/upboard/',
                    'data': {
                        'name': value,
                        'board_id': board_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            xtalert.alertSuccess(data['message']);
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
});

$(function () {
    $('.deleteboard-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var tr = self.parent().parent();
        var board_id = tr.attr('data-id');

        xtalert.alertConfirm({
            'msg': '确认删除此版块？',
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/delboard/',
                    'data': {
                        'board_id': board_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            xtalert.alertSuccess(data['message']);
                            window.location.reload();
                        }
                        else {
                            xtalert.close();
                            xtalert.alertErrorToast(data['message']);
                        }
                    },
                    'fail': function (error) {
                        xtalert.alertNetworkError();
                    }
                });
            },
            'cancelCallback': function () {

            }
        });
    });
});