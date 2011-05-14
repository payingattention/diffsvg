from xml.etree.ElementTree import ElementTree as ET
from svg_util.etree import find, findall
from svg_util.css import css_dict, css_string, set_property, get_property
from copy import deepcopy
tree = ET()
tree.parse("./tests/addabove/A.svg")
root = tree.getroot()
g = find(root,"g")
rect = find(root,"g/rect")
rect2 = deepcopy(rect)
rect2.attrib['id'] = rect.attrib['id']+"2"
rect2.attrib['x'] = str(float(rect.attrib['x']) + float(rect.attrib['width']))
g.append(rect2)
tree.write('bla3.svg')
