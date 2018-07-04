$(function () {
    $('.add-hl-btn').click(function (event) {
        event.preventDefault();

        var self = $(this);
        var trEn = self.parent().parent();
        var post_id = trEn.attr('data-id');

        if (self.text() === '加精') {
            xtalert.alertConfirm({
                'msg': '确定加入精华帖吗？',
                'confirmCallback': function () {
                    zlajax.post({
                        'url': '/cms/hpost/',
                        'data': {
                            'post_id': post_id
                        },
                        'success': function (data) {
                            if (data['code'] === 200) {
                                xtalert.alertSuccess(data['message']);
                                self.text('取消加精');
                            }
                            else {
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
        }
        else if (self.text() === '取消加精') {
            xtalert.alertConfirm({
                'msg': '确定取消精华帖吗？',
                'confirmCallback': function () {
                    zlajax.post({
                        'url': '/cms/uhpost/',
                        'data': {
                            'post_id': post_id
                        },
                        'success': function (data) {
                            if (data['code'] === 200) {
                                xtalert.alertSuccess(data['message']);
                                self.text('加精');
                            }
                            else {
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
        }
    });
});

$(function () {
    $('.cel-hl-btn').click(function (event) {
        event.preventDefault();

        var self = $(this);
        var trEn = self.parent().parent();
        var post_id = trEn.attr('data-id');

        xtalert.alertConfirm({
            'msg': '确定删除帖子吗？',
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/dhpost/',
                    'data': {
                        'post_id': post_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            xtalert.alertSuccess(data['message']);
                            setTimeout(function () {
                                window.location.reload();
                            }, 500);
                        }
                        else {
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