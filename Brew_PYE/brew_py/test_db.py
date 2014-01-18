'''
Created on Jan 15, 2014

@author: jmiller
'''
from brew_py import db, User

db.create_all()

admin = User('admin12w', 'admin@example.com')
guest = User('guest123', 'guest@example.com')
db.session.add(admin) #@UndefinedVariable
db.session.add(guest) #@UndefinedVariable
db.session.commit() #@UndefinedVariable
