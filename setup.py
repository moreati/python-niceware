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
    version='0.2.1',
    description='Convert cryptographic keys to human-readable phrases, or generate random-yet-memorable passphrases',
    long_description=readme + '\n\n' + history,
    author='Alex Willmer',
    author_email='alex@moreati.org.uk',
    url='https://github.com/moreati/python-niceware',
    packages=[
        'niceware',
    ],
    entry_points={
        'console_scripts': [
            'niceware = niceware.__main__:main',
        ]
    },
    package_dir={'niceware': 'niceware'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='niceware diceware passphrase password encryption',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
