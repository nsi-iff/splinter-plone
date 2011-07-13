from setuptools import setup, find_packages
import sys, os

version = '0.1.0'
readme = open('README.rst').read()

setup(name='splinter-plone',
    version=version,
    description="Splinter integration for Plone",
    long_description=readme,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='splinter plone cms web acceptance testing',
    author='Ronaldo Amaral',
    author_email='rsantos@iff.edu.br',
    url='https://github.com/nsi-iff/splinter-plone',
    license='GNU General Public License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'Products.PloneTestCase',
        #  'Testing',
        'splinter'
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
