'''
Created on Jan 19, 2014

@author: jmiller
'''

from xml.etree import ElementTree as ET

def get_element(element_tree, xpath, return_text):
    for elem in element_tree.iterfind(xpath):
        if return_text:
            return elem.text
        else:
            return ET.tostring(elem)