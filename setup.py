from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os

from codecs import open

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(name='csodbpy',
    version='0.1.0',
    description='Libraries and utilities for accessing NASA Community Snow Observations database',
    author='Anthony Arendt',
    author_email='arendta@uw.edu',
    license='MIT',
    url='https://github.com/communitysnowobs/cso-api',
    packages=find_packages(),
    long_description=long_description
)