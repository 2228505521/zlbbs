
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class CMSPersmission(object):
    # 超级管理员
    ALL_PERMISSION =    0b11111111
    # 访问者权限
    VISITOR =           0b00000001
    # 管理帖子权限
    POSTER =            0b00000010
    # 管理评论权限
    COMMENTER =         0b00000100
    # 管理板块权限
    BOARDER =           0b00001000
    # 管理前台用户权限
    FRONTUSER =         0b00010000
    # 管理后台用户权限
    CMSUSER =           0b00100000
    # 管理banner权限
    BANNER =            0b01000000
    # 管理后台管理员的权限
    ADMINER =           0b10000000

cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    des = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)

    users = db.relationship('CMSUser', secondary='cms_role_user', backref='roles')


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        # 设置密码的同时进行密码加密
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        # 判断加密后的密码和原来的密码是否一致
        print('原密码：{} 加密：{} 新密码：{}'.format(self._password,self.password, raw_password))
        result = check_password_hash(self._password, raw_password)
        return result

    # 从模型中找到用户所有的权限
    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    # 判断这个是否有某个权限
    def has_permission(self, permission):
        return (self.permissions&permission) == permission

    # 判断该用户是否是开发者
    def is_developer(self):
        return self.has_permission(CMSPersmission.ALL_PERMISSION)



# 密码对外的字段名叫做password
# 密码对内的字段名叫做_password