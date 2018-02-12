#encoding:utf-8
import config
from functools import wraps
from flask import session,render_template,redirect,url_for
def login_required(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return fun(*args,**kwargs)
        else:
            return  redirect(url_for('cms.login'))
    return wrapper

