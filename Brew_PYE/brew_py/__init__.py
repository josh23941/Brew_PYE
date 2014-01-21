from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'brew_py/uploads'
ALLOWED_EXTENSIONS = set(['xml'])

#initialize app with some coniguration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:josh23941@localhost:3306/brew_pye'
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'josh23941'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



#helper for upload_file()
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
#import routing infor for app...I think the documentation said 
#this is bad practice but necessary here ?? investigate this later


    
import controller, models
from models import db




