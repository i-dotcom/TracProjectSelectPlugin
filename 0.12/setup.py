#!/usr/bin/env python
# -*- coding: utf-8 -*-


from projectselect import __version__ as VERSION
from setuptools import setup

setup(
    name = 'ProjectSelect',
    version = VERSION,
    packages = ['projectselect'],
    package_data = { 'projectselect': ['htdocs/projectselect.js', ] },
    author = 'Marek Wywiał',
    author_email = 'marek.wywial@i-dotcom.pl',
    maintainer = 'Marek Wywiał',
    maintainer_email = 'marek.wywial@i-dotcom.pl',
    url = 'http://trac-hacks.org/',
    description = 'The ProjectSelect Plugin for Trac',
    entry_points={'trac.plugins': ['ProjectSelect = projectselect.projectselect']},
    keywords = 'trac multiproject project',
    license = 'BSD',
)

