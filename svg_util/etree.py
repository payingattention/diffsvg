SVG_NS = "{http://www.w3.org/2000/svg}"

def add_ns(query):
    return SVG_NS + query.replace('/','/'+SVG_NS)
    
def find(e,query):
    return e.find(add_ns(query))
    
def findall(e,query):
    return e.findall(add_ns(query))
