from flask import Flask

#initialize app with some coniguration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:josh23941@localhost:3306/brew_pye'
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'josh23941'

#import routing infor for app...I think the documentation said 
#this is bad practice but necessary here ?? investigate this later
import main_controller

    
