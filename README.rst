Google Chart Wrapper
======================


:Authors:
    Justin Quick <justquick@gmail.com>, and many more in AUTHORS.txt  
:Version: 1.0

::

    pip install google-chartwrapper==1.0.0
    

Second generation Python wrapper for the `Google Chart Image API <http://code.google.com/apis/chart/image/>`_.
Chart instances can render the URL of the actual Google chart and quickly insert into webpages on the fly or save images for later use.
Made for dynamic Python websites (Django, Zope, CGI, etc.) that need on the fly, dynamic chart image generation. Works for Python versions 2.3 to 3.2.::

    from gchart import Pie
    Pie([5,10]).title('Hello Pie').color('red','lime').label('hello', 'world')

This generates a chart instance that can be rendered/saved in many ways. The most useful is display on a website

.. image:: http://chart.apis.google.com/chart?chco=ff0000,00ff00&chd=s:f9&chs=300x150&cht=p3&chl=hello|world&chtt=Hello%20Pie&.png

Requirements
--------------

- Python 2.3 to 3.2

Optional

- PIL (for PNG image manipulation)
- Nose and Tox (for testing)

Usage
--------

Construction
^^^^^^^^^^^^^^

The chart takes any iterable python data type (now including numpy arrays)
and does the encoding for you::

    Data sets 
    >>> dataset = (1, 2, 3)
    Also 2 dimensional
    >>> dataset = [[3,4], [5,6], [7,8]]

Initialize the chart with a valid type (see API reference) and dataset::

    3D Pie chart
    >>> from gchart import BaseChart
    >>> BaseChart('p3', dataset)
    <BaseChart  p3 (1, 2, 3)>
    
    Encoding (simple/text/extended)
    >>> chart = BaseChart('p3', dataset, encoding='text')
    
    maxValue (for encoding values)
    >>> chart = BaseChart('p3', dataset, maxValue=100)
    
    Size
    >>> chart = BaseChart('p3', dataset, size=(300,150))
    
    OR directly pass in API parameters
    >>> chart = BaseChart('p3', dataset, chtt='My Cool Chart', chl='A|B|C')


Rendering, Viewing and Saving
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The wrapper has many useful ways to take the URL of your chart and output it 
into different formats like::

    URL of the actual Google chart
    >>> chart.url
    'http://chart.apis.google.com/chart?...'
    
    As an HTML <img> tag, keyword arguments will be added as tag attributes
    >>> chart.img(height=500,id="chart")
    '<img alt="" title="" src="http://chart.apis.google.com/chart?..." id="chart" height="500" >'
    
    Save chart to a file as PNG image, returns file name
    >>> chart.save('my-cool-chart')
    'my-cool-chart.png'
    
    Fetches the PngImageFile using the PIL module for image manipulation
    >>> chart.image()
    <PngImagePlugin.PngImageFile instance at 0xb795ee4c>
    
    Now that you have the image instance, the world is your oyster
    Try saving image as JPEG,GIF,etc.
    >>> chart.image().save('my-cool-chart.jpg','JPEG')
    
    Show URL directly in your default web browser
    >>> chart.show()
    
Examples
------------

See the `demo page <http://justquick.github.com/google-chartwrapper-demos/>`_ for tons of examples and source code


Testing 
--------

Tests are located in ``gchart/tests.py`` and contributions are welcome.
To run the tests, simply execute ``nosetests`` in the source checkout. 
If you have Tox installed and have the right Python environments setup,
you can test the module against them by running ``tox`` in the source checkout.


