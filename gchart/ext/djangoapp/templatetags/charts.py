"""
Django templatetags for chart and note types
Now takes an as argument
If the as argument is 'img', it will return a XHTML <img/>
If the as argument is 'url', it will simply return the url of the chart
If the as argument is anything else, the chart will be loaded into the context
and named what the as argument is

{% chart ... [as url|img|varname] %}
...
{% endchart %}

Example:

    {% chart Pie3D 1 2 3 4 5 as pie %}
        {% label A B C D %}
        {% color green %}
    {% endchart %}

    {% pie %} # The chart obj itself
    {% pie.image %} # The PIL instance
    {% pie.checksum %} # An SHA1 checksum

The FancyNode powers the tag for Note,Pin,Text and Bubble charts
The <type> argument is one of the chart types in lower case

    {% <type> ... [as url|img|varname]%}
    
    Example:
        {% bubble icon_text_big snack bb $2.99 ffbb00 black as img %}
    """

from django.template import Library,Node
from django.template import Variable, VariableDoesNotExist
import GChartWrapper

# version independent testing for numeric types
try:
    # python2.6 and later
    from numbers import Number as NumberType
    isNumberType = lambda x: isinstance(x, NumberType)
except ImportError, e:
    # deprecated function
    from operator import isNumberType

register = Library()

class GenericNode(Node):
    def __init__(self, args):
        # Warning: Take care not to modify self.args during rendering. Otherwise
        # subsequent renditions (e.g. in chart in a loop) will be incorrect.
        self.args = map(Variable, map(unicode,args))
    def render(self,context):
        # Holds the resolved arguments so that self.args remains unchanged.
        self.resolved_args = []
        for n,arg in enumerate(self.args):
            try:
                self.resolved_args.insert(n, arg.resolve(context))
                # If the resolution yields a numeric, use the unicode string instead.
                if isNumberType(self.resolved_args[n]): self.resolved_args[n] = arg.var
            except VariableDoesNotExist, e:
                # Unquoted string.
                self.resolved_args.insert(n, arg.var)
            except Exception, e:
                assert False, (repr(e), n)
        return self.post_render(context)
    def post_render(self, context): return self.resolved_args
    
def attribute(parser, token):
    return GenericNode(token.split_contents())

for tag in GChartWrapper.constants.TTAGSATTRS:
    register.tag(tag, attribute)

class ChartNode(Node):
    def __init__(self, tokens, nodelist):
        self.type = None
        self.tokens = []
        self.mode = None
        if tokens and len(tokens)>1:
            # chart type is resolved while rendering
            self.type = Variable(tokens[1])

            if tokens[-2] == 'as':
                self.mode = Variable(tokens[-1])
                self.tokens = map(Variable, tokens[2:-2])
            else:
                self.tokens = map(Variable, tokens[2:])
        self.nodelist = nodelist
    def render(self, context): 
        args = []
        kwargs = {}
        for t in self.tokens:
            try:
                args.append(t.resolve(context))
            except VariableDoesNotExist, e:
                # unquoted string token - convert to plain string
                # (arguments are expected to be plain strings, not unicode)
                arg = str(t.var)
                if arg.find('=')>-1:
                    k,v = arg.split('=')[:2]
                    kwargs[k] = v
                else:
                    args.append(arg)   
        if len(args) == 1 and type(args[0]) in map(type,[[],()]):
            args = args[0]

        try:
            self.resolved_type = self.type.resolve(context)
        except VariableDoesNotExist, e:
            # chart type provided as unquoted string.
            self.resolved_type = self.type.var

        if self.resolved_type in dir(GChartWrapper):
            chart = getattr(GChartWrapper,self.resolved_type)(args,**kwargs)
        elif self.resolved_type in GChartWrapper.constants.TYPES:
            chart = GChartWrapper.GChart(self.resolved_type,args,**kwargs)
        else:
            raise TypeError('Chart type %s not recognized'%self.resolved_type)

        for n in self.nodelist:
            rend = n.render(context)           
            if type(rend) == type([]):
                if rend[0] == 'img':
                    for k,v in map(lambda x: x.split('='), rend[1:]):
                        imgkwargs[k] = v
                    continue
                if rend[0] == 'axes':
                    getattr(getattr(chart, rend[0]), rend[1])(*rend[2:])
                else:
                    if isinstance(rend[1], list) or isinstance(rend[1], tuple):
                        getattr(chart, rend[0])(*rend[1])
                    else:
                        getattr(chart, rend[0])(*rend[1:])
        imgkwargs = {}
        if self.mode:
            self.resolved_mode = self.mode.resolve(context)
            if self.resolved_mode == 'img':  
                return chart.img(**imgkwargs)
            elif self.resolved_mode == 'url':  
                return str(chart)
            else:  
                context[self.resolved_mode] = chart
        else:
            return chart.img(**imgkwargs)

def make_chart(parser, token):
    nodelist = parser.parse(('endchart',))
    parser.delete_first_token()
    tokens = token.contents.split()
    return ChartNode(tokens,nodelist)
    
register.tag('chart', make_chart)

class FancyNode(GenericNode):
    cls = None
    def post_render(self,context):
        mode = None
        self.resolved_args = self.resolved_args[1:]
        if self.resolved_args[-2] == 'as':
            mode = self.resolved_args[-1]
            self.resolved_args = self.resolved_args[:-2]
        for n,arg in enumerate(self.resolved_args):
            self.resolved_args[n] = arg.replace('\\n','\n').replace('\\r','\r')
        G = self.cls(*self.resolved_args)
        if mode:
            if mode == 'img':  
                return G.img()
            if mode == 'url':  
                return str(G)
            else:  
                context[mode] = G
        else:
            return G.img()
        
class NoteNode(FancyNode):
    cls = GChartWrapper.Note
def note(parser, token):
    return NoteNode(token.split_contents())
register.tag(note)

class PinNode(FancyNode):
    cls = GChartWrapper.Pin
def pin(parser, token):
    return PinNode(token.split_contents())
register.tag(pin)

class TextNode(FancyNode):
    cls = GChartWrapper.Text
def text(parser, token):
    return TextNode(token.split_contents())
register.tag(text)

class BubbleNode(FancyNode):
    cls = GChartWrapper.Bubble
def bubble(parser, token):
    return BubbleNode(token.split_contents())
register.tag(bubble)
