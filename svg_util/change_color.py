from xml.etree.ElementTree import ElementTree as ET
from svg_util.etree import find, findall
from svg_util.css import css_dict, css_string, set_property, get_property
tree = ET()
tree.parse("./tests/addabove/A.svg")
root = tree.getroot()
rect = find(root,"g/rect")
set_property(rect,'fill',"#0000ff")
tree.write('bla2.svg')
