# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:23 2018

@author: shirley.ng
"""

import datetime
birthday = input ("What is your birthday? (In DD/MM/YY) ")
birthdate = datetime.datetime.strptime(birthday,"%d/%m/%y").date()

print ("Your birth month is " + birthdate.strftime('%B'))
print ("Your birth date is " + birthdate.strftime('%d'))