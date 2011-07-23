from jinja2 import Environment, Template
#from GChartWrapper.jinja2 import ChartExtension


from jinja2 import nodes
from jinja2.ext import Extension


class ChartExtension(Extension):
    tags = set(['chart'])
    
    def parse(self, parser):
        args = []
        while 0:
            token = parser.stream.next()
            print token
            if str(token) == 'eof': break
            args.append(token)

        args.append(parser.parse_expression())
        args.append(parser.parse_expression())
        #else:
        #args.append(nodes.Const(None))
        print args
        body = parser.parse_statements(['name:endchart'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_chart_support', args),
                               [], [], body)

    def _chart_support(self, *args, **kwargs):
        """Helper callback."""
        print args,kwargs
        return ''

template = Template("""
{% chart  Line  %}
    size 200 100  
    axes type xy  
     axes label April May June  
     axes label None  50+Kb  
{% endchart %}

""", extensions=[ChartExtension])


template.render(data='fohmnytenefohmnytene')