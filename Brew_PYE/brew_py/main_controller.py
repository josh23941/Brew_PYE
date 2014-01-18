'''
Created on Jan 15, 2014

@author: jmiller
'''

from flask import url_for, redirect, render_template, request, session
from brew_py import app, User

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        real_password = User.query.filter_by(username=user).first().password  # @UndefinedVariable
        if password == real_password:
            session['logged_in'] = True
            return redirect(url_for('main'))
        else:
            session['logged_in'] = False
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/main')
def main():
    return render_template('main.html')