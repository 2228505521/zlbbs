import os

# 设置数据库
DEBUG = True

DB_URI = r"mysql+pymysql://root:781066@127.0.0.1:3306/zlbbs?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# PERMANENT_SESSION_LIFETIME = 1

# 设置密匙
SECRET_KEY = r'{\xbf\x8a\xaf\xb5\x18\x89~\x0f\xc6cE$VRb\xdd\xfce\x87\x1b}y\xd7'

CMS_USER_ID = 'abababfd'
FRONT_USER_ID = 'SDFSDF'

# 设置flask-mail相关配置

# 发送者邮箱的服务器地址 default ‘localhost’
MAIL_SERVER = 'smtp.163.com' #smtp.qq.com
# 端口号 default 25
MAIL_PORT = '465'
# MAIL_USE_TLS: 端口号587 MAIL_PORT设置的什么就在哪个上面设置true
# MAIL_USE_SSL: 端口号465
MAIL_USE_SSL = True
# 发送邮件的用户名
MAIL_USERNAME = '18600764994@163.com'
# 唯一授权码
MAIL_PASSWORD = '0000000000qQ'# nyzwnvsvomaxecfg
# 默认发送用户
MAIL_DEFAULT_SENDER = '18600764994@163.com'

# 阿里大于相关配置
ALIDAYU_APP_KEY = '23709557'#LTAIJsWj1hZncOaX
ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'#ZjWkfyb8CbRbu1zdPN4DcidC2Hi0UV
ALIDAYU_SIGN_NAME = '小饭桌应用'#程佳俊
ALIDAYU_TEMPLATE_CODE = 'SMS_68465012'#SMS_137550462

# ueditor相关配置
# UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "a3KafHAOJy_WPOuoV8dqTT4VvMWuhq9QNAFzD7tx"
UEDITOR_QINIU_SECRET_KEY = "W8lA713_lha9rt9mX4its0WWAPTWJWC4LiDcY8Yg"
UEDITOR_QINIU_BUCKET_NAME = "jackie-cheng"
UEDITOR_QINIU_DOMAIN = "http://paywzwgr1.bkt.clouddn.com/"