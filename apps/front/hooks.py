
from .views import bp
import config
from flask import session, g, render_template
from .models import FrontUser


@bp.before_request
def my_before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user
    else:
        g.front_user = None


@bp.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('front/404.html'), 404