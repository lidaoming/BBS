from .views import bp
import config
from flask import session,g
from .models import CMS_USER
from exts import db





@bp.before_request
def before_request():
    #print 123
    if config.CMS_USER_ID in session:
        user_id=session.get(config.CMS_USER_ID)
        user=db.session.query(CMS_USER).get(user_id)
        if user:
            g.cms_user=user