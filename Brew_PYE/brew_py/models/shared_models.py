'''
Created on Jan 20, 2014

@author: jmiller
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def save_model_to_db(model_object):
    db.session.add(model_object)  # @UndefinedVariable
    db.session.commit() #@UndefinedVariable
    return True