#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extensive unit tests, more are welcome

All methods should be commented and must return a Chart instance as the last line.
Dont forget to add the checksum to CHART_CHECKSUMS
"""
from functools import wraps

from gchart.charts import *
from gchart.encoding import Encoder
from gchart.settings import PY_VER,_print


def check_sum(known_sum):
    def inner(func):
        @wraps(func)
        def sub():
            chart = func()
            chart_name = func.__name__.split('test_')[1]
            test_sum = chart.checksum()
            assert known_sum == test_sum, \
                    '%s: %s != %s' % (chart_name, test_sum, known_sum)
        return sub
    return inner

@check_sum('36f99c6a7e93af8d164af220ae626c10002f808e')
def test_scatter():
    chart = Scatter([[12,87,75,41,23,96,68,71,34,9],[98,60,27,34,56,79,58,74,18,76],[84,23,69,81,47,94,60,93,64,54]])
    chart.axes('xy')
    chart.axes.label(0, 0,20,30,40,50,60,70,80,90,10)
    chart.axes.label(1, 0,25,50,75,100)
    chart.size(300,200)
    return chart


@check_sum('049d0fe4a213204e8e31f07658c7a665ea866698')
def test_fancy_radar():
    chart = RadarSpline(['voJATd9v','MW9BA9'],encoding='simple')
    chart.color('red','orange')
    chart.size(400,400)
    chart.line(2,4,0)
    chart.line(2,4,0)
    chart.axes('x')
    chart.axes.label(0, 0,45,90,135,180,225,270,315)
    chart.axes.range(0, 0.0,360.0)
    chart.grid(25.0,25.0,4.0,4.0)
    chart.marker('B','FF000080',0,1.0,5.0)
    chart.marker('B','FF990080',1,1.0,5.0)
    chart.marker('h','blue',0,1.0,4.0)
    chart.marker('h','3366CC80',0,0.5,5.0)
    chart.marker('V','00FF0080',0,1.0,5.0)
    chart.marker('V','008000',0,5.5,5.0)
    chart.marker('v','00A000',0,6.5,4)
    return chart

@check_sum('bc72f51d748767fc1692b6a227d5184415e9e2f5')
def test_omitted_colors():
    chart = Line([[20,10,15,25,17,30],[0,5,10,7,12,6],[35,25,45,47,24,46],
        [15,40,30,27,39,54],[70,55,63,59,80,60]],encoding='text',series=1)
    chart.scale(0,100,-50,100)
    chart.marker('F','',1,'1:4',20)
    return chart        

@check_sum('94219f27b54883078db0ef744292a40e46de2da7')
def test_bar_zero():
    chart = VerticalBarGroup([20,35,50,10,95],encoding='text')
    chart.color('cc0000')
    chart.position(.5)
    return chart

@check_sum('5e60f45fb27f32aefe048d9eb22f17a7d117c162')
def test_interval():
    chart = Line('cEAELFJHUc',encoding='simple')
    chart.color('76A4FB')
    chart.line(2)
    chart.axes('x')
    chart.axes.range(0,10,50,5)
    return chart

@check_sum('2cd25d4a258abb9d62d144668e3cb54f71b01af1')
def test_pacman():
    chart = Pie([80,20])
    chart.orientation(0.628)
    chart.color('yellow','white')
    return chart

@check_sum('1fb72aac2758d164bca43a40472ae185091291b1')
def test_simple():
    # Instantiate the BaseChart instance, this is all you will need for making charts
    # BaseChart(type=None, dataset=None), see the doc for more
    chart = BaseChart()
    # Set the chart type, either Google API type or regular name
    chart.type('pie')
    # Update the chart's dataset, can be two dimensional or contain string data
    chart.dataset( 'helloworld' )
    # Set the size of the chart, default is 300x150
    chart.size(250,100)
    return chart

@check_sum('6f33c38098da3aa433efce60e89ec825e6df13d4')
def test_hvz():
    # Make a vertical bar group and scale it to the max
    chart = VerticalBarGroup( [[31],[59],[4]], encoding='text' )
    chart.scale(0,59)
    chart.color('lime','red','blue')
    chart.legend('Goucher(31)','Truman(59)','Kansas(4)')
    chart.fill('c','lg',45,'cccccc',0,'black',1)
    chart.fill('bg','s','cccccc')        
    chart.size(200,100)
    return chart

@check_sum('00aa575be9406cfc7930ceb95e0438cd85ae2cae')
def test_qr_code():
    # Output a QR code graph that allows 15% restore with 0 margin
    # *Defaults to UTF-8 encoding 
    chart = QRCode('To the human eye QR Codes look like hieroglyphics, but they can be read by any device that has the appropriate software installed.')
    chart.size(300, 300)
    # or use output_encoding method
    chart.output_encoding('UTF-8')
    # level_data(error_correction,margin_size)
    chart.level_data('M',0)
    return chart

@check_sum('40d64c1c3aeb9c3836e501033c4bf65da2ff2f83')
def test_title():
    # Title using name with optional color and size
    chart = Line( ['GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl'] )
    chart.title('The Zen of Python','00cc00',36)
    chart.color('00cc00')
    return chart
    
@check_sum('9b6f9a566b49fa23c91a6f992e4a4737caac4ae5')
def test_line():
    # Add red line 6 thick
    # with 5 line segments with 2 blank segments
    chart = Line( ['hX1xPj'] )
    chart.axes('xy')
    chart.axes.label(0, 'Mar', 'Apr', 'May', 'June', 'July')
    chart.axes.label(1, None, '50 Kb')        
    chart.color('red')
    chart.line(6,5,2)
    return chart

@check_sum('d3251fb77a28a5918955020c745fa435b0f4a314')
def test_bar():
    # 2 color horizontal bars 10 wide
    # with 5 spacing between bars in group and 10 between groups
    chart = HorizontalBarGroup( ['hell','orld'] )
    chart.color('cc0000', '00aa00') 
    chart.bar(10,5,10)   
    return chart

@check_sum('3fe7636938cda678be044848799a2c87ecad6099')
def test_pie():
    # Simple pie chart based on list
    chart = Pie3D( [1,2,3,4] )
    chart.label('A','B','C','D')
    chart.color('00dd00')
    return chart

@check_sum('cf327d123a3a2fdf04620a966903fc20f096f82c')
def test_venn():
    # Extended venn diagram based on int list, scale the data to the max value
    chart = Venn( [100,80,60,30,30,30,10], encoding='text')
    chart.scale(0,100)
    return chart

@check_sum('6040f894d8e71160b9e87541f7ef9db224efae9c')
def test_axes():
    # Call type first with the chxt
    # then call label and style in order, 
    # label can contain None(s)
    chart = Line( ['foobarbaz'] )
    chart.color('76A4FB') 
    chart.axes('xyrx')
    chart.axes.label(0,'Foo', 'Bar', 'Baz')
    chart.axes.style(0, '0000dd', 14)
    chart.axes.label(1, None, '20K', '60K', '100K')  
    chart.axes.label(2, 'A', 'B', 'C')  
    chart.axes.label(3, None,'20','40','60','80')      
    return chart

@check_sum('90953636424f46e568bf8a316efbba4df0461eef')
def test_grid():
    # Create dashed line with grid x,y as floats
    # then, just like line, the line and blank segments
    chart = Line( ['foobarbaz'] )
    chart.color('76A4FB')   
    chart.line(3,6,3)
    chart.grid(20.0,25.0,1,0)
    return chart

@check_sum('fc7ab02d17a07a611a02b0a4dda7763c4bfec712')
def test_markers():
    # Mark up some of the data randomly
    chart = Line( ['helloWorldZZZZ098236561'] )
    chart.marker('c','red',0,1,20)
    chart.marker('d','80C65A',0,6,15)    
    chart.marker('o','FF9900',0,4.0,20.0)
    chart.marker('s','3399CC',0,5.0,10.0)
    chart.marker('v','BBCCED',0,6.0,1.0)
    chart.marker('V','3399CC',0,7.0,1.0)
    chart.marker('x','FFCC33',0,8.0,20.0)
    chart.marker('h','black',0,0.30,0.5 )       
    chart.marker('a','000099',0,4,10)
    chart.marker('R','A0BAE9',0,8,0.6)    
    chart.marker('r','E5ECF9',0,1,0.25)
    return chart
    
@check_sum('6d0d251ac640c0d5185124cb5ea9ccc636268f14')
def test_jacobian():     
    # from http://toys.jacobian.org/hg/googlecharts/raw-file/tip/docs/examples.html  
    chart = Line(['ALAtBmC1EcGYIsLWOXRuVdZhd9ivn4tYzO5b..'],encoding='extended')
    chart.size(300,200)
    chart.color('cc0000')
    chart.fill('c','s','eeeeee')
    chart.legend('Sweet')
    return chart

@check_sum('95664c2d4aeae5bcb94b1b003b361e2035d44e64')
def test_markerfill():
    # Fill the chart areas with markers
    chart = Line( ['99','cefhjkqwrlgYcfgc',
        'QSSVXXdkfZUMRTUQ','HJJMOOUbVPKDHKLH','AA'] )
    chart.marker('b','76A4FB',0,1,0)
    chart.marker('b','224499',1,2,0)
    chart.marker('b','red',2,3,0)
    chart.marker('B','80C65A',3,4,0)
    return chart

@check_sum('1766f4b8b774d41985a4a3b2ab3f9791dedab2a3')
def test_fill():
    # Fill the chart/background using chf, add axes to show bg 
    chart = Line( ['pqokeYONOMEBAKPOQVTXZdecaZcglprqxuux393ztpoonkeggjp'] )
    chart.color('red')
    chart.line(4,3,0)
    chart.axes('xy') 
    chart.axes.label(0, 1,2,3,4,5)
    chart.axes.label(1, None,50,100)
    chart.fill('c','lg',45,'white',0,'76A4FB',0.75)
    chart.fill('bg','s','EFEFEF')
    return chart

@check_sum('33cd2c7acdc4aa9745ed95a0aa1ff641525adf5c')
def test_legend():
    # Add legend to the data set which follows collors
    chart = Line( ['FOETHECat','leafgreen','IRON4YOUs'] )  
    chart.color('red','lime','blue')
    chart.legend('Animals','Vegetables','Minerals')
    chart.axes('y') 
    return chart

@check_sum('acc8c1a1199e2363fee076486365b6f8a29e72a0')
def test_legend2():
    # Add a left aligned legend to the chart
    chart = Line( ['abcde','FGHIJ','09876'] )  
    chart.color('red','lime','blue')
    chart.legend('Animals','Vegetables','Minerals')
    chart.legend_pos('l')
    chart.axes('y') 
    return chart

@check_sum('5f2d550e98ae1a85312b4d7e33761d30ca89acfd')
def test_legend_position():
    # Place the legend in the top position
    chart = Venn([100,20,20,20,20,0,0])
    chart.legend('First','Second','Third')
    chart.legend_pos('t')
    chart.color('red','lime','blue')
    return chart

@check_sum('5f27957e39363ca470c0e97d1fcffdc19fa00afb')
def test_multiline():
    # Draw multiple lines with markers on an lxy chart
    chart = LineXY( [ 
        [0,30,60,70,90,95,100], # x values
        [20,30,40,50,60,70,80], # y values, etc.
        [10,30,40,45,52],
        [100,90,40,20,10],
        ['-1'], # domain not found, interpolated
        [5,33,50,55,7],
    ])
    chart.scale(0,100)
    chart.color('3072F3','red','00aaaa')
    chart.marker('s','red',0,-1,5)
    chart.marker('s','blue',1,-1,5)
    chart.marker('s','00aa00',2,-1,5)   
    chart.line(2,4,1)   
    return chart

@check_sum('7d6d5d0fa5565ef3e1069ba91db472484a339696')
def test_axes_position():
    # multiple axis with label positions specified
    # values between 0 and 100 - use text encoding
    data = [[4.6, 6.0, 7.4, 11.6, 12.0, 14.8, 18.1, 25.1, 
             27.9, 28.3, 30.6, 34.4, 43.7, 48.3, 57.6, 64.6, 
             72.5, 74.4, 76.2, 77.2, 86.0, 86.9, 93.9, 96.7, 99.0], 
            [80.5, 100.0, 95.4, 93.7, 96.3, 91.7, 71.5, 63.0, 
             65.2, 65.5, 66.0, 75.9, 65.8, 64.4, 64.2, 62.5, 37.2, 
             35.3, 32.4, 35.2, 38.4, 37.9, 69.8, 38.0, 64.5]]
    
    # positions between 0 and 100
    axis = [ [0, 13, 28, 42, 56, 71, 84, 100],
             ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] ]
    
    # don't do integer arithmetic
    min_value = float(min(data[1]))
    max_value = float(max(data[1]))
    last_value = float(data[1][-1])
    
    chart = LineXY(data, encoding='text')
    chart.color('76A4FB')
    chart.marker('o', '0077CC',0,-1,5)
    chart.marker('r', 'E6F2FA',0,(min_value/max_value),1.0) # 0 to 1.0
    chart.axes("xyr")    
    chart.axes.label(0, *axis[1])
    chart.axes.position(0, *axis[0])
    chart.axes.label(1, '%d'%min_value, '%d'%max_value)    
    chart.axes.position(1, int(100*min_value/max_value),100) # 0 to 100
    chart.axes.label(2, '%d'%last_value)
    chart.axes.position(2, int(100*last_value/max_value)) # 0 to 100
    return chart

@check_sum('0b3b189c0675fd51bda46714706e3f7dfb4164dc')
def test_guide_intro():
    chart = Pie3D([60,40], encoding='text')
    chart.size(250,100)
    chart.label('Hello', 'World')
    return chart

@check_sum('1dfcb2ba4444e3c09be3b55221cc04e5a5c0bf32')
def test_guide_granularity_20():
    chart = Line('fohmnytenefohmnytene', encoding='simple')
    chart.size(200,100)
    chart.axes('xy')
    chart.axes.label(0, 'April','May','June')
    chart.axes.label(1, None, '50 Kb')
    return chart

@check_sum('dc7d8714f28d7a59d2b768ecba7f685814a73bd4')
def test_guide_granularity_40():
    chart = Line('frothsmzndyoteepngenfrothsmzndyoteepngen', encoding='simple')
    chart.size(200,100)
    chart.axes('xy')
    chart.axes.label(0, 'April','May','June')
    chart.axes.label(1, None, '50 Kb')
    return chart

@check_sum('014f1a251dab5fa14fdadf7868b64a210bb1cf5e')
def test_guide_granularity_80():
    chart = Line('formostthisamazingdayfortheleapinggreenlformostthisamazingdayfortheleapinggreenl',
        encoding='simple')
    chart.size(200,100)
    chart.axes('xy')
    chart.axes.label(0, 'April','May','June')
    chart.axes.label(1, None, '50 Kb')
    return chart

@check_sum('35281ef165d532021290c003e2068527d40003b0')
def test_guide_granularity_150():
    chart = Line('ithankYouGodformostthisamazingdayfortheleapinggreenlyspiritsoftreesandabluetruedreamofskyandforeverythingwhichisnaturalwhichisinfinitewhichisyeseecumm',
        encoding='simple')
    chart.size(200,100)
    chart.axes('xy')
    chart.axes.label(0, 'April','May','June')
    chart.axes.label(1, None, '50 Kb')
    return chart

@check_sum('0d5a40563ad832312bd357564a9da9787e38d6ef')
def test_guide_granularity_300():
    chart = Line('ithankYouGodformostthisamazingdayfortheleapinggreenlyspiritsoftreesandabluetruedreamofskyandforeverythingwhichisnaturalwhichisinfinitewhichisyesithankYouGodformostthisamazingdayfortheleapinggreenlyspiritsoftreesandabluetruedreamofskyandforeverythingwhichisnaturalwhichisinfinitewhichisyeseecummings',
        encoding='simple')
    chart.size(200,100)
    chart.axes('xy')
    chart.axes.label(0, 'April','May','June')
    chart.axes.label(1, None, '50 Kb')
    return chart

@check_sum('11ec3b84d8de22e8bf6a32cbca3b62374aa68a46')
def test_guide_line_lc():
    # http://code.google.com/apis/chart/#line_charts
    chart = Line('fooZaroo', encoding='simple')
    chart.size(200,100)
    return chart

@check_sum('767bab6609f60b6c7185b0ed0a1434ad9d73f4c7')
def test_guide_sparkline():
    # http://code.google.com/apis/chart/#sparkline  
    chart = Sparkline([27,25,25,25,25,27,100,31,25,36,25,25,39,
        25,31,25,25,25,26,26,25,25,28,25,25,100,28,27,31,25,
        27,27,29,25,27,26,26,25,26,26,35,33,34,25,26,25,36,25,
        26,37,33,33,37,37,39,25,25,25,25], encoding='text')
    chart.color('0077CC')
    chart.size(200,40)
    chart.marker('B', 'E6F2FA',0,0,0)
    chart.line(1,0,0)
    return chart

@check_sum('a1d1801762105d58f67c544be36e2af7bf69a2a8')
def test_guide_bhs():
    # http://code.google.com/apis/chart/#bar_charts
    chart = HorizontalBarStack('ello', encoding='simple')
    chart.color('4d89f9')
    chart.size(200,125)        
    return chart

@check_sum('e65f1bea45ae7197943366d8de1268aad6e5b66d')
def test_guide_bvs():
    chart = VerticalBarStack([ [10,50,60,80,40],[50,60,100,40,20] ], encoding='text')
    chart.color('4d89f9', 'c6d9fd')
    chart.size(200,125)
    return chart

@check_sum('a327b4be8fa55deccba5b4baab7680c75f621064')
def test_guide_bvs_scale():
    chart = VerticalBarStack([ [10,50,60,80,40],[50,60,100,40,20] ], encoding='text')
    chart.color('4d89f9', 'c6d9fd')
    chart.size(200,125)
    chart.scale(0,160)
    return chart
    
@check_sum('b051f7ab51afd534f89095fab7db3c161fcb3bc3')
def test_guide_bhg():
    chart = HorizontalBarGroup(['el','or'], encoding='simple')
    chart.color('4d89f9','c6d9fd')
    chart.size(200,125)
    return chart

@check_sum('36ce2efaf74fad1912b8351147b821d0253f9c56')
def test_guide_bvg():
    chart = VerticalBarGroup(['hello','world'], encoding='simple')
    chart.color('4d89f9','c6d9fd')
    chart.size(200,125)
    return chart

@check_sum('83ff879fc173bbcf80350d62d7d880b619424d10')
def test_guide_chbh_clipped():
    chart = HorizontalBarStack('hello', encoding='simple')
    chart.color('4d89f9')
    chart.size(200,125)
    return chart

@check_sum('a6b043ed705fe90afef78c393403fc813ca7aa1e')
def test_guide_chbh_size():
    chart = HorizontalBarStack('hello', encoding='simple')
    chart.color('4d89f9')
    chart.size(200,125)
    chart.bar(10)
    return chart

@check_sum('9703b8ca52e8c38c37353c6935d5053f8120c37a')
def test_guide_radar():
    # Create a radar chart w/ multiple lines
    chart = Radar([ [77,66,15,0,31,48,100,77],[20,36,100,2,0,100] ], encoding='text')  
    chart.size(200,200)
    chart.color('red','FF9900')
    chart.line(2,4,0)
    chart.line(2,4,0)        
    chart.axes('x')
    chart.axes.label(0, 0,45,90,135,180,225,270,315)
    chart.axes.range(0, 0,360)
    return chart

@check_sum('2391235ee09f58cc194eaf16b3c87f839613ebc5')
def test_guide_map():
    # Make a map of the US as in the API guide
    chart = Map('fSGBDQBQBBAGABCBDAKLCDGFCLBBEBBEPASDKJBDD9BHHEAACAC', encoding='simple')
    chart.color('f5f5f5','edf0d4','6c9642','365e24','13390a')
    chart.fill('bg','s','eaf7fe')
    chart.size(440,220)
    chart.map('usa', 'NYPATNWVNVNJNHVAHIVTNMNCNDNELASDDCDEFLWAKSWIORKYMEOHIAIDCTWYUTINILAKTXCOMDMAALMOMNCAOKMIGAAZMTMSSCRIAR')
    return chart

@check_sum('cdad708a80c49b705212d098bf83f9ccb30610aa')
def test_guide_meter():
    # Create a simple Google-O-Meter with a label
    chart = Meter(70)
    chart.label('Hello')
    chart.size(225,125)
    return chart

@check_sum('9b0fb89df43d69b64755153b919e598180fc1a9d')
def test_numpy():
    # Test to see whether numpy arrays work correctly
    # Must have numpy installed to do this test correctly
    data = [10,20,30,40,50,60,70,80,90]
    try:
        from numpy import array
        data = array(data)
    except ImportError:
        _print('Warning: numpy must be installed to do this test correctly')
    chart = Radar(data, encoding='text')
    chart.size(200,200)    
    return chart

@check_sum('cb6325bb97779fabdc77c8ab76e6bf4ed1d5447b')
def test_concentric_pie():
    # Using concentric pie charts
    chart = PieC(['Helo','Wrld'], encoding='simple')
    chart.size(200,100)
    return chart
    
@check_sum('0c3dee619eb6c43d8b5405f537438467a7d736e5')
def test_financial():
    # Fancy markers for financial data
    chart = Line([[0,5,10,7,12,6],[35,25,45,47,24,46],[15,40,30,27,39,54],[70,55,63,59,80,60]], encoding='text')
    chart.marker('F','blue',0,'1:4',20)
    chart.size(200,125)
    return chart
    
@check_sum('c01b4efa34a4850f6888ebcde3d9ee28ba621f85')
def test_bar_text():
    # Using text markers in a bar chart
    chart = HorizontalBarGroup([[40,60],[50,30]], encoding='text')
    chart.size(200,125)
    chart.marker('tApril mobile hits','black',0,0,13)
    chart.marker('tMay mobile hits','black',0,1,13,-1)
    chart.marker('tApril desktop hits','black',1,0,13)
    chart.marker('tMay desktop hits', 'black',1,1,13)
    chart.color('FF9900','FFCC33')
    return chart
    
@check_sum('4f995e40b16a49d0c407c0bf1b536f7642f6253d')
def test_margins():
    chart = Line(['Uf9a','a3fG'], encoding='simple')
    chart.size(250,100)
    chart.label(1,2,3,4)
    chart.fill('bg','s','e0e0e0')
    chart.color('black','blue')
    chart.margin(20,20,20,30,80,20)
    chart.legend('Temp','Sales')
    return chart
    
@check_sum('5aae24644331ca33c0cb83dc01a34d389edd6adf')
def test_min_max():
    chart = Line('mHMza', encoding='simple')
    chart.color('008000')
    chart.line(2.0,4.0,1.0)
    chart.size(200,140)
    chart.axes('x')
    chart.axes.label(0, None,'t',None,'F',None)
    chart.marker('tMin','blue',0,1,10)
    chart.marker('fMax','red',0,3,15)
    chart.margin(0,0,30,0)
    return chart

@check_sum('ee50ac8a04073a7933612bfcdfba4f759de0e55e')
def test_text():
    # Make a text chart label w/ any text you like
    # Google automagically ignores white space and spaces text correctly
    text = '''
    1600 Ampitheatre Parkway
    Mountain View, CA
    (650)+253-0000
    '''
    chart = Text('darkred',16,'h','red','b',text)
    return chart

@check_sum('430c921aa8d73e80feae07b2ba04909c6a6b1ab3')
def test_letter_pin():
    # Simple map pin w/ a letter/number
    return Pin('pin_letter','A','red','black')

@check_sum('01110b589dbe1ed9aed7a3eb057bd9020b6d21a2')
def test_icon_pin():
    # Map pin w/ a certain icon
    return Pin('pin_icon','home','yellow')

@check_sum('97cd7dac85adad57e2cf8209d0795a4f5216cb6a')
def test_adv_letter_pin():
    return Pin('xpin_letter','star','A','aqua','black','red')

@check_sum('b8a2ec08aeb3fb0a839598a82dfba02c7cdc8638')
def test_adv_icon_pin():
    # Map pin w/ cool icon
    return Pin('xpin_icon','star','home','aqua','red')

@check_sum('42558403a2a9d66e9b54deea094114029c86d529')
def test_text_pin():
    # Straight up map pin w/ following text
    return Pin('spin',1.2,30,'FFFF88',10,'_','Foo\nBar')

@check_sum('84ab40101b56759dc073d864c4d0ebddd546d2be')
def test_text_withspaces_pin():
    # Straight up map pin w/ following text
    return Pin('spin',1.2,30,'FFFF88',10,'_','Foo Bar\nBar')
    
@check_sum('a3a55893fc130abd814c80c9841e3547e2c2877a')
def test_sticky_note():
    # Note w/ title and text 
    return Note('note_title','pinned_c',1,'darkgreen','l',"Joe's\nToday 2-for-1 !\n555-1234")

@check_sum('9375cabf12b442764db34862c68ae74f85c42ca9')
def test_thought_note():
    # Thought bubble note
    return Note('note','thought',1,'navy','h',"wouldn't it be\ngreat to eat\nat Joe's?")

@check_sum('9a7988231bc235bda5ab21e19288fba5b554adf7')
def test_weather_note():
    # First example w/ true utf-8 encoding
    return Note('weather','taped_y','sunny','Barcelona','max 25°','min 15°')
    
@check_sum('65d1df5f7bda98cfaea2a96dfe8dcca1058c444c')
def test_small_bubble_icon():
    # Small bubble marker
    return Bubble('icon_text_small','petrol','bb','$3/gal','khaki','black')

@check_sum('f09ebedf3cc5c461604539afdcff9dac09817d71')
def test_large_bubble_icon():
    # Larger bubble marker
    return Bubble('icon_text_big','snack','bb','$2.99','ffbb00','black')

@check_sum('20c705a0e3038594749b8b9cdf8f09e470e76b17')
def test_large_bubble_icon_texts():
    # Large bubble marker w/ icon and multiline text
    return Bubble('icon_texts_big','petrol','bb','khaki','black','LoCost Fuel\n$3.05/gal unleaded\n$2.10/gal diesel')

@check_sum('ff1474c87defa687727a4ee42dca9c641a46668c')
def test_large_bubble_texts():
    # Large bubble marker with just text
    return Bubble('texts_big','bb','teal','khaki',"Joe's Restaurant\n123 Long St\n92745 Mountain View")

@check_sum('ead386ad75dabb21e13fd4b3a357d6025bdd4506')
def test_czech_and_unicode():
    # Submitted by anedvedicky
    chart = VerticalBarStack( [[10], [20], [30]], encoding = 'text')
    chart.color('green','lime','red')
    chart.label('šýŽěůčář...')
    chart.legend('šýŽěůčář...','∫µ≤','´®†¥¨ˆøπ¬˚≤µ˜')
    return chart

@check_sum('9cab6532523a353cd87d3edec45d9222de9dde5d')
def test_tick_marks():
    chart = Line('cEAELFJHHHKUju9uuXUc', encoding="simple")
    chart.color('76A4FB')
    chart.size(220, 125)
    chart.line(2)
    chart.axes('xyrx')
    chart.axes.range(1, 0,4)
    chart.axes.label(2, 'min','avg','max')
    chart.axes.label(3, 'Jan','Feb','Mar')
    chart.axes.style(2, '0000DD',13,-1,'t','FF0000')
    chart.axes.position(2, 10,35,95)
    chart.axes.tick(1,10)
    chart.axes.tick(2,-180)
    return chart

@check_sum('8ec06bda7223eb500e7f0357efd6e717543d9abb')
def test_currency_bar():
    chart = VerticalBarStack([43.56,35.62,48.34,57.50,67.30,60.91])
    chart.color('blue')
    chart.bar(17,15)
    chart.marker('N*cEUR1*','black',0,-1,11)
    return chart

@check_sum('0e02091bfe03d6cf31704c87de01dea6c47e3717')
def test_circle_diamonds():
    chart = Line(['Hello','world'])
    chart.marker('o','ff9900',0,-1,15.0)
    chart.marker('d','ff0000',1,-1,10.0)
    return chart

@check_sum('0d256be1fe2efc32a76564e9de76d64463fba7fc')
def test_pie_whitespace_plus():
    # Simple pie chart based on list
    chart = Pie3D( [1,2,3,4] )
    chart.size(400, 150)
    chart.label('A','B','C','D')
    chart.legend('12 to 15','16 to 20','21 to 29','30+')
    chart.color('00dd00')
    return chart

@check_sum('4e53c7add42ce61a933ce106a9854222c54c9147')
def test_fromstring():
    url='http://chart.apis.google.com/chart?cht=p3&chd=t:60,40&chs=250x100&chl=Hello|World'
    return BaseChart.fromurl(url)


def _test_encoding(encoding, expected, data, scale):
    codec = Encoder(encoding, scale)
    assert codec.encode(data) == expected
    assert codec.decode(codec.encode(data)) == [data]
    
def test_simple_encode():
    _test_encoding('simple', 's:Ab9', [0,27,61], 61)
    
def test_text_encode():
    _test_encoding('text', 't:0.0,10.0,100.0,-1.0,-1.0', [0,10,100,-1,-1], (0,100))

def test_extended_encode():
    _test_encoding('extended', 'e:AH-HAA..', [7,3975,0,4095], 4095)



if __name__ == '__main__':
    def get_chart(chart):
        return getattr(TestChartTypes('test_%s'%chart), 'test_%s'%chart)()
    def saveall():
        import os
        if not os.path.isdir('tests'):
            os.mkdir('tests')
        for chart in TestChartTypes.all:
            chartobj = get_chart(chart)
            chartobj.save('tests/%s'%chart)
    
    import sys
    calls = {
        'unit': lambda: unittest.main(),
        'save': lambda: saveall(),
    }
    arg = sys.argv[-1]
    sys.argv = sys.argv[:-1]
    if arg in calls:
        calls[arg]()
    else:
        for chart in TestChartTypes.all:
            _print( chart,'\t',get_chart(chart))
