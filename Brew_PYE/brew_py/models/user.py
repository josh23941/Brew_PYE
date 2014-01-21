'''
Created on Jan 20, 2014

@author: jmiller
'''
from sqlalchemy import Column, Integer, String
from shared_models import db

# User Model
class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    password = Column(String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    # Right now no reason to have 'inactive' users
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
    