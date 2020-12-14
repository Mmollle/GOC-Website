import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

TEMPLATE_DIR = os.path.join(".", "templates")
STATIC_DIR = os.path.join(".", "static")

app = Flask(__name__, template_folder = TEMPLATE_DIR, static_folder = STATIC_DIR)
app.config['SECRET_KEY'] = 'd035d622dc82b6465e417465da37a499'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
db = SQLAlchemy()

from goc import routes