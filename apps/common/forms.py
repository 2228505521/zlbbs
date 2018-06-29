
from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, InputRequired
import hashlib

class SMSCaptchaForm(BaseForm):
    salt = 'sdfskdflskfjslaseir'
    telephone = StringField(validators=[regexp(r'1[345789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        # 重写父类方法, 如果父类的方法都失败了，那么直接返回False
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False

        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        # md5(timestamp+telephone+salt)
        # md5函数必须要传一个bytes类型的字符串进去
        sign2 = hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest()
        if sign2 == sign:
            return True
        else:
            return False

