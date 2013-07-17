#!/usr/bin/env python
from distutils.core import setup

setup(name='Rosuitta',
      version='0.0-dev',
      description='Django Suit-compatible Rosetta templates',
      author='Michał Bielawski',
      author_email='m.bielawski@merixstudio.com',
      url='https://bitbucket.org/merixstudio/rosuitta',
      packages=['rosuitta'],
      package_data={'rosuitta': ['templates/rosetta/*.html']})
