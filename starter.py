#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Example of python file using unicode

We need to write down somethings for using unicode like 'Han-geul'
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = "Ellena Jiae Lim"
__copyright__ = "Copyright 2017, Mackevision Korea"

__license__ = "GPL"
__version__ = "1.1.0"
__maintainer__ = "Ellena Jiae Lim"
__email__ = "ellena.lim@mackevision.com"
__status__ = "Production - PDM"

"""
# Get current time (yyyy-mm-dd_hh_mm)
now = str(datetime.datetime.now())
now = now[0:16]
now = str.replace(now, " ", "_")
now = str.replace(now, ":", "_")

# Get current directory
here = os.getcwd()

print now
print here

print sys.executable
print sys.path
"""