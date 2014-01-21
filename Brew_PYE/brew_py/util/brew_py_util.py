'''
Created on Jan 19, 2014

@author: jmiller
'''

from xml.etree import ElementTree as ET
from brew_py import ALLOWED_EXTENSIONS

def get_element(element_tree, xpath, return_text):
    for elem in element_tree.iterfind(xpath):
        if return_text:
            return elem.text
        else:
            return ET.tostring(elem)
        
#helper for upload_file()
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS