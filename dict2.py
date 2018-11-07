# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:25:21 2018

@author: shirley.ng
"""



names = ['csev','cwen','csev','zqian','cwen']

counts = dict()
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
        
print(counts)

##Simplified by get function
counts = dict()
for name in names :
    counts[name] = counts.get(name,0)+1
print(counts)

#get the count of the name in 0 position
print(counts.get(name,0))

print(counts.get('cwen',0))
print(counts.get('aaa',0))