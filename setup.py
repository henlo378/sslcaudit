# ----------------------------------------------------------------------
# SSLCAUDIT - a tool for automating security audit of SSL clients
# Released under terms of GPLv3, see COPYING.TXT
# Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
# ----------------------------------------------------------------------

import sys

# "distutils" goes away in Python 3.12. Import through "distutils" if Python version is less than 3.10 and through "setuptools" if Python 3.10 (or newer) is used (to avoid deprecation warning).
if ((sys.version_info.major == 3) and (sys.version_info.minor >= 10)):
    from setuptools import setup
else:
    from distutils.core import setup

setup(
    name='sslcaudit',
    author='Alexandre Bezroutchko',
    author_email='abb@gremwell.com',
    description='Utility to perform security audits of SSL/TLS clients',
    url='http://www.gremwell.com/sslcaudit',
    version='1.1',
    license='GPLv3',
    scripts=['bin/sslcaudit'],
    package_dir={'sslcaudit': 'sslcaudit'},
    packages=['sslcaudit', 'sslcaudit.core', 'sslcaudit.modules',
              'sslcaudit.modules.base', 'sslcaudit.modules.dummy',
              'sslcaudit.modules.sslcert', 'sslcaudit.modules.sslproto', 'sslcaudit.profile', 'sslcaudit.test',
              'sslcaudit.ui'],
    package_data={'sslcaudit': ['files/*']},
    requires=['m2crypto', 'qt4']
)
