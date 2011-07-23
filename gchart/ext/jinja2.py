from jinja2 import nodes
from jinja2.ext import Extension


class ChartExtension(Extension):
    tags = set(['chart'])
    
    def parse(self, parser):
        lineno = parser.stream.next().lineno

        args = [parser.parse_expression()]

        args.append(parser.parse_expression())
        #else:
        #    args.append(nodes.Const(None))

        body = parser.parse_statements(['name:endchart'], drop_needle=True)

        return nodes.CallBlock(self.call_method('_chart_support', args),
                               [], [], body).set_lineno(lineno)

    def _chart_support(self, *args):
        """Helper callback."""
        print( args)
