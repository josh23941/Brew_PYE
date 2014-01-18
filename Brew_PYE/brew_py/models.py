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
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    #Right now no reason to have 'inactive' users
    def is_active(self):
        return True
    
    @staticmethod
    def get(username):
        return User.query.filter_by(username=username).first()
    
    def get_id(self):
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
    
#create_all tables from the db.Model classes
db.create_all()
'''
#need to move this to appropriate place where registering a user would occur.
admin = User('admin', 'josh23941')
db.session.add(admin) #@UndefinedVariable
db.session.commit() #@UndefinedVariable
'''