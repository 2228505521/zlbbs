from flask import Blueprint, request, make_response, jsonify
from utils import restful
from static.common.sms_alidayu import sms_alidayu
from utils.captcha import Captcha
import json
from .forms import SMSCaptchaForm
from utils.zlcache import cache

from utils.captcha import Captcha
from io import BytesIO
import qiniu

# celery异步发送短息
from tasks import send_captcha

bp = Blueprint('common', __name__, url_prefix='/com')

# 图形验证码
@bp.route('/captcha/')
def graph_captcha():
    # 获取到生成的验证码的图片
    text, image = Captcha.gene_graph_captcha()
    # 存储图形验证码到内存
    cache.set(text.lower(), text.lower())
    # 将图片转换成二进制流的形式，使用make_response包装成浏览器可以识别的图片
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp # 返回一张二进制表示的图片


# 参数未加密版本
# @bp.route('/sms_captcha/')
# def smsCaptcha():
#     telephone = request.args.get('telephone')
#     if not telephone:
#         return restful.params_error('请传入手机号码')
#     captcha = Captcha.gene_text(4)
#     print(captcha)
#     resp = json.loads(sms_alidayu.send_sms(telephone, template_param=u"{'code':'%s'}" % captcha))
#     if resp.get('Code') == 'OK':
#         return restful.success('发送成功')
#     else:
#         return restful.params_error(message='验证码发送失败')

# 参数加密版本
@bp.route('/sms_captcha/', methods=['POST'])
def smsCaptcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(4)
        # sms_alidayu.send_sms(telephone, template_param=u"{'code':'%s'}" % captcha)
        # send_captcha(telephone, template_param=u"{'code':'%s'}" % captcha)
        resp = json.loads(send_captcha(telephone, template_param=u"{'code':'%s'}" % captcha))
        print(resp)
        if resp.get('Code') == 'OK':
            # 保存验证码到内存中
            cache.set(telephone, captcha.lower())

            return restful.success('发送成功')
        else:
            return restful.params_error(message='验证码发送失败')
    else:
        return restful.params_error(message='参数错误！')


# 初始化七牛后台服务
@bp.route('/uptoken/')
def uptoken():
    AK = 'a3KafHAOJy_WPOuoV8dqTT4VvMWuhq9QNAFzD7tx'
    SK = 'W8lA713_lha9rt9mX4its0WWAPTWJWC4LiDcY8Yg'
    q = qiniu.Auth(AK, SK)
    bucket = 'jackie-cheng'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})