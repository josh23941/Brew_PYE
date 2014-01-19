'''
Created on Jan 15, 2014

@author: jmiller
'''

from flask import url_for, redirect, render_template, request, g, session
from brew_py import app, login_manager, allowed_file
from flask_login import login_required, login_user, current_user, logout_user
from models import User, Recipe
import os
from werkzeug import secure_filename
from xml.etree import ElementTree as ET
from xml_util import process_recipe


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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/main')
@login_required
def main():
    return render_template('main.html')

@app.route('/recipes/view')
@login_required
def recipes_view():
    return render_template('view_recipes.html')

'''''
Uploads a file to UPLOAD_FOLDER
'''''
@app.route('/recipes/upload', methods=['POST'])
@login_required
def upload_file():
    uploaded_file = request.files['inputFile']
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(temp_path)
        recipe_xml = ET.parse(temp_path)
        args = process_recipe(recipe_xml, Recipe.get_recipe_dict())
        recipe = Recipe(*args)
        Recipe.save(recipe)
        #sometime add verification that this is recipe_xml??? or even beer recipe_xml
        #pull the data you want and save to db
        return redirect(url_for('main'))

