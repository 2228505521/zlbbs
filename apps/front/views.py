
from flask import (
    Blueprint,
    render_template,
    redirect,
    views,
    make_response,
    request,
    session,
    g,
    abort
)
from sqlalchemy.sql import func

from static.common.sms_alidayu import sms_alidayu
import json
from .forms import SignUpForm, LoginForm, PostForm, CommentForm
from utils import restful
from .models import FrontUser
from ..models import BannerModel, BoardModel, PostModel, CommentModel, HeighLightPostModel
from exts import db
from utils import safeutils
import config
from .decorators import login_required
from flask_paginate import Pagination, get_page_parameter

# celery异步发送短信
from tasks import send_captcha

bp = Blueprint('front', __name__, url_prefix='/front')

@bp.route('/index/')
def index():
    board_id = request.args.get('bd')
    banners = BannerModel.query.order_by(BannerModel.prioirty.desc()).limit(4)
    boards = BoardModel.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    sort = request.args.get('st', type=int, default=1)
    start = (page - 1)*10
    end = start + 10
    posts = None
    total = 0
    global query_obj
    if sort == 1:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 2:
        query_obj = db.session.query(PostModel).outerjoin(HeighLightPostModel).order_by(HeighLightPostModel.create_time.desc(), PostModel.create_time.desc())
    elif sort == 3:
        pass
    elif sort == 4:
        query_obj = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(func.count(CommentModel.id).desc(), PostModel.create_time.desc())

    if board_id:
        query_obj = PostModel.query.filter(PostModel.board_id==board_id)
        posts = query_obj.slice(start, end)
        total = query_obj.count()
    else:
        posts = query_obj.slice(start, end)
        total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total)
    context = {
        'banners': banners,
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
        'current': board_id,
        'current_sort': sort
    }
    return render_template('front/front_index.html', **context)

# 测试从哪个页面到注册页面，注册完成后再返回那个页面
# @bp.route('/test/')
# def test(message=None):
#     content = {
#         'message': message
#     }
#     return render_template('cms/cms_login.html', content=content)

# 注册接口
class SignupView(views.MethodView):

    def get(self):
        # 实现从注册页面返回上一个页面功能
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        return render_template('front/front_signup.html')

    def post(self):
        form = SignUpForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password1 = form.password1.data
            username = form.username.data

            user = FrontUser(telephone=telephone, password=password1, username=username)
            db.session.add(user)
            db.session.commit()

            return restful.success(message='注册成功')
        else:
            return restful.params_error(message=form.get_error())

bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'), endpoint='signup')

# 登录接口
class LoginView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and return_to != request.url:
            return render_template('front/front_login.html', return_to=return_to)
        return render_template('front/front_login.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password:
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success('登录成功')
            else:
                return restful.params_error('手机号码或者密码错误')
        else:
            return restful.params_error(form.get_error())

bp.add_url_rule('/login/', view_func=LoginView.as_view('login'), endpoint='login')


# 发布帖子
class PostView(views.MethodView):
    decorators = [login_required]

    def get(self):
        boards = BoardModel.query.all()
        context = {
            'boards': boards
        }
        return render_template('front/front_post.html', **context)

    def post(self):
        form = PostForm(request.form)
        if form.validate():
            board = BoardModel.query.get(form.board_id.data)
            if not board:
                return restful.params_error('没有找到这个版块')
            post = PostModel(title=form.title.data, content=form.content.data, board_id=form.board_id.data, author=g.front_user)
            db.session.add(post)
            db.session.commit()
            return restful.success('帖子发布成功！')
        else:
            return restful.params_error(form.get_error())

bp.add_url_rule('/post/', view_func=PostView.as_view('post'), endpoint='post')


# 帖子详情
@bp.route('/pd/<post_id>/')
def post_detail(post_id):
    post = PostModel.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return render_template('front/front_pdetail.html', post=post)


# 评论
@bp.route('/addcomment/', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        if not post:
            return restful.params_error('没有找到对应的帖子')
        comment = CommentModel(content=content, post_id=post_id, author_id=g.front_user.id)
        db.session.add(comment)
        db.session.commit()
        return restful.success('评论成功！')
    else:
        return restful.params_error(form.get_error())


@bp.route('/phoneCaptcha/')
def phone_captcha():
    # sms_alidayu.send_sms("18600764994", "程佳俊", "SMS_137550462", r"{code:1234}")
    resp = json.loads(send_captcha("18600764994", template_param=r"{code:1234}"))
    if resp['Code'] == 'OK':
        return ('发送成功')
    else:
        return ('发送失败')