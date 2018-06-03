#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='hello',
    author='shaddygarg',
    version='1.0',
    author_email='shaddygarg1@gmail.com',
    description='My first maltego transform',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        '': ['*.gif', '*.png', '*.conf', '*.mtz', '*.machine']  # list of resources
    },
    install_requires=[
        'canari>=3.0'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
