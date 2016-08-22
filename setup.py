#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='HIP2Unicode',
    version='1.5.0',
    description='Converter from HIP to Unicode',
    author='Nurono',
    author_email='while0pass@yandex.ru',
    url='https://github.com/while0pass/hip2unicode',
    packages=['hip2unicode', 'hip2unicode.conversions',
              'hip2unicode.representations'],
    zip_safe=False,
)
