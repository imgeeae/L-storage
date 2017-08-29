#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Information of this python file using unicode

You need to write down somethings for using unicode like 'Han-geul'.
And you can get when it is, where you are, which interpreter you use.
"""

import sys
import os
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

# Get current time (yyyy-mm-dd_hh_mm)
now = str(datetime.datetime.now())
now = now[0:16]
now = str.replace(now, " ", "_") # ing.replace()
now = str.replace(now, ":", "_")

# Get current directory
here = os.getcwd()

print now
print here
print sys.executable


