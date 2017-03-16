#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [
    'flake8',
    'pytest',
]

setup(
    name='niceware',
    version='0.1.0',
    description='Convert cryptographic keys to human-readable phrases, or generate random-yet-memorable passphrases',
    long_description=readme + '\n\n' + history,
    author='Alex Willmer',
    author_email='alex@moreati.org.uk',
    url='https://github.com/moreati/python-niceware',
    packages=[
        'niceware',
    ],
    package_dir={'niceware': 'niceware'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='niceware',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
