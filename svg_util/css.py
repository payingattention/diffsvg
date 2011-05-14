def css_dict(styles_str):
    return dict([tuple(style.split(':')) for style in styles_str.split(';')])
    
def css_string(styles_dic):
    return ";".join([key+":"+val for key, val in styles_dic.iteritems()])
    
def get_property(elem,name):
    return css_dict(elem.attrib['style'])[name]
    
def set_property(elem,name,val):
    styles_dic = css_dict(elem.attrib['style'])
    styles_dic[name] = val
    elem.attrib['style'] = css_string(styles_dic)
