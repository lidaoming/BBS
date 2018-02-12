#coding:utf-8
from flask import Blueprint,render_template,views,request,session,redirect,url_for,g
from .forms import LoginForm
from exts import db
from .models import CMS_USER
from .decorators import login_required
import config
bp=Blueprint('cms',__name__,url_prefix='/cms')

#cms首页视图函数
@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')



#cms管理系统登陆视图函数
class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/login.html',message=message)
    def post(self):
        form=LoginForm(request.form)
        if form.validate():
            #登陆验证通过
            email=form.email.data
            password=form.password.data
            user=db.session.query(CMS_USER).filter(email==email).first()
            if user:
                if user.check_password(password):
                    #验证成功
                    session[config.CMS_USER_ID]=user.id
                    return redirect(url_for('cms.index'))
                else:
                    #return "用户名或者密码错误"
                    return self.get(message=u'用户名或者密码错误')
            else:
                return self.get(message=u'去注册吧~~')
        else:
            #return "输入的数据有问题呢。。"
            return self.get(message=u'输入的数据有问题呢。。')
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))


#CMS管理系统个人信息视图函数
@bp.route('/profile')
@login_required
def profile():
    return render_template('cms/profile.html')

#CMS管理系统注销视图函数
@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('cms.login'))




