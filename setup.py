#!/usr/bin/env python3

from setuptools import setup

setup (name = 'ugit',
        version = '1.0',
        pacalges = ['ugit'],
        entry_points = {
            'console_scripts' : [
                'ugit = ugit.cli:main'
                ]
            })
