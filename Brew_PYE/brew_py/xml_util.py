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
        
def process_recipe(element_tree, dictionary):
    params = []
    for k,v in dictionary.iteritems():
        params.append(get_element(element_tree, k, v))
    print params
    return params
'''
dictionary = OrderedDict([('RECIPE/NAME', True),  # @IndentOk
                    ('RECIPE/VERSION', True),
                    ('RECIPE/TYPE', True),
                    ('RECIPE/BREWER', True),
                    ('RECIPE/BATCH_SIZE', True),
                    ('RECIPE/BOIL_SIZE', True),
                    ('RECIPE/EFFICIENCY', True),
                    ])
'''