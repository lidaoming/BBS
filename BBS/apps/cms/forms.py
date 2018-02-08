#encoding:utf-8
from wtforms import Form,StringField
from wtforms.validators import Email,InputRequired,Length
class LoginForm(Form):
    email=StringField(validators=[Email(message="请输入正确邮箱格式"),InputRequired(message="请输入邮箱")])
    password=StringField(validators=[Length(4,20,message='密码太短或太长')])

