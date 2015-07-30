#!/usr/bin/env python

from distutils.core import setup

setup(
    name='HIP2Unicode',
    version='1.0',
    description='Converter from HIP to Unicode, written in Python',
    author='Andrej Hitrov',
    author_email='andrej@hitrov.ru',
    url='https://github.com/while0pass/hip2unicode',
    packages=[
        'hip2unicode', 'hip2unicode.conversions', 'hip2unicode.representations',
        'hip2unicode.tools'
    ],
    zip_safe=False,
)
