from gchart.charts import *

__all__ = ['Sparkline', 'Map', 'HorizontalBarStack', 'VerticalBarStack', 'QRCode',
'Line', 'BaseChart', 'HorizontalBarGroup', 'Scatter', 'Pie3D', 'Pie', 'Meter',
'Radar', 'RadarSpline', 'VerticalBarGroup', 'LineXY', 'Venn', 'PieC','Pin',
'Text','Note','Bubble','charts','settings','encoding','tests']
__version__ = '1.0'
__author__ = 'Justin Quick <justquick@gmail.com>'

def chart(context, chart=None, *args, **kwargs):
    from gchart import charts
    if chart and chart in dir(charts):
        return getattr(charts, chart)(*args, **kwargs)
    return BaseChart(*args, **kwargs)