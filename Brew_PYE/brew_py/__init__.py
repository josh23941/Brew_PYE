from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#initialize app with some coniguration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:josh23941@localhost:3306/testertest1'
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'josh23941'

#setup db
db = SQLAlchemy(app)

#User Model
class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username
    
import main_controller

'''
#login manager ?need to reed docs on this is session management ??
login_manager = LoginManager()
login_manager.init_app(app)
'''


'''
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
'''
    
