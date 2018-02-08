#encoding:utf8
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from BBS import create_app
from exts import db
from apps.cms import  models as cms_models
app=create_app()
manage=Manager(app)
migrate=Migrate(app,db)
manage.add_command('db',MigrateCommand)
@manage.option('-u','--username',dest='username')
@manage.option('-p','--password',dest='password')
@manage.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user=cms_models.CMS_USER(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print ("cms user add success!")



if __name__ == '__main__':
    manage.run()