'''
Created on Jan 20, 2014

@author: jmiller
'''

from brew_py import app, db
import unittest

'''
SKELETON FOR TESTING APP
'''
class BrewPyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:josh23941@localhost:3306/brew_pye_test'
        app.config['TESTING'] = True
        
        self.app = app.test_client()
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
    
    def test_blah(self):
        print 'blah'
        
if __name__ == '__main__':
    unittest.main()
