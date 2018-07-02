
from apps.forms import BaseForm
from wtforms import StringField, ValidationError, IntegerField
from wtforms.validators import InputRequired, regexp, Length, EqualTo
from utils.zlcache import cache

class SignUpForm(BaseForm):
    telephone = StringField(validators=[InputRequired(message='请输入手机号码'), regexp(r'1[345789]\d{9}', message='请输入正确的手机号码')])
    sms_captcha = StringField(validators=[regexp(r'\w{4}', message='请输入正确格式的短信验证码')])
    username = StringField(validators=[regexp(r'.{2,20}', message='请输入正确格式的用户名')])
    password1 = StringField(validators=[regexp(r'[0-9a-zA-Z_\.]{6,20}',message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo('password1', message='两次输入的密码不一致')])
    graph_captcha = StringField(validators=[regexp(r'\w{4}', message='图形验证码格式不正确')])

    def validate_sms_captcha(self, field):
        sms_captcha = field.data.strip()
        telephone = self.telephone.data.strip()
        sms_captcha_cache = cache.get(telephone)
        if not sms_captcha_cache or sms_captcha_cache.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码不正确')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data.strip()
        graph_captcha_cache = cache.get(graph_captcha)
        if not graph_captcha_cache:
            raise ValidationError(message='图形验证码错误')


class LoginForm(BaseForm):
    telephone = StringField(validators=[InputRequired(message='请输入手机号码'), regexp(r'1[345789]\d{9}', message='请输入正确的手机号码')])
    password = StringField(validators=[regexp(r'[0-9a-zA-Z_\.]{6,20}',message='请输入正确格式的密码！')])
    remember = StringField()


class PostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入版块id！')])

