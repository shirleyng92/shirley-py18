# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:10:56 2018

@author: shirley.ng
"""

import datetime

currentDate = datetime.date.today()
print (currentDate)
print (currentDate.year)
print (currentDate.month)
print (currentDate.day)

print (currentDate.strftime('%d %b,%y'))
print (currentDate.strftime('%d %b,%Y'))

print (currentDate.strftime
('Please attend our event %A, %B %d in the year %Y'))