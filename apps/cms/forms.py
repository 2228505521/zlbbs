
from wtforms import Form, StringField, IntegerField, ValidationError
from wtforms.validators import Email, InputRequired, Length, EqualTo, NumberRange

from ..forms import BaseForm

from utils.zlcache import cache

from flask import g


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入有效长度的密码')])
    remember = IntegerField()


class RestPWDForm(BaseForm):
    old_password = StringField(validators=[Length(6, 20, message='请输入正确格式的原始密码'), InputRequired(message='原始密码不能为空')])
    new_password = StringField(validators=[Length(6, 20, message='请输入正确格式的新密码'), InputRequired(message='新密码不能为空')])
    rnew_password = StringField(validators=[EqualTo('new_password', message='两次密码不一致')])


class RestEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    captcha = StringField(validators=[Length(6, 6, message='请输入正确长度的验证码')])

    # 从memached中获取邮箱和验证码，对比是否一致
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data

        captcha_cache = cache.get(email)
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError(message='邮箱验证码错误')
        return True

    def validate_email(self, field):
        email = self.email.data
        if email == g.cms_user.email:
            raise ValidationError(message='邮箱不能设置为原始邮箱')


class AddBannerForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入轮播图名称')])
    img = StringField(validators=[InputRequired(message='请输入轮播图链接')])
    url = StringField(validators=[InputRequired(message='请输入轮播图跳转链接')])
    prioirty = IntegerField(validators=[InputRequired(message='请输入轮播图显示优先级')])


class UpdataBannerForm(AddBannerForm):
    banner_id = IntegerField(validators=[InputRequired(message='请输入轮播图的id!')])


class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入版块名称')])


class UpdateBoardForm(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message='请输入版块的id！'), NumberRange(1, max=100, message='版块id超出限制')])