$(function () {
    $('#save-banner-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var banner_dialog = $("#banner-dialog");
        var nameInput = $("input[name='name']");
        var imageInput = $("input[name='img']");
        var urlInput = $("input[name='url']");
        var prioirtyInput = $("input[name='prioirty']");

        var name = nameInput.val();
        var img = imageInput.val();
        var url = urlInput.val();
        var prioirty = prioirtyInput.val();
        var submitType = self.attr('data-type');
        var banner_id = self.attr('data-id');

        var myurl = '';
        if (submitType === 'update') {
            myurl = '/cms/upbanner/'
        }
        else {
            myurl = '/cms/addbanner/'
        }

        if (!name || !img || !url || !prioirty) {
            xtalert.alertErrorToast('请完善信息');
            return;
        }
        else {
            zlajax.post({
                'url': myurl,
                'data': {
                    'name': name,
                    'img': img,
                    'url': url,
                    'prioirty': prioirty,
                    'banner_id': banner_id
                },
                'success': function (data) {
                    if (data['code'] === 200) {
                        banner_dialog.modal('hide');
                        xtalert.alertSuccess(data['message'] ? data['message'] : '编辑成功');
                        window.location.reload();
                    }
                    else {
                        xtalert.alertErrorToast(data['message'])
                    }
                },
                'fail': function (error) {
                    xtalert.alertNetworkError()
                }
            });
        }
    });
});

$(function () {
    $('.edit-banner-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $('#banner-dialog');
        dialog.modal('show');

        var tr = self.parent().parent();
        var name = tr.attr('data-name');
        var image = tr.attr('data-image');
        var url = tr.attr('data-url');
        var prioirty = tr.attr('data-prioirty');

        var nameInput = dialog.find("input[name='name']");
        var imageInput = dialog.find("input[name='img']");
        var urlInput = dialog.find("input[name='url']");
        var prioirtyInput = dialog.find("input[name='prioirty']");
        var saveBtn = dialog.find("#save-banner-btn");

        nameInput.val(name);
        imageInput.val(image);
        urlInput.val(url);
        prioirtyInput.val(prioirty);
        saveBtn.attr("data-type", 'update');
        saveBtn.attr('data-id', tr.attr('data-id'));

    });
});

$(function () {
    $('.delete-banner-btn').click(function (event) {
        event.preventDefault();

        var self = $(this);
        var tr = self.parent().parent();
        var banner_id = tr.attr('data-id');

        xtalert.alertConfirm({
            'msg': '您确定要删除这个轮播图吗？',
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/delbanner/',
                    'data': {
                        'banner_id': banner_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            xtalert.alertSuccess('删除成功！');
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
            },
            'cancelCallback': function () {
            }
        });
    });
});

$(function () {
    zlqiniu.setUp({
        'domain': 'http://paywzwgr1.bkt.clouddn.com/',
        'browse_btn': 'upload-btn',
        'uptoken_url': '/com/uptoken/',
        'success': function (up, file, info) {
            console.log('上传结果：', file);

            var imageInput = $("input[name='img']");
            imageInput.val(file['name']);

        }
    });
});