import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


# f: Callable would be the flask end point function something like >> def index():
# (*args, **kwargs) is req because we do not kno if the callable has args like >> def index(args...):
def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('You need to be signed in for this page.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('Admin access required for this page.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function

