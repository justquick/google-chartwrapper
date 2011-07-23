from setuptools import setup, find_packages

CLASSIFIERS = (
    ('Development Status :: 4 - Beta'),
    ('Environment :: Console'),
    ('Environment :: Web Environment'),
    ('Framework :: Django'),
    ('Intended Audience :: Developers'),
    ('Intended Audience :: Science/Research'),
    ('Intended Audience :: System Administrators'),
    ('License :: OSI Approved :: BSD License'),
    ('Natural Language :: English'),
    ('Operating System :: OS Independent'),
    ('Topic :: Artistic Software'),
    ('Topic :: Internet :: WWW/HTTP'),
    ('Topic :: Internet :: WWW/HTTP :: Dynamic Content'),
    ('Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries'),
    ('Topic :: Multimedia'),
    ('Topic :: Multimedia :: Graphics'),
    ('Topic :: Scientific/Engineering :: Visualization'),
    ('Topic :: Software Development :: Libraries :: Python Modules'),
    ('Topic :: Utilities'),
)

DESCRIPTION = """Second generation Python wrapper for the `Google Chart Image API <http://code.google.com/apis/chart/image/>`_.
Chart instances can render the URL of the actual Google chart and quickly insert into webpages on the fly or save images for later use.
Made for dynamic Python websites (Django, Zope, CGI, etc.) that need on the fly, dynamic chart image generation. Works for Python versions 2.3 to 3.2.
"""

setup(
    name='google-chartwrapper',
    version='1.0.0',
    description='Python Google Chart Wrapper',
    long_description=DESCRIPTION,
    author="Justin Quick",
    author_email='justquick@gmail.com',
    url='https://github.com/justquick/google-chartwrapper',
    classifiers=CLASSIFIERS,
    packages=find_packages('.', ('examples',)),
)