#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'reflectme',
]

requires = [
    'Flask==0.10.1',
    'Flask-SQLAlchemy==1.0',
    'Flask-WTF==0.9.5',
    'Pygments==1.6',
    'appdirs==1.2.0',
]

setup(
    name='reflectme',
    version='0.0.1',
    description='Simple HTTP server for recording requests and returning arbitrary responses.',
    author='Charles Lavery',
    author_email='charles.lavery@gmail.com',
    url='https://github.com/clavery/reflectme',
    packages=packages,
    package_dir={'reflectme': 'reflectme'},
    package_data={
        'reflectme': [
            'static/*',
            'templates/*'
        ],
    },
    include_package_data=True,
    install_requires=requires,
    license='MIT License',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
    entry_points = {
        'console_scripts': [ 'reflectme = reflectme.cli:main' ],
    },
)
