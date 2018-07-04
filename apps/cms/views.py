from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    redirect,
    url_for,
    g,
    jsonify
)

from .models import CMSUser, CMSPersmission
from ..models import BannerModel, BoardModel, PostModel, HeighLightPostModel
from .forms import (
    LoginForm,
    RestPWDForm,
    RestEmailForm,
    AddBannerForm,
    UpdataBannerForm,
    AddBoardForm,
    UpdateBoardForm
)
from .decorators import login_required, permission_required
import config
from exts import db, mail
from utils import restful
# 发送邮件
from flask_mail import Message
import string
import random
from utils.zlcache import cache
from flask_paginate import get_page_parameter, Pagination

# celery异步执行发送邮件
from tasks import send_mail

bp = Blueprint('cms', __name__, url_prefix='/cms')


# 路由必须在第一位
@bp.route('/index/')
@login_required
def index():
    return render_template('cms/cms_index.html')


# 个人信息接口
@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


# 登录接口
class LoginView(views.MethodView):
    def get(self, message=None):
        content = {
            'message': message
        }
        return render_template('cms/cms_login.html', content=content)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = request.form.get('email')
            password = request.form.get('password')
            remember = request.form.get('remember')

            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 如果设置permanent为True则过期时间变为31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或密码错误')

        else:
            message = form.errors.popitem()[1][0]
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'), endpoint='login')


# 登出接口
class LoginOutView(views.MethodView):
    decorators = [login_required]

    def get(self):
        del session[config.CMS_USER_ID]
        if config.CMS_USER_ID not in session:
            print('注销成功！')
        return redirect(url_for('cms.login'))


bp.add_url_rule('/loginout/', view_func=LoginOutView.as_view('loginout'), endpoint='loginout')


# 修改密码接口
class RestPWDView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/rest_pwd.html')

    def post(self):
        form = RestPWDForm(request.form)
        if form.validate():
            pwd = form.old_password.data
            newpwd = form.new_password.data
            user = g.cms_user
            if user.check_password(pwd):
                user.password = newpwd
                db.session.commit()

                return restful.success()
            else:
                return restful.params_error("原始密码错误")
        else:
            message = form.get_error()
            return restful.params_error(message)


bp.add_url_rule('/resetpwd/', view_func=RestPWDView.as_view('resetpwd'), endpoint='resetpwd')


# 修改邮箱接口
class RestEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/rest_email.html')

    def post(self):
        form = RestEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


bp.add_url_rule('/resetemail/', view_func=RestEmailView.as_view('resetemail'), endpoint='resetemail')


# 获取邮箱验证码
@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.params_error('请输入邮箱地址')

    source = list(string.ascii_letters) #获取a-z和A-Z的列表
    source.extend([str(x) for x in range(10)])
    captcha = ''.join(random.sample(source, 6))

    # 发送邮件
    # message = Message(subject='您的验证码是：', recipients=[email], body=captcha)
    # try:
    #     mail.send(message)
    # except:
    #     return restful.server_error('服务器内部错误')

    try:
        send_mail(subject='您的验证码是：', recipients=[email], body=captcha)
    except:
        return restful.server_error('服务器内部错误')

    # 存储邮件对应的验证码
    cache.set(email, captcha)

    return restful.success()


# 测试发送邮件接口
@bp.route('/testemail/')
def testemail():
    message = Message(subject='测试发送', recipients=['jackie_5521@163.com'], body='测试')
    mail.send(message)
    return '测试邮件发送'


# 轮播图管理
@bp.route('/banner/')
@login_required
@permission_required(CMSPersmission.BANNER)
def banners():
    banners = BannerModel.query.order_by(BannerModel.prioirty.desc()).all()
    return render_template('cms/cms_scrollbanner.html', banners=banners)


# 添加轮播图
@bp.route('/addbanner/', methods=['POST'])
@login_required
def add_banner():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        img = form.img.data
        url = form.url.data
        prioirty = form.prioirty.data

        banner = BannerModel()
        banner.name = name
        banner.image = img
        banner.url = url
        banner.prioirty = prioirty

        db.session.add(banner)
        db.session.commit()

        return restful.success('添加成功！')
    else:
        return restful.params_error(message=form.get_error())


