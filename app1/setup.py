#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name='simplistic',
    version='0.1.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    description='Simplistic HTTP Server',
    author='Simplistic',
    author_email='simplistic@github.com',
    install_requires=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points='''
        [console_scripts]
        simplistic=simplistic.simplisticHTTPServer:run
    ''',
)

