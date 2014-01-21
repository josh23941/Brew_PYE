'''
Created on Jan 18, 2014

@author: jmiller
'''

from sqlalchemy import Column, Integer, String, Float, Text
from collections import OrderedDict
from xml.etree import ElementTree as ET
from xml_util import get_element
from flask import g
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
    
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    owner = Column(String(80))
    name = Column(String(80))
    version = Column(Float)
    type = Column(String(9))
    brewer = Column(String(80))
    batch_size = Column(Float)
    boil_size = Column(Float)
    efficiency = Column(Float)
    hops = Column(Text)
    fermentatbles = Column(Text)
    style = Column(Text)
    equipment = Column(Text)
    mash = Column(Text)
    est_og = Column(Text)
    est_fg = Column(Text)
    est_color = Column(Text)
    ibu = Column(Text)
    est_abv = Column(Text)
    
    @staticmethod
    def get_by_owner(owner):
        return Recipe.query.filter_by(owner=owner)
    
    def __init__(self, owner, name, version, type, brewer, batch_size, boil_size, efficiency, hops, fermentables, style, equipment,
                 mash, est_og, est_fg, est_color, ibu, est_abv):
        self.owner = owner
        self.name = name
        self.version = version
        self.type = type
        self.brewer = brewer
        self.batch_size = batch_size
        self.boil_size = boil_size
        self.efficiency = efficiency
        self.hops = hops
        self.fermentables = fermentables
        self.style = style
        self.equipment = equipment
        self.mash = mash
        self.est_og = est_og
        self.est_fg = est_fg
        self.est_color = est_color
        self.ibu = ibu
        self.est_abv = est_abv
        
        
    def get_id(self):
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
    
    @staticmethod
    def process_recipe(filepath):
        dictionary = OrderedDict([('RECIPE/NAME', True),
                    ('RECIPE/VERSION', True),
                    ('RECIPE/TYPE', True),
                    ('RECIPE/BREWER', True),
                    ('RECIPE/BATCH_SIZE', True),
                    ('RECIPE/BOIL_SIZE', True),
                    ('RECIPE/EFFICIENCY', True),
                    ('RECIPE/HOPS', False),
                    ('RECIPE/FERMENTABLES', False),
                    ('RECIPE/STYLE', False),
                    ('RECIPE/EQUIPMENT', False),
                    ('RECIPE/MASH', False),
                    ('RECIPE/EST_OG', True),
                    ('RECIPE/EST_FG', True),
                    ('RECIPE/EST_COLOR', True),
                    ('RECIPE/IBU', True),
                    ('RECIPE/EST_ABV', True),
                    ])
        element_tree = ET.parse(filepath)
        #session owner will be set to owner of recipe in database>
        params = [g.user.username]
        for k, v in dictionary.iteritems():
            params.append(get_element(element_tree, k, v))
        return params



def save_model_to_db(model_object):
    db.session.add(model_object)  # @UndefinedVariable
    db.session.commit() #@UndefinedVariable
    return True
'''
#need to move this to appropriate place where registering a user would occur.
admin = User('admin', 'josh23941')
db.session.add(admin) #@UndefinedVariable
db.session.commit() #@UndefinedVariable
'''
