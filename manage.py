
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlbbs import create_app
from exts import db

from apps.cms import models as cms_models

from apps.front import models as front_models

from apps.models import BannerModel, BoardModel

app = create_app()

cmsUser = cms_models.CMSUser
cmsRole = cms_models.CMSRole
cmsPermission = cms_models.CMSPersmission

FrontUser = front_models.FrontUser

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)

# shell创建一个用户
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = cmsUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')

# 将一个用户添加到某个组
@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = cmsUser.query.filter_by(email=email).first()
    if user:
        role = cmsRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加角色成功')
        else:
            print('没有这个角色')
    else:
        print('%s邮箱没有这个用户' % email)


@manager.command
def create_role():
    # 访问者
    visitor = cmsRole(name='访问者', des='只能观看数据，不能修改。')
    visitor.permissions = cmsPermission.VISITOR

    # 运营人员
    operator = cmsRole(name='运营者', des='修改个人信息，管理帖子，管理评论')
    operator.permissions = cmsPermission.VISITOR|cmsPermission.POSTER|cmsPermission.FRONTUSER|cmsPermission.COMMENTER

    # 管理员
    admin = cmsRole(name='管理员', des='拥有本系统所有权限')
    admin.permissions = cmsPermission.VISITOR|cmsPermission.POSTER|cmsPermission.FRONTUSER|cmsPermission.COMMENTER|cmsPermission.CMSUSER|cmsPermission.BOARDER|cmsPermission.BANNER

    # 开发者
    developer = cmsRole(name='开发者', des='开发人员专用角色')
    developer.permissions = cmsPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()

@manager.command
def test_permission():
    user = cmsUser.query.first()
    if user.has_permission(cmsPermission.VISITOR):
        print('%s 有访问者的权限' % user.username)
    else:
        print('%s 没有有访问者的权限' % user.username)

# 创建一个前台用户
@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)
    db.session.commit()



if __name__ == '__main__':
    manager.run()