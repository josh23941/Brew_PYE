'''
Created on Jan 18, 2014

@author: jmiller
'''

from flask_sqlalchemy import SQLAlchemy
from brew_py import app

#setup db
db = SQLAlchemy(app)

#User Model
class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username
    
    def isAuthenticated(self):
        return True
    
    #Right now no reason to have 'inactive' users
    def isActive(self):
        return True
    @staticmethod
    def get(username):
        return User.query.filter_by(username=username).first()
    
#create_all tables from the db.Model classes
db.create_all()

'''
#need to move this to appropriate place where registering a user would occur.
admin = User('admin', 'josh23941')
db.session.add(admin) #@UndefinedVariable
db.session.commit() #@UndefinedVariable
'''