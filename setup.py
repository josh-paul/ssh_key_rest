#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='ssh-key-rest',
    version='0.0.1',
    description=('Simple REST api to create, validate, and fingerprint ssh keys'),
    long_description=desc,
    url='https://github.com/josh-paul/check_servers',
    author='Josh Paul',
    author_email='trevalen@me.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='ssh key  rest ssh-key ssh-key-rest',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=['futures', 'requests', 'tabulate'],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