# 修改轮播图
@bp.route('/upbanner/', methods=['POST'])
@login_required
def upload_banner():
    form = UpdataBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        img = form.img.data
        url = form.url.data
        prioirty = form.prioirty.data
        banner = BannerModel.query.get(banner_id)
        if banner_id:
            banner.name = name
            banner.img = img
            banner.url = url
            banner.prioirty = prioirty
            db.session.commit()

            return restful.success('编辑成功！')
        else:
            return restful.params_error('没有此banner，修改失败！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/delbanner/', methods=['POST'])
@login_required
def def_banner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.params_error('没有这个轮播图id！')
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error('没有这个轮播图！')
    db.session.delete(banner)
    db.session.commit()
    return restful.success('删除成功！')


# 帖子管理
@bp.route('/posts/')
@login_required
@permission_required(CMSPersmission.POSTER)
def posts():
    star = request.args.get('star', type=int, default=0)
    puery_obj = None

    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    total = PostModel.query.count()
    pagination = Pagination(page=page, bs_version=3, total=total)

    if star == 1:
        puery_obj = db.session.query(PostModel).outerjoin(HeighLightPostModel).filter(PostModel.id==HeighLightPostModel.post_id).order_by(HeighLightPostModel.create_time.desc(), PostModel.create_time.desc()).slice(start, end)
    elif star == 2:
        # puery_obj = db.session.query(PostModel).outerjoin(HeighLightPostModel).filter(PostModel.id!=HeighLightPostModel.post_id).order_by(PostModel.create_time.desc()).slice(start, end)

        puery_obj = db.session.query(PostModel).filter(PostModel.heighlist == None).order_by(PostModel.create_time.desc()).slice(start, end)
    else:
        puery_obj = PostModel.query.order_by(PostModel.create_time.desc()).slice(start, end)

    return render_template('cms/cms_posts.html', posts=puery_obj, pagination=pagination)


# 帖子加精
@bp.route('/hpost/', methods=['POST'])
@permission_required(CMSPersmission.POSTER)
def heighlist_post():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('没有帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('没有找到对应帖子')
    heighlight = HeighLightPostModel(post=post)
    db.session.add(heighlight)
    db.session.commit()
    return restful.success('已成功加精！')


# 取消加精
@bp.route('/uhpost/', methods=['POST'])
@permission_required(CMSPersmission.POSTER)
def unheighlist_post():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('没有帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('没有找到对应帖子')
    heighl = HeighLightPostModel.query.filter_by(post_id=5).first()
    db.session.delete(heighl)
    db.session.commit()
    return restful.success('已取消加精！')


# 删除帖子
@bp.route('/dhpost/', methods=['POST'])
@permission_required(CMSPersmission.POSTER)
def delheighlist_post():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('没有帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('没有找到对应帖子')
    heighlist = post.heighlist
    if heighlist:
        db.session.delete(heighlist)
    db.session.delete(post)
    db.session.commit()
    return restful.success('帖子已删除！')


# 评论管理
@bp.route('/comments/')
@login_required
@permission_required(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


# 版块管理
@bp.route('/boards/')
@login_required
@permission_required(CMSPersmission.BOARDER)
def boards():
    boards = BoardModel.query.order_by(BoardModel.create_time.desc()).all()
    context = {
        'boards': boards
    }
    return render_template('cms/cms_boards.html', **context)


# 添加新版块
@bp.route('/addboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def addboard():
    form = AddBoardForm(request.form)
    if form.validate():
        name = form.name.data
        board = BoardModel()
        board.name = name
        db.session.add(board)
        db.session.commit()
        return restful.success('添加成功！')
    else:
        restful.params_error(form.get_error())


# 更新版块
@bp.route('/upboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def upboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        if not board_id:
            return restful.params_error(form.get_error())
        board = BoardModel.query.get(board_id)
        if not board:
            return restful.params_error('没有找到此版块！')
        board.name = name
        db.session.commit()
        return restful.success('编辑成功！')
    else:
        return restful.params_error(form.get_error())


# 删除版块
@bp.route('/delboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def delboard():
    board_id = request.form.get('board_id')
    if not board_id:
        return restful.params_error('没有找到对应id！')
    board = BoardModel.query.get(board_id)
    if not board:
        return restful.params_error('没有找到此版块！')
    db.session.delete(board)
    db.session.commit()
    return restful.success('删除成功！')


# 前台用户管理
@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


# 用户管理
@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


# 分组管理
@bp.route('/croles/')
@login_required
@permission_required(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')

