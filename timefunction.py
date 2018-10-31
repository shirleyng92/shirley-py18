# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:08:24 2018

@author: shirley.ng
"""

import datetime

currentTime = datetime.datetime.now()

#provide YYYY-MM-DD HH:MM:SS.MS
print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

#24hour time format
print (datetime.datetime.strftime(currentTime,'%H:%M'))

#12hour time format
print (datetime.datetime.strftime(currentTime,'%I:%M %p'))