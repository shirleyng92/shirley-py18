# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:32:44 2018

@author: shirley.ng
"""
####Example 1
##type1
#def add_item(item, item_list = []):
#    item_list.append(item)
#    print(item_list)

##type2    
##This way, everytime the function is called, it is independent
##not getting value from the last entries
def add_item(item, item_list = None):
    if item_list == None:
        item_list = []
    item_list.append(item)
    print(item_list)
    
    
####Example 2
def printDict(**kwargs):
    print(kwargs)
    
def printTuple(*args):
    print(args)