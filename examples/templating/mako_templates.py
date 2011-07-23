from mako.template import Template

print Template("""
<%namespace name="gcw" module="GChartWrapper"/>

${
    gcw.chart('Line',data)\
        .axes.type('xy')\
        .axes.label('Mar','Apr','May')\
        .axes.label(None,'50+Kb')\
        .color('red')\
        .line(6,5,2)\
        .img()
}

""").render(data='fohmnytenefohmnytene')

print Template("""
<%namespace name="gcw" module="GChartWrapper"/>

${
    gcw.chart()\
        .type('pie')\
        .dataset(data)\
        .size(250,100)\
        .img()
}

""").render(data='helloworld')
