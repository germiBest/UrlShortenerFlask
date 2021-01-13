import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
#from config import Config
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


csrf = CSRFProtect()

app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
csrf.init_app(app)
db = SQLAlchemy(app)

from app import routes, models
