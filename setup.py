#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='BitlyShorter',
    version='1.0.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    packages=['shorter'],
    url='https://github.com/alexandrevicenzi/shorter',
    bugtrack_url='https://github.com/alexandrevicenzi/shorter/issues',
    license='MIT',
    description='Branded bitlink generator for Bitly',
    keywords='url, link, bitly, bitlink, short, shorturl',
    platforms='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Internet',
        'Topic :: Utilities',
    ],
)
