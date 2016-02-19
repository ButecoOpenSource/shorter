#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='BitlyShorter',
    version='1.1.2',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    packages=['shorter'],
    install_requires=['PyYAML==3.11', 'requests==2.9.1', 'tornado==4.3'],
    include_package_data=True,
    url='https://github.com/alexandrevicenzi/shorter',
    bugtrack_url='https://github.com/alexandrevicenzi/shorter/issues',
    license='MIT',
    description='Branded bitlink generator for Bitly',
    keywords='url, link, bitly, bitlink, short, shorturl',
    platforms='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
    ],
)
