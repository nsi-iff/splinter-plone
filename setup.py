from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='splinter-plone',
      version=version,
      description="Splinter integration for Plone",
      long_description="""\
Integration of Splinter, an open source tool for testing web applications with Plone CMS""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='splinter plone cms web acceptance testing',
      author='Ronaldo Amaral',
      author_email='rsantos@iff.edu.br',
      url='',
      license='',
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
