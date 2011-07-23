"""
An example of how to use the GChartWrapper with the Cheetah templating language
"""
try:
    from Cheetah.Template import Template
except ImportError:
    raise ImportError, 'You must have cheetah templates installed'
    
print Template("""
    #from GChartWrapper import Line
    #set G = $Line($data)
    $G.color('ff0000')
    $G.line(6,5,2)
    $G.img()
""",  searchList=[{'data':['hX1xPj']}])  
