from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

csrf = CSRFProtect()
app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
csrf.init_app(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import routes, models
