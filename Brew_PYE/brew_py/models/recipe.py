'''
Created on Jan 20, 2014

@author: jmiller
'''

from shared_models import db
from sqlalchemy import Column, Integer, String, Float, Text
from flask import g
from xml.etree import ElementTree as ET

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
    
    @staticmethod
    def get_inner_xml(element_tree, xpath):
        for elem in element_tree.iterfind(xpath):
            return ET.tostring(elem)
        
    #takes filepath of uploaded Beersmith2 recipe xml.
    #TODO: there are more fields to extract from xml if wanted
    def __init__(self, filepath):
        
        etree = ET.parse(filepath)
        
        self.owner = g.user.username
        self.name = etree.iterfind('RECIPE/NAME').next().text
        self.version = etree.iterfind('RECIPE/VERSION').next().text
        self.type = etree.iterfind('RECIPE/TYPE').next().text
        self.brewer = etree.iterfind('RECIPE/BREWER').next().text
        self.batch_size = etree.iterfind('RECIPE/BATCH_SIZE').next().text
        self.boil_size = etree.iterfind('RECIPE/BOIL_SIZE').next().text
        self.efficiency = etree.iterfind('RECIPE/EFFICIENCY').next().text
        self.hops = Recipe.get_inner_xml(etree, 'RECIPE/HOPS')
        self.fermentables = Recipe.get_inner_xml(etree, 'RECIPE/FERMENTABLES')
        self.style = Recipe.get_inner_xml(etree, 'RECIPE/STYLE')
        self.equipment = Recipe.get_inner_xml(etree, 'RECIPE/EQUIPMENT')
        self.mash = Recipe.get_inner_xml(etree, 'RECIPE/MASH')
        self.est_og = etree.iterfind('RECIPE/EST_OG').next().text
        self.est_fg = etree.iterfind('RECIPE/EST_FG').next().text
        self.est_color = etree.iterfind('RECIPE/EST_COLOR').next().text
        self.ibu = etree.iterfind('RECIPE/IBU').next().text
        self.est_abv = etree.iterfind('RECIPE/EST_ABV').next().text
        
        
    def get_id(self):
        try:        
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
    