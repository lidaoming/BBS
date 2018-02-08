#coding:utf-8
from flask import Blueprint,render_template,views,request,session,redirect,url_for
from .forms import LoginForm
from exts import db
from .models import CMS_USER
bp=Blueprint('cms',__name__,url_prefix='/cms')
@bp.route('/')
def index():
    return "管理界面"

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
                    session['user_id']=user.id
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