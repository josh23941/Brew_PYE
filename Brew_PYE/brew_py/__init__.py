from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

#Config stuff...should move to file
UPLOAD_FOLDER = 'brew_py/uploads'
ALLOWED_EXTENSIONS = set(['xml'])

#initialize app with some coniguration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:josh23941@localhost:3306/brew_pye'
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'josh23941'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Setup flask-login manager extension
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

#imports all routes to views
import controller

#Gets the SQLAlchemy object 'db' after models have been setup
#the db is not attached to the app yet so which allows for easy swapping in of the test db
from models.shared_models import db







