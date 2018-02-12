#encoding:utf8
import os

SECRET_KEY=os.urandom(24)
DEBUG=True
host='127.0.0.1'
port='3306'
database='BBS'
username='root'
password='toor'
SQLALCHEMY_TRACK_MODIFICATIONS=False
DB_URI='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(username,password,host,port,database)
SQLALCHEMY_DATABASE_URI=DB_URI
CMS_USER_ID='cms_user_id'