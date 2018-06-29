$(function () {
    $('#submit-btn').click(function (event) {
        event.preventDefault();

        var telephone_input = $("input[name='telephone']");
        var password_input = $("input[name='password']");
        var remember_checkbox = $("input[name='remember']");

        var telephone = telephone_input.val();
        var password = password_input.val();
        var remember = remember_checkbox.checked?1:0;
        zlajax.post({
            'url': '/front/login/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember
            },
            'success': function (data) {
                if (data['code'] === 200){
                    var return_to = $('#return-to-url').text();
                    if (return_to) {
                        window.location = return_to;
                    }
                    else {
                        window.location = '/front/index/';
                    }
                }
                else {
                    xtalert.alertInfoToast(data['message']);
                }
            }
        });

    });
});