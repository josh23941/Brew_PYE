'''
Created on Jan 15, 2014

@author: jmiller
'''

from flask import url_for, redirect, render_template, request
from brew_py import app
from flask_login import LoginManager, login_required, login_user
from models import User

'''''''''''''''''''''''''''''
FLASK-LOGIN STUFF
'''''''''''''''''''''''''''''
#flask login-manager extension initialization
login_manager = LoginManager()
login_manager.login_view = '/login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)  

'''''''''''''''''''''''''''''
APP ROUTES
'''''''''''''''''''''''''''''

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get(username)
        if(user):
            real_password = user.password  
            if password == real_password:
                #login_user(user)
                return redirect(url_for('main'))
    return render_template('login.html')
    
@app.route('/main')
def main():
    return render_template('main.html')