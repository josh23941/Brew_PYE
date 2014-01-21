'''
Created on Jan 16, 2014

@author: jmiller
'''
from brew_py import app, db
with app.app_context():
    db.init_app(app)
    db.create_all()
app.run(debug=False)
