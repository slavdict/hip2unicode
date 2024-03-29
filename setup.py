#!/usr/bin/env python

from setuptools import setup

setup(
    name='HIP2Unicode',
    version='3.6.0',
    description='Converter from HIP to Unicode',
    author='Nurono',
    author_email='while0pass@yandex.ru',
    url='https://github.com/slavdict/hip2unicode',
    packages=['hip2unicode', 'hip2unicode.conversions',
              'hip2unicode.representations'],
    zip_safe=False,
    python_requires='>=3.5',
)
