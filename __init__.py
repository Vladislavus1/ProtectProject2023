from flask import Flask
from flask_login import LoginManager
import os

upload_folder = os.path.join('images')
results_folder = os.path.join('static/results.img')
app = Flask(__name__)
app.config["SECRET_KEY"] = "Hello_world!"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager_ukr = LoginManager()
login_manager_ukr.init_app(app)
login_manager.login_view = 'login_ukr'
from . import routes