from flask import Flask
import config
from exts import db, mail
from apps.cms import bp as cms_bp
from apps.common import bp as com_bp
from apps.front import bp as front_bp
from flask_wtf import CSRFProtect
from apps.front.ueditor import bp as editor_bp
from utils.captcha import Captcha

from os import urandom

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    mail.init_app(app)

    # 设置csrf保护
    CSRFProtect(app)

    app.register_blueprint(cms_bp)
    app.register_blueprint(com_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(editor_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
