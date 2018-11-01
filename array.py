# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:34:50 2018

@author: shirley.ng
"""

guests = ['MY','SC','Shir','Elaine']

##item from left start from 0
#print(guests[2])

##item from right start from -1
#print(guests[-1])

##replacing
#print('First value default: ' + guests[0])
#guests[0] = 'SS'
#print('First value is now: ' + guests[0])
#
##add new value
#guests.append('Jenny')
#print(guests[-1] + " is added to the guest list")
#
##to remove value
#print('2nd value is: ' + guests[1])
#
##remove by stating name
##guests.remove('SC')
##remove by index position
#del guests[1]
#
#print('2nd value after removing is: ' + guests[1])

##check index position
#print(guests.index('Shir'))

#printing a range of elements
for step in range(len(guests)):
    print(guests[step])

#scores = [10,20,30,40,50]
#print(scores[3])