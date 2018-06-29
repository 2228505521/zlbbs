
from flask import session, redirect, url_for, g

from functools import wraps

import config

def login_required(func):

    @wraps(func)
    def inner(*args, **kwargs):
        user_id = session.get(config.FRONT_USER_ID)
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.login'))
    return inner