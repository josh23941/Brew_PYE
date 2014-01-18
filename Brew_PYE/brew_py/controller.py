'''
Created on Jan 15, 2014

@author: jmiller
'''

from flask import url_for, redirect, render_template, request, g, session
from brew_py import app, login_manager
from flask_login import login_required, login_user, current_user
from models import User



@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))  # @UndefinedVariable

'''''''''''''''''''''''''''''
APP ROUTES
''''''''''''''''''''''''''''' 

#Before all requests load global user as the current_user from Flask-Login
@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username = username).first()  # @UndefinedVariable
        if(user):
            real_password = user.password  
            if password == real_password:
                login_user(user)
                return redirect(request.args.get('next') or url_for('main'))
    return render_template('login.html')
    
@app.route('/main')
@login_required
def main():
    return render_template('main.html')