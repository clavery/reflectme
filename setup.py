#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(package_dir, 'requirements.txt')) as f:
    requires = [p.rstrip() for p in f.readlines()]


setup(
    name='reflectme',
    version='0.0.4',
    description='Simple HTTP server for recording requests and returning arbitrary responses.',
    author='Charles Lavery',
    author_email='charles.lavery@gmail.com',
    url='https://github.com/clavery/reflectme',
    packages=find_packages(),
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
        'console_scripts': ['reflectme = reflectme.cli:main'],
    },
)
