#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

DESCRIPTION = (
    "A collection of utilities for working in Google's Colaboratory for ML."
)
LONG_DESCRIPTION = open('README.rst').read()
VERSION = '0.0'

#setup_requires = (
#    ['pytest-runner'] if any(x in sys.argv for x in ('pytest', 'test', 'ptr')) else []
#)


setup(
    name='google-colab-utils',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Luke Bechtel',
    author_email='luke@lukebechtel.com',
    url='http://lukebechtel.com',
    license='MIT',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[], #setup_requires,
    tests_require=['pytest'],
    #test_suite="",
    install_requires=[],
    keywords=['google', 'colab', 'jupyter', 'ipynb', 'data science'],
    python_requires='>=2.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
